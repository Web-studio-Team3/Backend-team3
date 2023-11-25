from bson import ObjectId

from app.core.favourites.dao.favourite_read import FavouriteRead
from app.core.favourites.entities.favourite import Favourite
from app.infrastracture.dao.base import BaseDao


class FavouriteReadImpl(BaseDao, FavouriteRead):
    def get_favourite_by_id(self, id: str) -> Favourite:
        favourite = self._database["favourite"].find_one({"_id": ObjectId(id)})
        if not favourite:
            raise TypeError

        return create_favourite(favourite)

    def get_favourite_by_item_id(self, item_id: str) -> list[Favourite]:
        favourites = self._database["favourite"].find({"item_id": item_id})
        if not favourites:
            raise TypeError

        return list(map(create_favourite, favourites))

    def get_favourite_by_user_id(self, user_id: str) -> list[Favourite]:
        favourites = self._database["favourite"].find({"user_id": user_id})
        if not favourites:
            raise TypeError

        return list(map(create_favourite, favourites))


def create_favourite(favourite_db_object):
    return Favourite(
        id=str(favourite_db_object["_id"]),
        user_id=favourite_db_object["user_id"],
        item_id=favourite_db_object["item_id"],
    )
