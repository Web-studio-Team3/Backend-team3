from typing import Protocol
from app.core.sale_item.dto.sale_item_relation import SaleItemRelation, SaleItemRelationId


class SaleItemRelationWrite(Protocol):
    def create(self, sale_item_relation: SaleItemRelation) -> SaleItemRelationId:
        raise NotImplementedError

    def delete(self, sale_item_relation_id: str) -> None:
        raise NotImplementedError
    
    def deleteByItemId(self, item_id: str) -> None:
        raise NotImplementedError
