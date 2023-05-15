from bson import ObjectId

from app.core.picture_item_relation.entities.picture_item_relation import PictureItemRelation
from app.core.picture_item_relation.dao.picture_item_relation_read import PictureItemRelationRead

from app.infrastracture.dao.base import BaseDao


class PictureItemRelationReadImpl(
    BaseDao, PictureItemRelationRead
):
    def get_picture_item_relations(self) -> list[PictureItemRelation]:
        relations = self._database["picture_item_relation"].find()
        return list(map(create_picture_item_relation, relations))

    def get_picture_item_relation_by_id(self, id: str) -> PictureItemRelation:
        relation = self._database["picture_item_relation"].find_one(
            {"_id": ObjectId(id)}
        )
        if not relation:
            raise TypeError
        return create_picture_item_relation(relation)


def create_picture_item_relation(pir_db_object):
    return PictureItemRelation(
        id=str(pir_db_object["_id"]),
        picture_id=pir_db_object["picture_id"],
        item_id=pir_db_object["item_id"]
    )
