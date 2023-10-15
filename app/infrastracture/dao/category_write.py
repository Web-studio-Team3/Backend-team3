from bson import ObjectId

from app.core.category.dao.category_write import CategoryWrite
from app.core.category.dto.category import CategoryCreate, CategoryId, CategoryUpdateWithId

from app.infrastracture.models.category import CategoryModel
from app.infrastracture.dao.base import BaseDao

class CategoryWriteDaoImpl(
    BaseDao, CategoryWrite
):
    def create(self, category: CategoryCreate) -> None:
        category = CategoryModel(
                title=category.title,
                childs=list(map(ObjectId, category.childs))
            ).dict(exclude_none=True)
        print(category)
        self._database["categories"].insert_one(
            category
        )

    def delete(self, category_id: CategoryId) -> None:
        self._database["categories"].find_one_and_delete({"_id": ObjectId(category_id.id)})

    def update(self, category: CategoryUpdateWithId) -> None:
        self._database["categories"].find_one_and_update(
            {"_id": ObjectId(category.id)}, {"$set": category.category_update.dict(exclude_none=True)}
        )