from app.shared.dto_base import BaseDto
from typing import Optional


class ItemId(BaseDto):
    id: str


class ItemCreate(BaseDto):
    category_id: str
    title: str
    description: str
    condition: str
    address: str
    cost: str
    status: str

        
class ItemUpdate(BaseDto):
    category_id: Optional[str]
    title: Optional[str]
    description: Optional[str]
    condition: Optional[str]
    address: Optional[str]
    cost: Optional[str]
    status: Optional[str]


class ItemUpdateWithId(BaseDto):
    id: str
    item_update: ItemUpdate
    