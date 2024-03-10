from typing import Protocol

from app.core.sold_item.dto.sold_item_relation import (
    SoldItemRelation,
    SoldItemRelationId,
)


class SoldItemRelationWrite(Protocol):
    def create(self, sold_item_relation: SoldItemRelation) -> SoldItemRelationId:
        raise NotImplementedError

    def delete(self, sold_item_relation_id: str) -> None:
        raise NotImplementedError
