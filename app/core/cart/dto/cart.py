from app.shared.dto_base import BaseDto


class CartItem(BaseDto):
    user_id: str
    item_id: str


class CartId(BaseDto):
    id: str


class CartItemId(BaseDto):
    item_id: str


class CartUserId(BaseDto):
    user_id: str
