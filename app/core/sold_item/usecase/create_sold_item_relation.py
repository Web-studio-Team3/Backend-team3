from app.core.shared.usecase_base import UseCase
from app.core.sold_item.dao.sold_item_relation_write import SoldItemRelationWrite
from app.core.sold_item.dto.sold_item_relation import (
    SoldItemRelation,
    SoldItemRelationId,
)


class CreateSoldItemRelationUseCase(UseCase[SoldItemRelation, SoldItemRelationId]):
    def __init__(self, write_dao: SoldItemRelationWrite):
        self._write_dao = write_dao

    def execute(self, obj: SoldItemRelation) -> SoldItemRelationId:
        return self._write_dao.create(sold_item_relation=obj)
