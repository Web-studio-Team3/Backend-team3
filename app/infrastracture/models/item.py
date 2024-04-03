from typing import Optional

from bson.objectid import ObjectId
from pydantic import BaseModel

from app.core.item.entities.item import Item


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, ObjectId):
            raise TypeError("ObjectId required")
        return str(v)


class ItemModel(BaseModel):
    category_id: ObjectId
    title: str
    description: str
    condition: str
    address: str
    cost: str
    status: str
    buyer_id: Optional[ObjectId]
    seller_id: ObjectId

    class Config:
        arbitrary_types_allowed = True


def from_entity(item: Item) -> ItemModel:
    return ItemModel(
        category_id=ObjectId(item.category_id),
        title=item.title,
        description=item.description,
        condition=item.condition,
        address=item.address,
        cost=item.cost,
        status=item.status,
        buyer_id=ObjectId(item.buyer_id),
        seller_id=ObjectId(item.seller_id),
    )
