from bson import ObjectId

from app.core.favourites.dao.favourite_write import FavouriteWrite
from app.core.favourites.dto.favourite import Favourite, FavouriteId
from app.infrastracture.dao.base import BaseDao
from app.infrastracture.models.favourite import FavouriteModel


class FavouriteWriteImpl(BaseDao, FavouriteWrite):
    def create(self, favourite: Favourite) -> FavouriteId:
        inserted_id = (
            self._database["favourite"]
            .insert_one(
                FavouriteModel(
                    user_id=favourite.user_id, item_id=favourite.item_id
                ).dict(exclude_none=True)
            )
            .inserted_id
        )
        return FavouriteId(id=str(inserted_id))

    def delete(self, favourite_id: str) -> None:
        self._database["favourite"].delete_one({"_id": ObjectId(favourite_id)})
