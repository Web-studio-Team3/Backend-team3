from bson import ObjectId

from app.infrastracture.dao.base import BaseDao
from app.infrastracture.models.sale_item_relation import SaleItemRelationModel

from app.core.sale_item.dao.sale_item_relation_write import SaleItemRelationWrite
from app.core.sale_item.dto.sale_item_relation import (
    SaleItemRelation,
    SaleItemRelationId
)


class SaleItemRelationWriteImpl(
    BaseDao, SaleItemRelationWrite
):
    def create(self, sale_item_relation: SaleItemRelation) -> SaleItemRelation:
        inserted_id = self._database["sale_item_relation"].insert_one(
            SaleItemRelationModel(
                user_id=sale_item_relation.user_id,
                item_id=sale_item_relation.item_id
            ).dict(exclude_none=True)
        ).inserted_id

        return SaleItemRelationId(id=str(inserted_id))


    def delete(self, sale_item_relation_id: str) -> None:
        self._database["sale_item_relation"].delete_one(
            {"_id": ObjectId(sale_item_relation_id)}
        )

    
    def deleteByItemId(self, item_id: str) -> None:
        self._database['sale_item_relation'].delete_one(
            {"item_id": item_id}
        )
