from app.core.shared.usecase_base import UseCase
from app.core.sale_item.dao.sale_item_relation_write import SaleItemRelationWrite
from app.core.sale_item.dto.sale_item_relation import SaleItemRelation, SaleItemRelationId


class CreateSaleItemRelationUseCase(UseCase[SaleItemRelation, SaleItemRelationId]):
    def __init__(self, write_dao: SaleItemRelationWrite):
        self._write_dao = write_dao

    def execute(self, obj: SaleItemRelation) -> SaleItemRelationId:
        return self._write_dao.create(sale_item_relation=obj)
