from typing import Optional

from bson import ObjectId

from app.core.item.dao.item_read import ItemRead
from app.core.item.entities.item import Item
from app.core.user.dto.user import UserId
from app.infrastracture.dao.base import BaseDao


class ItemReadDaoImpl(BaseDao, ItemRead):
    def get_by_id(self, id: str) -> Item:
        item = self._database["item"].find_one({"_id": ObjectId(id)})
        if not item:
            raise TypeError

        if not("buyer_id" in item):
            return Item(
                id=str(item["_id"]),
                category_id=str(item["category_id"]),
                title=item["title"],
                description=item["description"],
                condition=item["condition"],
                address=item["address"],
                cost=item["cost"],
                status=item["status"],
                buyer_id=None,
                seller_id=str(item["seller_id"]),
            )
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
            if not ("buyer_id" in item):
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
                        buyer_id=None,
                        seller_id=str(item["seller_id"]),
                    )
                )
            else:
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

    def get_all_by_id(self, seller_id: str) -> list[Item]:
        items = self._database["item"].find({"seller_id": ObjectId(seller_id)})
        if not items:
            raise TypeError
        items_res = []
        for item in items:
            if not ("buyer_id" in item):
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
                        buyer_id=None,
                        seller_id=str(item["seller_id"]),
                    )
                )
            else:
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
