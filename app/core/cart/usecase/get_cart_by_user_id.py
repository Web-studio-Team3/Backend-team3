from app.core.cart.dao.cart_read import CartRead
from app.core.cart.dto.cart import CartItem, CartUserId
from app.core.shared.usecase_base import UseCase


class GetCartByUserIdUseCase(UseCase[CartUserId, list[CartItem]]):
    def __init__(self, read_dao=CartRead):
        self._read_dao = read_dao

    def execute(self, obj: CartUserId) -> list[CartItem]:
        return self._read_dao.get_cart_by_user_id(user_id=obj.user_id)
