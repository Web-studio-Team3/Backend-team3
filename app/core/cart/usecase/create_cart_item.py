from app.core.cart.dao.cart_write import CartWrite
from app.core.cart.dto.cart import CartItem, CartId
from app.core.shared.usecase_base import UseCase


class CreateCartItemUseCase(UseCase[CartItem, CartId]):
    def __init__(self, write_dao: CartWrite):
        self._write_dao = write_dao

    def execute(self, obj: CartItem) -> CartId:
        return self._write_dao.create(cart=obj)
