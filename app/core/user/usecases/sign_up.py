from app.core.shared.usecase_base import UseCase

from app.core.user.dto.user import UserSignUpRaw, UserSignUpHash
from app.core.user.dao.user_write import UserWrite
from app.core.user.usecases.password_hasher import PasswordHasher
from app.core.user.exceptions.user import AuthError


class SignUpUseCase(UseCase[UserSignUpRaw, None]):
    def __init__(
            self,
            dao: UserWrite,
            password_hasher: PasswordHasher
    ):
        self._dao = dao
        self._password_hasher = password_hasher

    def execute(self, user: UserSignUpRaw) -> None:
        try:
            user = UserSignUpHash(
                email=user.email,
                hashed_password=self._password_hasher.hash(user.raw_password),
                full_name=user.full_name,
                date_of_birth=user.date_of_birth,
                picture_id=user.picture_id
            )
        except ValueError as e:
            raise AuthError(e)
        except TypeError as e:
            raise AuthError(e)

        try:
            self._dao.create(user=user)

        except IndexError:
            raise AuthError("User with this email already exists")
