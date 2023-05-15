from app.shared.dto_base import BaseDto


class SaleItemRelation(BaseDto):
    user_id: str
    item_id: str


class SaleItemRelationId(BaseDto):
    id: str


class SaleItemRelationItemId(BaseDto):
    item_id: str


class SaleItemRelationUserId(BaseDto):
    user_id: str
