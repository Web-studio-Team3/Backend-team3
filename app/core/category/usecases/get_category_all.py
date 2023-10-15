from app.core.shared.usecase_base import UseCase

from app.core.category.dto.category import CategoryId
from app.core.category.dao.category_read import CategoryRead
from app.core.category.entities.category import Category


class GetCategoryAllUseCase(UseCase[CategoryId, list[Category]]):
    def __init__(self, dao: CategoryRead):
        self._dao = dao

    def execute(self) -> list[Category]:
        try:
            categories = self._dao.get_all()
        except TypeError:
            raise TypeError
        return categories
        