from bson import ObjectId

from app.core.item.dao.item_write import ItemWrite
from app.core.item.dto.item import ItemCreate, ItemId, ItemUpdateWithId
from app.infrastracture.dao.base import BaseDao
from app.infrastracture.models.item import ItemModel, PyObjectId


class ItemWriteDaoImpl(BaseDao, ItemWrite):
    def create(self, item: ItemCreate) -> ItemId:
        print("create item write dao impl")
        print(item)
        item_id = (
            self._database["item"]
            .insert_one(
                ItemModel(
                    category_id=ObjectId(item.category_id),
                    title=item.title,
                    description=item.description,
                    condition=item.condition,
                    address=item.address,
                    cost=item.cost,
                    status=item.status,
                ).dict(exclude_none=True)
            )
            .inserted_id
        )
        print(item_id)
        return ItemId(id=str(item_id))

    def delete(self, item_id: ItemId) -> None:
        self._database["item"].find_one_and_delete({"_id": ObjectId(item_id.id)})

    def update(self, item: ItemUpdateWithId) -> None:
        self._database["item"].find_one_and_update(
            {"_id": ObjectId(item.id)},
            {"$set": item.item_update.dict(exclude_none=True)},
        )
