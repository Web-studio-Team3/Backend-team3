from typing import Protocol

from app.core.token.dto.token import (
    AccessTokenDto,
    AccessTokenUpdateDto,
    AccessTokenUserIdDto,

    RefreshTokenDto,
    RefreshTokenUpdateDto,
    RefreshTokenUsernameDto,
)
from app.core.token.entities.token import AccessToken, RefreshToken


class AccessTokenWrite(Protocol):
    def create(self, token: AccessTokenDto) -> AccessToken:
        raise NotImplementedError

    def update(self, token: AccessTokenUpdateDto) -> AccessToken:
        raise NotImplementedError

    def delete_by_user_id(self, token: AccessTokenUserIdDto) -> None:
        raise NotImplementedError


class RefreshTokenWrite(Protocol):
    def create(self, token: RefreshTokenDto) -> RefreshToken:
        raise NotImplementedError

    def update(self, token: RefreshTokenUpdateDto) -> RefreshToken:
        raise NotImplementedError

    def delete_by_user_id(self, token: RefreshTokenUsernameDto) -> None:
        raise NotImplementedError
