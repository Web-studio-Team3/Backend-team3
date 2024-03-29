from typing import Optional

from app.core.item.dao.item_write import ItemWrite
from app.core.item.dto.item import ItemCreate, ItemId
from app.core.shared.usecase_base import UseCase


class CreateItemUseCase(UseCase[ItemCreate, ItemId]):
    def __init__(self, dao: ItemWrite):
        self._dao = dao

    def execute(self, item: ItemCreate) -> ItemId:
        try:
            print("начало")
            item = ItemCreate(
                category_id=item.category_id,
                title=item.title,
                description=item.description,
                condition=item.condition,
                address=item.address,
                cost=item.cost,
                status=item.status,
                buyer_id=item.buyer_id,
                seller_id=item.seller_id,
            )
            print("конец")
        except TypeError:
            raise TypeError

        try:
            print("create item use case")
            return self._dao.create(item=item)
        except TypeError:
            raise TypeError
