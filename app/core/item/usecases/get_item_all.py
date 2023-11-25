from app.core.item.dao.item_read import ItemRead
from app.core.item.dto.item import ItemId
from app.core.item.entities.item import Item
from app.core.shared.usecase_base import UseCase


class GetItemAllUseCase(UseCase[ItemId, list[Item]]):
    def __init__(self, dao: ItemRead):
        self._dao = dao

    def execute(self) -> list[Item]:
        try:
            items = self._dao.get_all()
        except TypeError:
            raise TypeError
        return items
