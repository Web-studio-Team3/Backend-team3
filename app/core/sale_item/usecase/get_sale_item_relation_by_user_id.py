from app.core.sale_item.dao.sale_item_relation_read import SaleItemRelationRead
from app.core.sale_item.dto.sale_item_relation import (
    SaleItemRelation,
    SaleItemRelationUserId,
)
from app.core.shared.usecase_base import UseCase


class GetSaleItemRelationByUserIdUseCase(
    UseCase[SaleItemRelationUserId, list[SaleItemRelation]]
):
    def __init__(self, read_dao=SaleItemRelationRead):
        self._read_dao = read_dao

    def execute(self, obj: SaleItemRelationUserId) -> list[SaleItemRelation]:
        return self._read_dao.get_sale_item_relation_by_user_id(user_id=obj.user_id)
