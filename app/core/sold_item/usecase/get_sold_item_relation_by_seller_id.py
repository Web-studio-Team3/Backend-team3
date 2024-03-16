from app.core.shared.usecase_base import UseCase
from app.core.sold_item.dao.sold_item_relation_read import SoldItemRelationRead
from app.core.sold_item.dto.sold_item_relation import SoldItemRelationSellerId
from app.core.sold_item.entities.sold_item_relation import SoldItemRelation


class GetSoldItemRelationBySellerIdUseCase(
    UseCase[SoldItemRelationSellerId, list[SoldItemRelation]]
):
    def __init__(self, read_dao=SoldItemRelationRead):
        self._read_dao = read_dao

    def execute(self, obj: SoldItemRelationSellerId) -> list[SoldItemRelation]:
        return self._read_dao.get_sold_item_relation_by_seller_id(
            seller_id=obj.seller_id
        )
