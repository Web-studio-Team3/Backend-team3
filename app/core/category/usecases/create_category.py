from app.core.shared.usecase_base import UseCase

from app.core.category.dto.category import CategoryCreate
from app.core.category.dao.category_write import CategoryWrite


class CreateCategoryUseCase(UseCase[CategoryCreate, None]):
    def __init__(self, dao: CategoryWrite):
        self._dao = dao

    def execute(self, category: CategoryCreate) -> None:
        try:
            category = CategoryCreate(
                title=category.title,
                childs=category.childs,
            )
        except TypeError:
            raise TypeError
            
        try:
            self._dao.create(category=category)
        except TypeError:
            raise TypeError