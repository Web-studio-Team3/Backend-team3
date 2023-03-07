from typing import Protocol
from core.user.entities.user_item_tracking_relation import UserItemTrackingRelation
from uuid import UUID


class TrackingRelationRead(Protocol):
    async def get_relations_by_user_id(self, user_id: UUID) -> list[UserItemTrackingRelation]:
        raise NotImplementedError

    async def get_relation_by_id(self, relation_id: UUID) -> UserItemTrackingRelation:
        raise NotImplementedError
