from typing import Optional

from bson import ObjectId

from app.core.item.dao.item_read import ItemRead
from app.core.item.entities.item import Item
from app.infrastracture.dao.base import BaseDao


class ItemReadDaoImpl(BaseDao, ItemRead):
    def get_by_id(self, id: str) -> Item:
        item = self._database["item"].find_one({"_id": ObjectId(id)})
        if not item:
            raise TypeError
        return Item(
            id=str(item["_id"]),
            category_id=str(item["category_id"]),
            title=item["title"],
            description=item["description"],
            condition=item["condition"],
            address=item["address"],
            cost=item["cost"],
            status=item["status"],
            buyer_id=str(item["buyer_id"]),
            seller_id=str(item["seller_id"]),
        )

    def get_all(self) -> list[Item]:
        items = self._database["item"].find()
        if not items:
            raise TypeError
        items_res = []
        for item in items:
            items_res.append(
                Item(
                    id=str(item["_id"]),
                    category_id=str(item["category_id"]),
                    title=item["title"],
                    description=item["description"],
                    condition=item["condition"],
                    address=item["address"],
                    cost=item["cost"],
                    status=item["status"],
                    buyer_id=str(item["buyer_id"]),
                    seller_id=str(item["seller_id"]),
                )
            )
        return items_res
