from datetime import date, datetime
from typing import List, Optional

from bson.objectid import ObjectId
from pydantic import BaseModel, Field


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class ItemModel(BaseModel):
    # id: str
    category_id: Optional[PyObjectId] = Field(...)
    title: Optional[str] = Field(...)
    description: Optional[str] = None
    condition: Optional[str] = Field(...)
    address: Optional[str] = None
    cost: Optional[str] = Field(...)
    status: Optional[str] = Field(...)
    # owner_id: Optional[ObjectId] = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "category_id": "635c427c38f70edcfd42f32f",
                "title": "Ноутбук",
                "description": "Крутой очень жесть прям",
                "condition": "б/у",
                "address": "Малая Семеновская, 12",
                "cost": "300$",
                "status": "Бронь",
            }
        }
