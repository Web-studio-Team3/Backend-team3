from bson import ObjectId

from app.core.cart.dao.cart_read import CartRead
from app.core.cart.entities.cart_item import CartItem
from app.infrastracture.dao.base import BaseDao


class CartReadImpl(BaseDao, CartRead):
    def get_cart_by_user_id(self, user_id: str) -> list[CartItem]:
        cart = self._database["cart"].find({"user_id": user_id})
        if not cart:
            raise TypeError

        return list(map(create_cart, cart))


def create_cart(cart_db_object):
    return CartItem(
        id=str(cart_db_object["_id"]),
        user_id=cart_db_object["user_id"],
        item_id=cart_db_object["item_id"],
    )
