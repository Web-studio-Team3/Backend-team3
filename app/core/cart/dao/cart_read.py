from typing import Protocol

from app.core.cart.entities.cart_item import CartItem


class CartRead(Protocol):
    def get_cart_by_user_id(self, user_id: str) -> list[CartItem]:
        raise NotImplementedError