from app.core.shared.usecase_base import UseCase

from app.core.item.dto.item import ItemCreate
from app.core.item.dao.item_write import ItemWrite


class CreateItemUseCase(UseCase[ItemCreate, None]):
    def __init__(self, dao: ItemWrite):
        self._dao = dao

    def execute(self, item: ItemCreate) -> None:
        try:
            item = ItemCreate(
                category_id=item.category_id,
                title=item.title,
                description=item.description,
                condition=item.condition,
                address=item.address,
                cost=item.cost,
                status=item.status
            )
        except TypeError:
            raise TypeError
        
        try:
            self._dao.create(item=item)
        except TypeError:
            raise TypeError