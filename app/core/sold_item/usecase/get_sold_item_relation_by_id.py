from app.core.shared.usecase_base import UseCase
from app.core.sold_item.dao.sold_item_relation_read import SoldItemRelationRead
from app.core.sold_item.dto.sold_item_relation import (
    SoldItemRelation,
    SoldItemRelationId,
)


class GetSoldItemRelationByIdUseCase(UseCase[SoldItemRelationId, SoldItemRelation]):
    def __init__(self, read_dao=SoldItemRelationRead):
        self._read_dao = read_dao

    def execute(self, obj: SoldItemRelationId) -> SoldItemRelation:
        return self._read_dao.get_sold_item_relation_by_id(id=obj.id)
