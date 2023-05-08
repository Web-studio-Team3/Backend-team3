from app.core.shared.usecase_base import UseCase
from app.core.sold_item.dao.sold_item_relation_read import SoldItemRelationRead
from app.core.sold_item.dto.sold_item_relation import (
    SoldItemRelationBuyerId,
    SoldItemRelation
)


class GetSoldItemRelationByBuyerIdUseCase(UseCase[SoldItemRelationBuyerId, list[SoldItemRelation]]):
    def __init__(self, read_dao=SoldItemRelationRead):
        self._read_dao = read_dao

    def execute(self, obj: SoldItemRelationBuyerId) -> list[SoldItemRelation]:
        return self._read_dao.get_sold_item_relation_by_buyer_id(buyer_id=obj.buyer_id)
