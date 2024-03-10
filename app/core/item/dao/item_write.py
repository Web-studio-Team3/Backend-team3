from typing import Protocol

from app.core.item.dto.item import ItemCreate, ItemId, ItemUpdateWithId


class ItemWrite(Protocol):
    def create(self, item: ItemCreate) -> ItemId:
        raise NotImplementedError

    def delete(self, item_id: ItemId) -> None:
        raise NotImplementedError

    def update(self, item: ItemUpdateWithId) -> None:
        raise NotImplementedError
