from typing import Protocol
from app.core.category.entities.category import Category


class CategoryRead(Protocol):
    def get_by_id(self, id: str) -> Category:
        raise NotImplementedError

    def get_all(self) -> list[Category]:
        raise NotImplementedError