from app.core.shared.usecase_base import UseCase
from app.core.token.dao.token_write import AccessTokenWrite
from app.core.token.dto.token import AccessTokenUserIdDto


class DeleteTokenByUserIdUseCase(UseCase[AccessTokenUserIdDto, None]):
    def __init__(self, token_write_dao: AccessTokenWrite):
        self._token_write_dao = token_write_dao

    def execute(self, access_token: AccessTokenUserIdDto) -> None:
        self._token_write_dao.delete_by_user_id(access_token)
