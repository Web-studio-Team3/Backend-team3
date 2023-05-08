from app.core.shared.usecase_base import UseCase
from app.core.sold_item.dao.sold_item_relation_write import SoldItemRelationWrite
from app.core.sold_item.dto.sold_item_relation import SoldItemRelationId


class DeleteSoldItemRelationUseCase(UseCase[SoldItemRelationId, None]):
    def __init__(self, write_dao: SoldItemRelationWrite):
        self._write_dao = write_dao

    def execute(self, obj: SoldItemRelationId) -> None:
        self._write_dao.delete(sold_item_relation_id=obj.id)
