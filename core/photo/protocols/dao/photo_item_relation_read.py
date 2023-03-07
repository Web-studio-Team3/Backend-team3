from typing import Protocol
from core.photo.entities import PhotoItemRelation
from uuid import UUID


class PhotoRelationRead(Protocol):
    async def get_photo_relations_by_item_id(self, item_id: UUID) -> list[PhotoItemRelation]:
        raise NotImplementedError

    async def get_photo_relation_by_id(self, relation_id: UUID) -> PhotoItemRelation:
        raise NotImplementedError
