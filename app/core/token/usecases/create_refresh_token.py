from app.core.shared.usecase_base import UseCase
from app.core.token.dao.token_coder import RefreshTokenCoder
from app.core.token.dao.token_write import RefreshTokenWrite
from app.core.token.dto.token import  RefreshTokenDto, RefreshTokenUsernameDto
from app.core.token.entities.token import RefreshToken


class CreateRefreshTokenUseCase(UseCase[RefreshTokenUsernameDto, RefreshToken]):
    def __init__(self, dao: RefreshTokenWrite, token_coder: RefreshTokenCoder):
        self._dao = dao
        self._token_coder = token_coder

    def execute(self, refresh_token_username_dto: RefreshTokenUsernameDto) -> RefreshToken:
        token = self._token_coder.encode_refresh(refresh_token_username_dto.telegram_username)

        return self._dao.create(
            RefreshTokenDto(user_id=refresh_token_username_dto.telegram_username, token=token)
        )
