from app.core.item.dao.item_write import ItemWrite
from app.core.item.dto.item import ItemId
from app.core.shared.usecase_base import UseCase


class DeleteItemUseCase(UseCase[ItemId, None]):
    def __init__(
        self,
        item_write_dao: ItemWrite,
    ):
        self._item_write_dao = item_write_dao

    def execute(self, item_id: ItemId) -> None:
        self._item_write_dao.delete(item_id=item_id)
