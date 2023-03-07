from core.user import dto
from core.user.protocols.dao.sold_relation_write import SoldRelationWrite
from core.shared.protocols import Committer
from core.shared.usecase.usecase import UseCase
from core.user import entities
from sqlalchemy.exc import IntegrityError


class AddSoldRelationUseCase(UseCase[dto.UserItemSoldRelation, None]):
    def __init__(
            self,
            dao: SoldRelationWrite,
            committer: Committer
    ):
        self._dao = dao
        self._committer = committer

    async def execute(self, sold_relation_dto: dto.UserItemSoldRelation) -> None:
        added_relation = entities.UserItemSoldRelation(
            user_id=sold_relation_dto.user_id,
            item_id=sold_relation_dto.item_id
        )

        await self._dao.create(relation=added_relation)

        try:
            await self._committer.commit()
        except IntegrityError:
            await self._committer.rollback()
            raise ValueError("Item not found or already sold")
