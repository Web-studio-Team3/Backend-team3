from bson.objectid import ObjectId
from pydantic import BaseModel

from app.core.category.entities.category import Category


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, ObjectId):
            raise TypeError("ObjectId required")
        return str(v)


class CategoryModel(BaseModel):
    title: str
    childs: list[ObjectId]

    class Config:
        arbitrary_types_allowed = True


def from_entity(category: Category) -> CategoryModel:
    return CategoryModel(
        title=category.title,
        childs=category.childs,
    )
