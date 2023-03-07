from core.user.protocols.dao.tracking_realation_read import TrackingRelationRead
from core.shared.usecase.usecase import UseCase
from core.user import entities
from core.user import dto
from core.shared.protocols import Committer
from sqlalchemy.exc import IntegrityError


class GetSoldRelationUseCase(UseCase[dto.UserItemTrackingRelationId, entities.UserItemTrackingRelation]):
    def __init__(
            self,
            dao: TrackingRelationRead,
            committer: Committer
    ):
        self._dao = dao
        self._committer = committer

    async def execute(self, relation_dto: dto.UserItemTrackingRelationId) -> entities.UserItemTrackingRelation:
        sold_item = await self._dao.get_relation_by_id(relation_id=relation_dto.relation_id)

        try:
            await self._committer.commit()
        except IntegrityError:
            await self._committer.rollback()
            raise ValueError("Relation not found")

        return sold_item
