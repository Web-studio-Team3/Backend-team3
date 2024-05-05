from typing import Protocol

from app.core.cart.dto.cart import CartItem, CartId


class CartWrite(Protocol):
    def create(self, cart: CartItem) -> CartId:
        raise NotImplementedError

    def delete(self, cart_id: str) -> None:
        raise NotImplementedError
