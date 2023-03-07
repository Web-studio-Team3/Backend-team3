from core.user import dto
from core.user.protocols.dao.tracking_relation_write import TrackingRelationWrite
from core.shared.protocols import Committer
from core.shared.usecase.usecase import UseCase
from core.user import entities
from sqlalchemy.exc import IntegrityError


class AddSoldRelationUseCase(UseCase[dto.UserItemTrackingRelation, None]):
    def __init__(
            self,
            dao: TrackingRelationWrite,
            committer: Committer
    ):
        self._dao = dao
        self._committer = committer

    async def execute(self, tracking_relation_dto: dto.UserItemTrackingRelation) -> None:
        added_relation = entities.UserItemTrackingRelation(
            user_id=tracking_relation_dto.user_id,
            item_id=tracking_relation_dto.item_id
        )

        await self._dao.create(relation=added_relation)

        try:
            await self._committer.commit()
        except IntegrityError:
            await self._committer.rollback()
            raise ValueError("Item not found or already tracked")
