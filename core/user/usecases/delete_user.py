from core.user.protocols.dao.user_write import UserWriteDao
from core.shared.usecase.usecase import UseCase
from core.shared.protocols import Committer
from sqlalchemy.exc import IntegrityError
from core.user import dto


class DeleteUserUseCase(UseCase[dto.DeleteUser, None]):
    def __init__(
            self,
            dao: UserWriteDao,
            committer: Committer
    ):
        self._dao = dao
        self._committer = committer

    async def execute(self, user_dto: dto.DeleteUser) -> None:
        await self._dao.delete(user_id=user_dto.user_id)

        try:
            await self._committer.commit()
        except IntegrityError:
            await self._committer.rollback()
            raise ValueError("User not found")
