from core.user import dto
from core.user.protocols.dao.sold_relation_write import SoldRelationWrite
from core.shared.protocols import Committer
from core.shared.usecase.usecase import UseCase
from sqlalchemy.exc import IntegrityError


class DeleteSoldRelation(UseCase[dto.UserItemSoldRelationDelete, None]):
    def __init__(
            self,
            dao: SoldRelationWrite,
            committer: Committer
    ):
        self._dao = dao
        self._committer = committer

    async def execute(self, sold_relation_dto: dto.UserItemSoldRelationDelete) -> None:
        await self._dao.delete(relation_id=sold_relation_dto.relation_id)

        try:
            await self._committer.commit()
        except IntegrityError:
            await self._committer.rollback()
            raise ValueError("Relation not found or already deleted")
