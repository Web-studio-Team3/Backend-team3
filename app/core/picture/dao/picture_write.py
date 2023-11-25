from typing import Protocol

from app.core.picture.entities.picture import Picture


class PictureWrite(Protocol):
    def create(self, picture_url: str) -> Picture:
        raise NotImplementedError

    def delete(self, id: str) -> None:
        raise NotImplementedError
