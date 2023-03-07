from typing import Protocol
from core.user import entities
from uuid import UUID


class SoldRelationWrite(Protocol):
    async def create(self, relation: entities.UserItemSoldRelation) -> None:
        raise NotImplementedError

    async def delete(self, relation_id: UUID) -> None:
        raise NotImplementedError
