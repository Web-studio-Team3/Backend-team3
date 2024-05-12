from app.core.shared.usecase_base import UseCase
from app.core.token.dao.token_read import TokenRead
from app.core.token.dto.token import AccessTokenUserIdDto
from app.core.token.entities.token import AccessToken
from app.core.token.usecases.create_token import CreateTokenUseCase
from app.core.user.dao.password_hasher import PasswordHasher
from app.core.user.dao.user_read import UserRead
from app.core.user.dto.user import UserSignIn
from app.core.user.exceptions.user import AuthError


class SignInUseCase(UseCase[UserSignIn, AccessToken]):
    def __init__(
        self,
        token_read_dao: TokenRead,
        create_token_use_case: CreateTokenUseCase,
        user_read_dao: UserRead,
        password_hasher: PasswordHasher,
    ):
        self._token_read_dao = token_read_dao
        self._user_read_dao = user_read_dao
        self._create_token_use_case = create_token_use_case
        self._password_hasher = password_hasher

    def execute(self, user: UserSignIn) -> AccessToken:
        try:
            user_entity = self._user_read_dao.get_by_email(user.email)
        except():
            raise AuthError("wrong email")

        if not self._password_hasher.check_password(
            user.raw_password, user_entity.hashed_password
        ):
            raise AuthError("wrong password")

        try:
            access_token = self._token_read_dao.get_by_user_id(
                user_id=user_entity.user_id
            )
        except TypeError:
            return self._create_token_use_case.execute(
                AccessTokenUserIdDto(user_id=user_entity.user_id)
            )

        return access_token
