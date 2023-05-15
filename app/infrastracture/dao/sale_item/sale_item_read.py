from bson import ObjectId

from app.infrastracture.dao.base import BaseDao

from app.core.sale_item.entities.sale_item_relation import SaleItemRelation
from app.core.sale_item.dao.sale_item_relation_read import SaleItemRelationRead


class SaleItemRelationReadImpl(
    BaseDao, SaleItemRelationRead
):
    def get_sale_item_relation_by_id(self, id: str) -> SaleItemRelation:
        relation = self._database["sale_item_relation"].find_one(
            {"_id": ObjectId(id)}
        )
        if not relation:
            raise TypeError

        return create_sale_item_relation(relation)

    def get_sale_item_relation_by_item_id(self, item_id: str) -> SaleItemRelation:
        relation = self._database["sale_item_relation"].find_one(
            {"item_id": item_id}
        )
        if not relation:
            raise TypeError

        return create_sale_item_relation(relation)

    def get_sale_item_relation_by_user_id(self, user_id: str) -> list[SaleItemRelation]:
        relations = self._database["sale_item_relation"].find(
            {"user_id": user_id}
        )

        return list(map(create_sale_item_relation, relations))


def create_sale_item_relation(sir_db_object):
    return SaleItemRelation(
        id=str(sir_db_object["_id"]),
        user_id=sir_db_object["user_id"],
        item_id=sir_db_object["item_id"]
    )
