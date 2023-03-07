from shared.dto import BaseDto
from uuid import UUID


class Photo(BaseDto):
    url: str


class PhotoGet(BaseDto):
    photo_id: UUID


class PhotoDelete(PhotoGet):
    pass
