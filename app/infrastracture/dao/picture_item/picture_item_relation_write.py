from bson import ObjectId

from app.core.picture_item_relation.dao.picture_item_relation_write import (
    PictureItemRelationWrite,
)
from app.core.picture_item_relation.dto.picture_item_relation import PictureItemRelation
from app.core.picture_item_relation.entities.picture_item_relation import (
    PictureItemRelation,
)
from app.infrastracture.dao.base import BaseDao
from app.infrastracture.models.picture_item_relation import PictureItemRelationModel


class PictureItemRelationWriteImpl(BaseDao, PictureItemRelationWrite):
    def create(self, picture_item_relation: PictureItemRelation) -> PictureItemRelation:
        picture_item_relation_id = (
            self._database["picture_item_relation"]
            .insert_one(
                PictureItemRelationModel(
                    picture_id=picture_item_relation.picture_id,
                    item_id=picture_item_relation.item_id,
                ).dict(exclude_none=True)
            )
            .inserted_id
        )

        new_picture_item_relation = self._database["picture_item_relation"].find_one(
            {"_id": ObjectId(picture_item_relation_id)}
        )

        return PictureItemRelation(
            id=str(new_picture_item_relation["_id"]),
            picture_id=new_picture_item_relation["picture_id"],
            item_id=new_picture_item_relation["item_id"],
        )

    def delete(self, id: str) -> None:
        self._database["picture_item_relation"].delete_one({"_id": ObjectId(id)})

    def update(self, picture_item_relation: PictureItemRelation) -> PictureItemRelation:
        self._database["picture_item_relation"].find_one_and_update(
            {"_id": ObjectId(picture_item_relation.id)},
            {"$set": picture_item_relation.dict(exclude_none=True)},
        )
        return self._database["picture_item_relation"].find_one(
            {"_id": ObjectId(picture_item_relation.id)}
        )
