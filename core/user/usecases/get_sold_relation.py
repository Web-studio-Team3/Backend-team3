from core.user.protocols.dao.sold_relation_read import SoldRelationRead
from core.shared.usecase.usecase import UseCase
from core.user import entities
from core.user import dto
from core.shared.protocols import Committer
from sqlalchemy.exc import IntegrityError


class GetSoldRelationUseCase(UseCase[dto.UserItemSoldRelationId, entities.UserItemSoldRelation]):
    def __init__(
            self,
            dao: SoldRelationRead,
            committer: Committer
    ):
        self._dao = dao
        self._committer = committer

    async def execute(self, relation_dto: dto.UserItemSoldRelationId) -> entities.UserItemSoldRelation:
        sold_item = await self._dao.get_relation_by_id(relation_id=relation_dto.relation_id)

        try:
            await self._committer.commit()
        except IntegrityError:
            await self._committer.rollback()
            raise ValueError("Relation not found")

        return sold_item
