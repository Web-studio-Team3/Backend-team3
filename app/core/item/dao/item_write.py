from typing import Protocol
from app.core.item.dto.item import (
    ItemId, ItemCreate, ItemUpdateWithId
)


class ItemWrite(Protocol):
    def create(self, item: ItemCreate) -> None:
        raise NotImplementedError

    def delete(self, item_id: ItemId) -> None:
        raise NotImplementedError

    def update(self, item: ItemUpdateWithId) -> None:
        raise NotImplementedError