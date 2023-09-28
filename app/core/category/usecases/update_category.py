from app.core.shared.usecase_base import UseCase

from app.core.category.dto.category import CategoryUpdateWithId
from app.core.category.entities.category import Category
from app.core.category.dao.category_write import CategoryWrite
from app.core.category.dao.category_read import CategoryRead


class UpdateCategoryUseCase(UseCase[CategoryUpdateWithId, Category]):
    def __init__(
        self,
        category_write_dao: CategoryWrite,
        category_read_dao: CategoryRead
    ):
        self._category_write_dao = category_write_dao
        self._category_read_dao = category_read_dao

    def execute(self, updated_category: CategoryUpdateWithId) -> Category:
        self._category_write_dao.update(updated_category)
        return self._category_read_dao.get_by_id(updated_category.id)
        