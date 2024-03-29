from app.core.sale_item.dao.sale_item_relation_read import SaleItemRelationRead
from app.core.sale_item.dto.sale_item_relation import (
    SaleItemRelation,
    SaleItemRelationId,
)
from app.core.shared.usecase_base import UseCase


class GetSaleItemRelationByIdUseCase(UseCase[SaleItemRelationId, SaleItemRelation]):
    def __init__(self, read_dao=SaleItemRelationRead):
        self._read_dao = read_dao

    def execute(self, obj: SaleItemRelationId) -> SaleItemRelation:
        return self._read_dao.get_sale_item_relation_by_id(id=obj.id)
