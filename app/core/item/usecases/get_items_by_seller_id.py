from app.core.item.dao.item_read import ItemRead
from app.core.item.entities.item import Item
from app.core.shared.usecase_base import UseCase


class GetAllItemsBySellerIdUseCase(UseCase[str, list[Item]]):
    def __init__(self, dao: ItemRead):
        self._dao = dao

    def execute(self, seller_id: str) -> list[Item]:
        try:
            items = self._dao.get_all_by_id(seller_id)
        except TypeError:
            raise TypeError
        return items
