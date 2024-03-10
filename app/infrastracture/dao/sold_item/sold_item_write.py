from bson import ObjectId

from app.core.sold_item.dao.sold_item_relation_write import SoldItemRelationWrite
from app.core.sold_item.dto.sold_item_relation import (
    SoldItemRelation,
    SoldItemRelationId,
)
from app.infrastracture.dao.base import BaseDao
from app.infrastracture.models.sold_item_relation import SoldItemRelationModel


class SoldItemRelationWriteImpl(BaseDao, SoldItemRelationWrite):
    def create(self, sold_item_relation: SoldItemRelation) -> SoldItemRelationId:
        inserted_id = (
            self._database["sold_item_relation"]
            .insert_one(
                SoldItemRelationModel(
                    seller_id=sold_item_relation.seller_id,
                    buyer_id=sold_item_relation.buyer_id,
                    item_id=sold_item_relation.item_id,
                ).dict(exclude_none=True)
            )
            .inserted_id
        )
        return SoldItemRelationId(id=str(inserted_id))

    def delete(self, sold_item_relation_id: str) -> None:
        self._database["sold_item_relation"].delete_one(
            {"_id": ObjectId(sold_item_relation_id)}
        )
