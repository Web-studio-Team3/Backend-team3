from typing import Protocol

from app.core.item.entities.item import Item
# from app.core.item.dto.item import UserGetByEmailResp


class ItemRead(Protocol):
    def get_by_id(self, id: str) -> Item:
        raise NotImplementedError

    def get_all(self) -> list[Item]:
        raise NotImplementedError

    def get_all_by_id(self, id: str) -> list[Item]:
        raise NotImplementedError
