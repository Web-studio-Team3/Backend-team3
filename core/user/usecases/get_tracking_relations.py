from core.user.protocols.dao.tracking_realation_read import TrackingRelationRead
from core.shared.usecase.usecase import UseCase
from core.user import entities
from core.user import dto
from core.shared.protocols import Committer
from sqlalchemy.exc import IntegrityError


class GetSoldRelationsUseCase(UseCase[dto.GetUserItemTrackingRelations, list[entities.UserItemTrackingRelation]]):
    def __init__(
            self,
            dao: TrackingRelationRead,
            committer: Committer
    ):
        self._dao = dao
        self._committer = committer

    async def execute(self, relation_dto: dto.GetUserItemTrackingRelations) -> list[entities.UserItemTrackingRelation]:
        sold_items = await self._dao.get_relations_by_user_id(user_id=relation_dto.user_id)

        try:
            await self._committer.commit()
        except IntegrityError:
            await self._committer.rollback()
            raise ValueError("Relation not found")

        return sold_items
