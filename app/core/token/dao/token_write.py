from typing import Protocol

from app.core.token.dto.token import (
    AccessTokenDto,
    AccessTokenUpdateDto,
    AccessTokenUserIdDto,
)
from app.core.token.entities.token import AccessToken


class TokenWrite(Protocol):
    def create(self, token: AccessTokenDto) -> AccessToken:
        raise NotImplementedError

    def update(self, token: AccessTokenUpdateDto) -> AccessToken:
        raise NotImplementedError

    def delete_by_user_id(self, token: AccessTokenUserIdDto) -> None:
        raise NotImplementedError
