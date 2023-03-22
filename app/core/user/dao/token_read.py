from typing import Protocol
from app.core.user.entities.token import AccessToken


class TokenRead(Protocol):
    def get_by_user_id(self, user_id: str) -> AccessToken:
        raise NotImplementedError

    def get_by_token(self, token: str) -> AccessToken:
        raise NotImplementedError
