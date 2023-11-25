from typing import Protocol

from app.core.sold_item.entities.sold_item_relation import SoldItemRelation


class SoldItemRelationRead(Protocol):
    def get_sold_item_relation_by_id(self, id: str) -> SoldItemRelation:
        raise NotImplementedError

    def get_sold_item_relation_by_seller_id(
        self, seller_id: str
    ) -> list[SoldItemRelation]:
        raise NotImplementedError

    def get_sold_item_relation_by_buyer_id(
        self, buyer_id: str
    ) -> list[SoldItemRelation]:
        raise NotImplementedError

    def get_sold_item_relation_by_item_id(self, item_id: str) -> SoldItemRelation:
        raise NotImplementedError
