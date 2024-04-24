from pydantic import BaseModel


class CartModel(BaseModel):
    user_id: str
    item_id: str
