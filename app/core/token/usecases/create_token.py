from app.core.shared.usecase_base import UseCase
from app.core.token.dao.token_coder import TokenCoder
from app.core.token.dao.token_write import TokenWrite
from app.core.token.dto.token import AccessTokenDto, AccessTokenUserIdDto
from app.core.token.entities.token import AccessToken


class CreateTokenUseCase(UseCase[AccessTokenUserIdDto, AccessToken]):
    def __init__(self, dao: TokenWrite, token_coder: TokenCoder):
        self._dao = dao
        self._token_coder = token_coder

    def execute(self, access_token_user_id_dto: AccessTokenUserIdDto) -> AccessToken:
        token = self._token_coder.encode(access_token_user_id_dto.user_id)

        return self._dao.create(
            AccessTokenDto(user_id=access_token_user_id_dto.user_id, token=token)
        )
