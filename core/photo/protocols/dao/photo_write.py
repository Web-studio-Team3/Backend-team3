from typing import Protocol
from core.photo.entities import Photo
from uuid import UUID


class PhotoWrite(Protocol):
    async def create(self, photo: Photo) -> None:
        raise NotImplementedError

    async def delete(self, photo_id: UUID) -> None:
        raise NotImplementedError
