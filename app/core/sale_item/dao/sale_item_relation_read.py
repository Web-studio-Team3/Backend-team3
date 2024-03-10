from typing import Protocol

from app.core.sale_item.entities.sale_item_relation import SaleItemRelation


class SaleItemRelationRead(Protocol):
    def get_sale_item_relation_by_id(self, id: str) -> SaleItemRelation:
        raise NotImplementedError

    def get_sale_item_relation_by_user_id(self, user_id: str) -> list[SaleItemRelation]:
        raise NotImplementedError

    def get_sale_item_relation_by_item_id(self, item_id: str) -> SaleItemRelation:
        raise NotImplementedError
