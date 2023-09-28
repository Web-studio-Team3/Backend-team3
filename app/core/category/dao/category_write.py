from typing import Protocol
from app.core.category.dto.category import (
    CategoryId, CategoryCreate, CategoryUpdateWithId
)


class CategoryWrite(Protocol):
    def create(self, category: CategoryCreate) -> None:
        raise NotImplementedError

    def delete(self, category_id: CategoryId) -> None:
        raise NotImplementedError

    def update(self, category: CategoryUpdateWithId) -> None:
        raise NotImplementedError