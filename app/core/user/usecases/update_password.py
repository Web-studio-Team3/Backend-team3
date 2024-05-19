from app.core.shared.usecase_base import UseCase
from app.core.user.dao.user_read import UserRead
from app.core.user.dao.user_write import UserWrite
from app.core.user.dto.user import UserUpdatePasswordWithId
from app.core.user.entities.user import User
from app.core.user.usecases.password_hasher import PasswordHasher


class UpdatePasswordUseCase(UseCase[UserUpdatePasswordWithId, None]):
    def __init__(
        self,
        user_write_dao: UserWrite,
        user_read_dao: UserRead,
        password_hasher: PasswordHasher,
    ):
        self._user_write_dao = user_write_dao
        self._user_read_dao = user_read_dao
        self._password_hasher = password_hasher

    def execute(self, updated_user: UserUpdatePasswordWithId) -> None:
        if updated_user.new_password:
            updated_user.new_password = self._password_hasher.hash(
                updated_user.new_password
            )
        self._user_write_dao.update_password(updated_user)
