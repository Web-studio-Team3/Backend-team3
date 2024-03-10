from app.core.sale_item.dao.sale_item_relation_read import SaleItemRelationRead
from app.core.sale_item.dto.sale_item_relation import (
    SaleItemRelation,
    SaleItemRelationItemId,
)
from app.core.shared.usecase_base import UseCase


class GetSaleItemRelationByItemIdUseCase(
    UseCase[SaleItemRelationItemId, SaleItemRelation]
):
    def __init__(self, read_dao=SaleItemRelationRead):
        self._read_dao = read_dao

    def execute(self, obj: SaleItemRelationItemId) -> SaleItemRelation:
        return self._read_dao.get_sale_item_relation_by_item_id(item_id=obj.item_id)
