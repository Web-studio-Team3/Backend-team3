from app.core.shared.usecase_base import UseCase
from app.core.user.dao.token_write import TokenWrite
from app.core.user.dto.token import AccessTokenUserIdDto, AccessTokenDto
from app.core.user.entities.token import AccessToken
from app.core.user.dao.token_coder import TokenCoder


class CreateTokenUseCase(UseCase[AccessTokenUserIdDto, AccessToken]):
    def __init__(self, dao: TokenWrite, token_coder: TokenCoder):
        self._dao = dao
        self._token_coder = token_coder

    def execute(self, access_token_user_id_dto: AccessTokenUserIdDto) -> AccessToken:
        token = self._token_coder.encode(access_token_user_id_dto.user_id)

        return self._dao.create(AccessTokenDto(user_id=access_token_user_id_dto.user_id, token=token))
