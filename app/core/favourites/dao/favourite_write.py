from typing import Protocol

from app.core.favourites.dto.favourite import Favourite, FavouriteId


class FavouriteWrite(Protocol):
    def create(self, favourite: Favourite) -> FavouriteId:
        raise NotImplementedError

    def delete(self, favourite_id: str) -> None:
        raise NotImplementedError
