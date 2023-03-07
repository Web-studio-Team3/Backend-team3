from core.user.protocols.dao.user_read import UserReadDao
from core.shared.usecase.usecase import UseCase
from core.user import entities
from core.user import dto
from core.shared.protocols import Committer
from sqlalchemy.exc import IntegrityError


class GetUserByIdUseCase(UseCase[dto.UserId, entities.User]):
    def __init__(
            self,
            dao: UserReadDao,
            committer: Committer
    ):
        self._dao = dao
        self._committer = committer

    async def execute(self, user_dto: dto.UserId) -> entities.User:
        user = await self._dao.get_by_id(user_id=user_dto.user_id)

        try:
            await self._committer.commit()
        except IntegrityError:
            await self._committer.rollback()
            raise ValueError("User not found")

        return user
