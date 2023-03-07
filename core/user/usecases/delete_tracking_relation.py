from core.user import dto
from core.user.protocols.dao.tracking_relation_write import TrackingRelationWrite
from core.shared.protocols import Committer
from core.shared.usecase.usecase import UseCase
from sqlalchemy.exc import IntegrityError


class DeleteSoldRelation(UseCase[dto.UserItemTrackingRelationDelete, None]):
    def __init__(
            self,
            dao: TrackingRelationWrite,
            committer: Committer
    ):
        self._dao = dao
        self._committer = committer

    async def execute(self, tracking_relation_dto: dto.UserItemTrackingRelationDelete) -> None:
        await self._dao.delete(relation_id=tracking_relation_dto.relation_id)

        try:
            await self._committer.commit()
        except IntegrityError:
            await self._committer.rollback()
            raise ValueError("Relation not found or already deleted")
