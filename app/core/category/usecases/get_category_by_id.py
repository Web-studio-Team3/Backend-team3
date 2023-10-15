from app.core.shared.usecase_base import UseCase

from app.core.category.dto.category import CategoryId
from app.core.category.dao.category_read import CategoryRead
from app.core.category.entities.category import Category


class GetCategoryByIdUseCase(UseCase[CategoryId, Category]):
    def __init__(self, dao: CategoryRead):
        self._dao = dao

    def execute(self, category_id: CategoryId) -> Category:
        try:
            category = self._dao.get_by_id(category_id.id)
        except TypeError:
            raise TypeError
        return category
        