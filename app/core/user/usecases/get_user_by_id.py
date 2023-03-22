from app.core.shared.usecase_base import UseCase
from app.core.user.dto.user import UserId
from app.core.user.dao.user_read import UserRead
from app.core.user.entities.user import User


class GetUserByIdUseCase(UseCase[UserId, User]):
    def __init__(self, dao: UserRead):
        self._dao = dao

    def execute(self, user_id: UserId) -> User:
        try:
            user = self._dao.get_by_id(user_id.id)
        except TypeError:
            raise TypeError
        return user
