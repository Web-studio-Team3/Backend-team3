from fastapi import APIRouter, UploadFile, File
from bson import ObjectId
from typing import List
from helpers.save_picture import save_picture, delete_picture

from models.photo_item_relation import PhotoItemRelation
from config.db import db
from schemas.photo_item_relation import photo_item_relation_entity, \
    photo_item_relation_entities

relation_router = APIRouter()

base_route = "/items/{item_id}/photo/"


@relation_router.post(base_route, tags=["item_photo"])
def add_photo_to_item(item_id, photo: List[UploadFile] = File(...)):
    for photo_item in photo:
        photo_url = save_picture(file=photo_item)
        relation = PhotoItemRelation(photo_url=photo_url, item_id=item_id)
        db.items_photo.insert_one(relation.dict(exclude_none=True))
    return photo_item_relation_entities(db.items_photo.find({"item_id": item_id}))


@relation_router.get(base_route, tags=["item_photo"])
def get_items_photo(item_id):
    return photo_item_relation_entities(db.items_photo.find({"item_id": item_id}))


@relation_router.delete(base_route, tags=["item_photo"])
def delete_all_items_photo(item_id):
    relations = photo_item_relation_entities(db.items_photo.find({"item_id": item_id}))
    db.items_photo.delete_many({"item_id": item_id})
    for relation in relations:
        delete_picture(relation.get("photo_url"))
    return {
        "message": "success"
    }


@relation_router.delete("/photo_item_relation/{relation_id}", tags=["item_photo"])
def delete_items_photo(relation_id):
    relation = photo_item_relation_entity(db.items_photo.find_one_and_delete({"_id": ObjectId(relation_id)}))
    delete_picture(relation.get("photo_url"))
    return {
        "message": "success"
    }
