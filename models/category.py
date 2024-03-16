from datetime import date, datetime
from typing import List, Optional

from bson import ObjectId
from pydantic import BaseModel, Field


class CategoryModel(BaseModel):
    # id: str
    title: Optional[str] = Field(...)
    childs: Optional[List] = None

    class Config:
        schema_extra = {
            "example": {
                "title": "Электроника",
            }
        }


class CategoryRelationModel(BaseModel):
    # id: str
    parent_category: Optional[CategoryModel]
    child_category: Optional[CategoryModel]

    class Config:
        schema_extra = {"example": {"title": "Параша"}}
