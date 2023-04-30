from app.core.shared.usecase_base import UseCase

from app.core.item.dto.item import ItemCreate
from app.core.item.dao.item_write import ItemWrite
from app.core.item.dto.item import ItemId


class CreateItemUseCase(UseCase[ItemCreate, ItemId]):
    def __init__(self, dao: ItemWrite):
        self._dao = dao

    def execute(self, item: ItemCreate) -> ItemId:
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
            print("create item use case")
            return self._dao.create(item=item)
        except TypeError:
            raise TypeError