from app.core.category.dao.category_write import CategoryWrite
from app.core.category.dto.category import CategoryId
from app.core.shared.usecase_base import UseCase


class DeleteCategoryUseCase(UseCase[CategoryId, None]):
    def __init__(
        self,
        category_write_dao: CategoryWrite,
    ):
        self._category_write_dao = category_write_dao

    def execute(self, category_id: CategoryId) -> None:
        self._category_write_dao.delete(category_id=category_id)
