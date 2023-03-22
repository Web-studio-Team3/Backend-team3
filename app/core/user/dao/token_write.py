from typing import Protocol
from app.core.user.dto.token import (
    AccessTokenDto,
    AccessTokenDeleteDto,
    AccessTokenUpdateDto
)
from app.core.user.entities.token import AccessToken


class TokenWrite(Protocol):
    def create(self, token: AccessTokenDto) -> AccessToken:
        raise NotImplementedError

    def update(self, token: AccessTokenUpdateDto) -> AccessToken:
        raise NotImplementedError

    def delete(self, token: AccessTokenDeleteDto) -> None:
        raise NotImplementedError
