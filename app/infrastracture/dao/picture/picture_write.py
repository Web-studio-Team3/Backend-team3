from bson import ObjectId

from app.core.picture.dao.picture_write import PictureWrite
from app.core.picture.entities.picture import Picture
from app.infrastracture.dao.base import BaseDao
from app.infrastracture.models.picture import PictureModel


class PictureWriteImpl(BaseDao, PictureWrite):
    def create(self, picture_url: str) -> Picture:
        picture_id = (
            self._database["picture"]
            .insert_one({"picture_url": picture_url})
            .inserted_id
        )

        return Picture(id=str(picture_id), picture_url=picture_url)

    def delete(self, id: str) -> None:
        self._database["picture"].delete_one({"_id": ObjectId(id)})
