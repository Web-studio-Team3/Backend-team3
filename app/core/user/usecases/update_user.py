from app.core.shared.usecase_base import UseCase

from app.core.user.dto.user import UserUpdateWithId
from app.core.user.entities.user import User
from app.core.user.dao.user_write import UserWrite
from app.core.user.dao.user_read import UserRead
from app.core.user.usecases.password_hasher import PasswordHasher


class UpdateUserUseCase(UseCase[UserUpdateWithId, User]):
    def __init__(
            self,
            user_write_dao: UserWrite,
            user_read_dao: UserRead,
            password_hasher: PasswordHasher
    ):
        self._user_write_dao = user_write_dao
        self._user_read_dao = user_read_dao
        self._password_hasher = password_hasher

    def execute(self, updated_user: UserUpdateWithId) -> User:
        if updated_user.user_update.password:
            updated_user.user_update.password = self._password_hasher.hash(updated_user.user_update.password)
        self._user_write_dao.update(updated_user)
        return self._user_read_dao.get_by_id(updated_user.id)
