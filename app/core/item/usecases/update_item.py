from app.core.shared.usecase_base import UseCase

from app.core.item.dto.item import ItemUpdateWithId
from app.core.item.entities.item import Item
from app.core.item.dao.item_write import ItemWrite
from app.core.item.dao.item_read import ItemRead


class UpdateItemUseCase(UseCase[ItemUpdateWithId, Item]):
    def __init__(
        self,
        item_write_dao: ItemWrite,
        item_read_dao: ItemRead
    ):
        self._item_write_dao = item_write_dao
        self._item_read_dao = item_read_dao

    def execute(self, updated_item: ItemUpdateWithId) -> Item:
        self._item_write_dao.update(updated_item)
        return self._item_read_dao.get_by_id(updated_item.id)
        