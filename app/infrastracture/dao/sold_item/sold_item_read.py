from bson import ObjectId
from app.core.sold_item.entities.sold_item_relation import SoldItemRelation

from app.infrastracture.dao.base import BaseDao

from app.core.sold_item.dao.sold_item_relation_read import SoldItemRelationRead


class SoldItemRelationReadImpl(
    BaseDao, SoldItemRelationRead
):
    def get_sold_item_relation_by_id(self, id: str) -> SoldItemRelation:
        relation = self._database["sold_item_relation"].find_one(
            {"_id": ObjectId(id)}
        )
        if not relation:
            raise TypeError

        return create_sold_item_relation(relation)
    
    def get_sold_item_relation_by_buyer_id(self, buyer_id: str) -> list[SoldItemRelation]:
        relations = self._database['sold_item_relation'].find(
            {'buyer_id': buyer_id}
        )
        if not relations:
            raise TypeError
        return list(map(create_sold_item_relation, relations))
    
    def get_sold_item_relation_by_item_id(self, item_id: str) -> SoldItemRelation:
        relation = self._database["sold_item_relation"].find_one(
            {"item_id": item_id}
        )
        if not relation:
            raise TypeError
        return create_sold_item_relation(relation)
    
    def get_sold_item_relation_by_seller_id(self, seller_id: str) -> list[SoldItemRelation]:
        relations = self._database['sold_item_relation'].find(
            {'seller_id': seller_id}
        )
        if not relations:
            raise TypeError
        return list(map(create_sold_item_relation, relations))


def create_sold_item_relation(sir_db_object):
    return SoldItemRelation(
        id=str(sir_db_object["_id"]),
        seller_id=sir_db_object["seller_id"],
        buyer_id=sir_db_object["buyer_id"],
        item_id=sir_db_object["item_id"]
    )
