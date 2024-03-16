from bson import ObjectId

from config.db import db


def itemEntity(item) -> dict:
    if item:
        return {
            "id": str(item["_id"]),
            "category": str(item["category_id"]),
            "title": item["title"],
            "description": item["description"],
            "condition": item["condition"],
            "address": item["address"],
            "cost": item["cost"],
            "status": item["status"],
            # "owner": item["owner_id"],
        }
    else:
        return {
            "error": "Not Found",
        }


def itemsEntity(entity) -> list:
    return [itemEntity(item) for item in entity]
