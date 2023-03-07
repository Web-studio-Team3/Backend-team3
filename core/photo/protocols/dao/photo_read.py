from typing import Protocol
from core.photo.entities import Photo
from uuid import UUID


class PhotoRead(Protocol):
    async def get(self, photo_id: UUID) -> Photo:
        raise NotImplementedError
