from app.core.shared.usecase_base import UseCase
from app.core.user.dto.user import UserSignIn
from app.core.user.entities.token import AccessToken
from app.core.user.dao.user_read import UserRead
from app.core.user.exceptions.user import AuthError
from app.core.user.dao.password_hasher import PasswordHasher
from app.core.user.dao.token_read import TokenRead
from app.core.user.dto.token import AccessTokenUserIdDto
from app.core.user.usecases.create_token import CreateTokenUseCase


class SignInUseCase(UseCase[UserSignIn, AccessToken]):
    def __init__(
            self,
            token_read_dao: TokenRead,
            create_token_use_case: CreateTokenUseCase,
            user_read_dao: UserRead,
            password_hasher: PasswordHasher
    ):
        self._token_read_dao = token_read_dao
        self._user_read_dao = user_read_dao
        self._create_token_use_case = create_token_use_case
        self._password_hasher = password_hasher

    def execute(self, user: UserSignIn) -> AccessToken:
        user_entity = self._user_read_dao.get_by_email(user.email)

        if not user_entity:
            raise AuthError("wrong email")
        if not self._password_hasher.check_password(user.raw_password, user_entity.hashed_password):
            raise AuthError("wrong password")

        try:
            access_token = self._token_read_dao.get_by_user_id(user_id=user_entity.user_id)
        except TypeError:
            return self._create_token_use_case.execute(AccessTokenUserIdDto(user_id=user_entity.user_id))

        return access_token
