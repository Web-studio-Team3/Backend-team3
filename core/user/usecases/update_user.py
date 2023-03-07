from core.user.protocols.dao.user_write import UserWriteDao
from core.shared.usecase.usecase import UseCase
from core.user import entities
from core.user import dto
from core.shared.protocols import Committer
from sqlalchemy.exc import IntegrityError


class UpdateUserUseCase(UseCase[dto.UpdateUser, None]):
    def __init__(
            self,
            dao: UserWriteDao,
            committer: Committer
    ):
        self._dao = dao
        self._committer = committer

    async def execute(self, user_dto: dto.UpdateUser) -> None:
        user = entities.User(
            email=user_dto.email,
            fullname=user_dto.full_name,
            date_of_birth=user_dto.date_of_birth,
            photo_id=user_dto.photo_id
        )
        user.id = user_dto.user_id

        await self._dao.update(user=user)

        try:
            await self._committer.commit()
        except IntegrityError:
            await self._committer.rollback()
            raise ValueError("User not found")
