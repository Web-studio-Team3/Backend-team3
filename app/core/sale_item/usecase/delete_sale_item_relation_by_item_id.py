from app.core.sale_item.dao.sale_item_relation_write import SaleItemRelationWrite
from app.core.sale_item.dto.sale_item_relation import SaleItemRelationItemId
from app.core.shared.usecase_base import UseCase


class DeleteSaleItemRelationByItemIdUseCase(UseCase[SaleItemRelationItemId, None]):
    def __init__(self, write_dao: SaleItemRelationWrite):
        self._write_dao = write_dao

    def execute(self, obj: SaleItemRelationItemId) -> None:
        self._write_dao.deleteByItemId(item_id=obj.item_id)
