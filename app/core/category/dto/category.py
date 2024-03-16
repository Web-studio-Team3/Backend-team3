from typing import Optional

from app.shared.dto_base import BaseDto


class CategoryId(BaseDto):
    id: str


class CategoryCreate(BaseDto):
    title: str
    childs: list[str]


class CategoryUpdate(BaseDto):
    title: Optional[str]
    childs: Optional[list[str]]


class CategoryUpdateWithId(BaseDto):
    id: str
    category_update: CategoryUpdate
