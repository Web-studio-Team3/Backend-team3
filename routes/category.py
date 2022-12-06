from gettext import find
from traceback import print_tb
from fastapi import APIRouter, Query
from fastapi.responses import FileResponse
from bson import ObjectId, objectid
import json

from models.category import CategoryModel, CategoryRelationModel
from config.db import db
from schemas.category import categoryEntity, categoriesEntity, categoryTreeEntity

category_router = APIRouter()

# @category_router.get('/categories/', tags=["categories"])
# async def find_all_categories():
#     return categoriesEntity(db.categories.find())

# @category_router.post('/categories/', tags=["categories"])
# async def create_category(category: CategoryModel):
#     categoryId = db.categories.insert_one(dict(category)).inserted_id
#     return categoriesEntity(db.categories.find({"_id": ObjectId(categoryId)}))

# @category_router.get('/categories/{category_id}', tags=["categories"])
# async def find_one_category(category_id):
#     return categoryEntity(db.categories.find_one({"_id": ObjectId(category_id)}))

# @category_router.put('/categories/{category_id}', tags=["categories"])
# async def update_category(category_id, category: CategoryModel):
#     db.categories.find_one_and_update({"_id": ObjectId(category_id)}, {
#         "$set": dict(category)
#     })
#     return categoryEntity(db.categories.find_one({"_id": ObjectId(category_id)}))

# @category_router.delete('/categories/{category_id}', tags=["categories"])
# async def delete_category(category_id):
#     db.categories.find_one_and_delete({'_id': ObjectId(category_id)})
#     return categoriesEntity(db.categories.find())

# Category relation
@category_router.get('/')
def find_all_categories():
    # parentCategories = []

    # categoriesRelation = db.categories_relation.find().sort('child_category_id')
    # # print(list(categoriesRelation))
    # for relation in categoriesRelation:
    #     print(relation.keys())
    #     if "parent_category_id" in relation.keys():
    #         parentCategories.append(db.categories.find_one({'_id': ObjectId(relation["parent_category_id"])}))
    #     else:
    #         parentCategories.append(None)
    #     print(parentCategories)

    categoriesTree = []
    allCategories = list(db.categories.find())
    iterCategories = allCategories.copy()
    # print(allCategories))
    i = 0
    for category in allCategories:
        i = 1
        # print(category)
        # print(allCategories)
        if category != None and "childs" in category.keys() and len(category["childs"]) > 0:
            # print(category)
            allCategories[allCategories.index(category)] = None
            childCategories, allCategories = next_lvl_category(category["childs"], allCategories)
            category["childs"] = childCategories
            category["_id"] = str(category["_id"])
            categoriesTree.append(category)
    
    for category in allCategories:
        if category != None:
            category["_id"] = str(category["_id"])
            categoriesTree.append(category)

    print(allCategories)
    # return categoriesTree

    return categoryTreeEntity(categoriesTree)

    # return categoriesEntity(
    #     db.categories.find().sort('_id'),
    #     parentCategories
    # )
    
def next_lvl_category(categories, allCategories):
    nextLvlCategories = []
    for category in categories:
        nextLvlCategory = db.categories.find_one({"_id": ObjectId(category)})
        allCategories[allCategories.index(nextLvlCategory)] = None
        nextLvlCategory["_id"] = str(nextLvlCategory["_id"])
        if "childs" in nextLvlCategory.keys() and len(nextLvlCategory["childs"]) > 0:
            childCategories, allCategories = next_lvl_category(nextLvlCategory["childs"], allCategories)
            nextLvlCategory["childs"] = childCategories
        nextLvlCategories.append(nextLvlCategory)
    return nextLvlCategories, allCategories

@category_router.post('/')
async def create_category(
        category: CategoryModel, 
        parent_category=Query(
            "Не указано",
            enum=[*[category["title"] for category in db.categories.find()]]
        )
    ):
    
    category = dict(category)
    category["childs"] = []
    childCategory = db.categories.insert_one(category)
    parentCategory = db.categories.find_one({"title": parent_category})
    if "childs" not in parentCategory.keys():
        parentCategory["childs"] = []
    parentCategory["childs"].append(childCategory.inserted_id)
    
    db.categories.find_one_and_update({"_id": ObjectId(parentCategory["_id"])}, {
        "$set": parentCategory
    })

    return categoryEntity(
        db.categories.find_one({"_id": childCategory.inserted_id})
    )

    # categoryRelation = {
    #     "child_category_id": childCategoryId 
    # }

    # parentCategoryId = None
    # if parentCategory:
    #     parentCategoryId = parentCategory["_id"]
    #     categoryRelation["parent_category_id"] = parentCategoryId
    
    # db.categories_relation.insert_one(dict(categoryRelation))

    # if parentCategoryId:
    #     return categoryEntity(
    #         db.categories.find_one({"_id": ObjectId(childCategoryId)}),
    #         parentCategory,
    #     )
    # else:
    #     return categoryEntity(
    #         db.categories.find_one({"_id": ObjectId(childCategoryId)}),
    #     )

@category_router.get('/{category_id}')
async def find_one_category(category_id):
    # parentCategoryId = db.categories_relation.find_one({"child_category_id": ObjectId(category_id)})["parent_category_id"]

    return categoryEntity(
        db.categories.find_one({"_id": ObjectId(category_id)}),
        # db.categories.find_one({"_id": ObjectId(parentCategoryId)}),
    )

@category_router.put('/{category_id}')
async def update_category(
        category_id,
        category: CategoryModel,
        parent_category=Query(
            "Не указано",
            enum=[*[cat["title"] for cat in find_all_categories()]] if find_all_categories() 
            else ["Не указано"]
        )
    ):

    category = dict(category)

    parentCategory = db.categories.find_one({"childs": ObjectId(category_id)})
    if parentCategory:
        parentCategory["childs"].remove(ObjectId(category_id))
        db.categories.find_one_and_update({"_id": ObjectId(parentCategory["_id"])}, {
        "$set": parentCategory
        })
    
    newParent = db.categories.find_one({"title": parent_category})
    newParent["childs"].append(ObjectId(category_id))

    category["childs"] = db.categories.find_one({"_id": ObjectId(category_id)})["childs"]
    
    db.categories.find_one_and_update({"_id": ObjectId(category_id)}, {
        "$set": category
    })
    
    db.categories.find_one_and_update({"_id": ObjectId(newParent["_id"])}, {
        "$set": newParent
    })
    
    # parentCategory = db.categories.find_one({"title": parent_category})
    # db.categories_relation.find_one_and_update({"child_category_id": ObjectId(category_id)}, {
    #     "$set": {
    #         "parent_category_id": parentCategory['_id']
    #     }
    # })
    

    return categoryEntity(
        db.categories.find_one({"_id": ObjectId(category_id)}),
        # parentCategory
    )

@category_router.delete('/{category_id}')
async def delete_category(category_id):
    db.categories.find_one_and_delete({'_id': ObjectId(category_id)})
    db.categories_relation.find_one_and_delete({'child_category_id': ObjectId(category_id)})

    parentCategories = []

    categoriesRelation = db.categories_relation.find().sort('child_category_id')
    for relation in categoriesRelation:
        if "parent_category_id" in relation.keys():
            parentCategories.append(db.categories.find_one({'_id': relation["parent_category_id"]}))
        else:
            parentCategories.append(None)

    return categoriesEntity(
        db.categories.find().sort('_id'),
        parentCategories
    )