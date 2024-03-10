from app.core.shared.usecase_base import UseCase
from app.core.token.dao.token_read import TokenRead
from app.core.token.entities.token import AccessToken


class GetAccessTokenByJwtUseCase(UseCase[str, AccessToken]):
    def __init__(self, dao: TokenRead):
        self._dao = dao

    def execute(self, token: str) -> AccessToken:
        return self._dao.get_by_token(token=token)
