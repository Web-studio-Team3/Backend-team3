def photo_item_relation_entity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "photo_url": str(item["photo_url"]),
        "item_id": str(item["item_id"]),
    }


def photo_item_relation_entities(items) -> list:
    return [photo_item_relation_entity(item) for item in items]
