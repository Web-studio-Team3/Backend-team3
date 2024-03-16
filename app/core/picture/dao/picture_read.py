from typing import Protocol

from app.core.picture.entities.picture import Picture


class PictureRead(Protocol):
    def get_picture_by_id(self, id: str) -> Picture:
        raise NotImplementedError
