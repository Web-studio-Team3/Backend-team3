from typing import Protocol
from core.photo.entities import PhotoItemRelation
from uuid import UUID


class PhotoRelationWrite(Protocol):
    async def create(self, relation: PhotoItemRelation) -> None:
        raise NotImplementedError

    async def delete(self, relation_id: UUID) -> None:
        raise NotImplementedError
