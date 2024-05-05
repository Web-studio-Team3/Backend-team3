from app.core.cart.dao.cart_write import CartWrite
from app.core.cart.dto.cart import CartId
from app.core.shared.usecase_base import UseCase


class DeleteCartItemUseCase(UseCase[CartId, None]):
    def __init__(self, write_dao: CartWrite):
        self._write_dao = write_dao

    def execute(self, obj: CartId) -> None:
        self._write_dao.delete(cart_id=obj.id)
