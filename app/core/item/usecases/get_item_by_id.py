from app.core.shared.usecase_base import UseCase

from app.core.item.dto.item import ItemId
from app.core.item.dao.item_read import ItemRead
from app.core.item.entities.item import Item


class GetItemByIdUseCase(UseCase[ItemId, Item]):
    def __init__(self, dao: ItemRead):
        self._dao = dao

    def execute(self, item_id: ItemId) -> Item:
        try:
            item = self._dao.get_by_id(item_id.id)
        except TypeError:
            raise TypeError
        return item
        