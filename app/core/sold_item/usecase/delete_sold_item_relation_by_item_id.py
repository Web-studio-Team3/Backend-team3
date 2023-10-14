from app.core.shared.usecase_base import UseCase
from app.core.sold_item.dao.sold_item_relation_write import SoldItemRelationWrite
from app.core.sold_item.dao.sold_item_relation_read import SoldItemRelationRead
from app.core.sold_item.dto.sold_item_relation import SoldItemRelationItemId

class DeleteSoldItemRelationByItemIdUseCase(UseCase[SoldItemRelationItemId, None]):
    def __init__(
        self,
        write_dao: SoldItemRelationWrite,
        read_dao: SoldItemRelationRead    
    ):
        self._write_dao = write_dao
        self._read_dao = read_dao

    def execute(self, obj: SoldItemRelationItemId) -> None:
        try:
            sold_relation = self._read_dao.get_sold_item_relation_by_item_id(
                item_id=obj.item_id
            )
        except TypeError:
            return
        self._write_dao.delete(sold_item_relation_id=sold_relation.id)
