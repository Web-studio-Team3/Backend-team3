from bson import ObjectId

from app.core.cart.dao.cart_write import CartWrite
from app.core.cart.dto.cart import CartItem, CartId
from app.infrastracture.dao.base import BaseDao
from app.infrastracture.models.cart import CartModel


class CartWriteImpl(BaseDao, CartWrite):
    def create(self, cart: CartItem) -> CartId:
        inserted_id = (
            self._database["cart"]
            .insert_one(
                CartModel(
                    user_id=cart.user_id, item_id=cart.item_id
                ).dict(exclude_none=True)
            )
            .inserted_id
        )
        return CartId(id=str(inserted_id))

    def delete(self, cart_id: str) -> None:
        self._database["cart"].delete_one({"_id": ObjectId(cart_id)})
