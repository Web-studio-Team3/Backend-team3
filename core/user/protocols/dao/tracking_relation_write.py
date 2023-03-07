from typing import Protocol
from core.user import entities
from uuid import UUID


class TrackingRelationWrite(Protocol):
    async def create(self, relation: entities.UserItemTrackingRelation) -> None:
        raise NotImplementedError

    async def delete(self, relation_id: UUID) -> None:
        raise NotImplementedError
