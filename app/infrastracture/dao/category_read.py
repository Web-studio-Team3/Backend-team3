from bson import ObjectId

from app.core.category.dao.category_read import CategoryRead
from app.core.category.entities.category import Category
from app.infrastracture.dao.base import BaseDao


class CategoryReadDaoImpl(BaseDao, CategoryRead):
    def get_by_id(self, id: str) -> Category:
        category = self._database["categories"].find_one({"_id": ObjectId(id)})
        if not category:
            raise TypeError
        return Category(
            id=str(category["_id"]),
            title=category["title"],
            childs=list(map(str, category["childs"])),
        )

    def get_all(self) -> list[Category]:
        categories = self._database["categories"].find()
        if not categories:
            raise TypeError
        categories_res = []
        for category in categories:
            categories_res.append(
                Category(
                    id=str(category["_id"]),
                    title=category["title"],
                    childs=list(map(str, category["childs"])),
                )
            )
        return categories_res
