from typing import Protocol
from core.user.entities.user_item_sold_relation import UserItemSoldRelation
from uuid import UUID


class SoldRelationRead(Protocol):
    async def get_relations_by_user_id(self, user_id: UUID) -> list[UserItemSoldRelation]:
        raise NotImplementedError

    async def get_relation_by_id(self, relation_id: UUID) -> UserItemSoldRelation:
        raise NotImplementedError
