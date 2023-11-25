from typing import Protocol

from app.core.favourites.entities.favourite import Favourite


class FavouriteRead(Protocol):
    def get_favourite_by_id(self, id: str) -> Favourite:
        raise NotImplementedError

    def get_favourite_by_user_id(self, user_id: str) -> list[Favourite]:
        raise NotImplementedError

    def get_favourite_by_item_id(self, item_id: str) -> list[Favourite]:
        raise NotImplementedError
