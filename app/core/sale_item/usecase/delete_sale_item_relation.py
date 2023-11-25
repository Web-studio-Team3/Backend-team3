from app.core.sale_item.dao.sale_item_relation_write import SaleItemRelationWrite
from app.core.sale_item.dto.sale_item_relation import SaleItemRelationId
from app.core.shared.usecase_base import UseCase


class DeleteSaleItemRelationUseCase(UseCase[SaleItemRelationId, None]):
    def __init__(self, write_dao: SaleItemRelationWrite):
        self._write_dao = write_dao

    def execute(self, obj: SaleItemRelationId) -> None:
        self._write_dao.delete(sale_item_relation_id=obj.id)
