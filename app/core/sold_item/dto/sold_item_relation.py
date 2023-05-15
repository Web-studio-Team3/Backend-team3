from app.shared.dto_base import BaseDto


class SoldItemRelation(BaseDto):
    seller_id: str
    buyer_id: str
    item_id: str


class SoldItemRelationId(BaseDto):
    id: str


class SoldItemRelationSellerId(BaseDto):
    seller_id: str


class SoldItemRelationBuyerId(BaseDto):
    buyer_id: str


class SoldItemRelationItemId(BaseDto):
    item_id: str
