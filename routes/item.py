from fastapi import APIRouter, Query
from bson import ObjectId, objectid

from models.item import ItemModel
from config.db import db
from schemas.item import itemEntity, itemsEntity

item_router = APIRouter()


@item_router.get('/items/', tags=["items"])
def find_all_items():
    return itemsEntity(
        db.item.find().sort('_id'),
    )

@item_router.post('/items/', tags=["items"])
async def create_item(item: ItemModel):
    itemId = db.item.insert_one(item.dict(exclude_none=True)).inserted_id

    return itemEntity(
        db.item.find_one({"_id": ObjectId(itemId)})
    )

@item_router.get('/items/{item_id}', tags=["items"])
async def find_one_item(item_id):
    return itemEntity(
        db.item.find_one({"_id": ObjectId(item_id)}),
    )

@item_router.put('/items/{item_id}', tags=['items'])
async def update_item(item_id, item: ItemModel):
    item = dict(item)
    db.item.find_one_and_update({"_id": ObjectId(item_id)}, {
        "$set": item
    })
    return itemEntity(
        db.item.find_one({"_id": ObjectId(item_id)}),
    )

@item_router.delete('/items/{item_id}', tags=["items"])
async def delete_item(item_id):
    db.item.find_one_and_delete({'_id': ObjectId(item_id)})
    return itemsEntity(
        db.item.find().sort('_id'),
    )