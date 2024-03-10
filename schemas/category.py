from bson import ObjectId

from config.db import db


def categoryTreeEntity(item) -> dict:
    for category in item:
        # print(category)
        if category == None:
            continue
        category["id"] = str(category.pop("_id"))
        category["title"] = category["title"]
        if "childs" in category.keys() and len(category["childs"]) > 0:
            category["childs"] = categoryTreeEntity(category["childs"])
    return item


def categoryEntity(item, parent=None) -> dict:
    return {
        "id": str(item["_id"]),
        "title": item["title"],
    }


def categoriesEntity(entity, parents) -> list:
    return [categoryEntity(item, parent) for item, parent in list(zip(entity, parents))]


def categoryRelationEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "parent_category": item["parent_category"]
        if "parent_category" in item.keys()
        else None,
        "child_category": item["child_category"]
        if "child_category" in item.keys()
        else None,
    }


def categoriesRelationEntity(entity) -> list:
    return [categoryRelationEntity(item) for item in entity]
