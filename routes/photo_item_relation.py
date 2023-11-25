from typing import List

from bson import ObjectId
from fastapi import APIRouter, File, UploadFile

from app.core.picture.picture_helper import delete_picture, save_picture
from config.db import db
from models.photo_item_relation import PhotoItemRelation
from schemas.photo_item_relation import (
    photo_item_relation_entities,
    photo_item_relation_entity,
)

relation_router = APIRouter()


@relation_router.post("/")
def add_photo_to_item(item_id, photo: List[UploadFile] = File(...)):
    for photo_item in photo:
        photo_url = save_picture(file=photo_item)
        relation = PhotoItemRelation(photo_url=photo_url, item_id=item_id)
        db.items_photo.insert_one(relation.dict(exclude_none=True))
    return photo_item_relation_entities(db.items_photo.find({"item_id": item_id}))


@relation_router.get("/")
def get_items_photo(item_id):
    return photo_item_relation_entities(db.items_photo.find({"item_id": item_id}))


@relation_router.delete("/")
def delete_all_items_photo(item_id):
    relations = photo_item_relation_entities(db.items_photo.find({"item_id": item_id}))
    db.items_photo.delete_many({"item_id": item_id})
    for relation in relations:
        delete_picture(relation.get("photo_url"))
    return {"chat_message": "success"}


@relation_router.delete("/{relation_id}")
def delete_items_photo(relation_id):
    relation = photo_item_relation_entity(
        db.items_photo.find_one_and_delete({"_id": ObjectId(relation_id)})
    )
    delete_picture(relation.get("photo_url"))
    return {"chat_message": "success"}
