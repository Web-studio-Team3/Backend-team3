from dataclasses import dataclass


@dataclass
class CartItem:
    id: str
    user_id: str
    item_id: str
