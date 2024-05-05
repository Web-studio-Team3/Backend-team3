from typing import Protocol


class TokenCoder(Protocol):
    def encode_access(self, user_id: str) -> str:
        raise NotImplementedError

    def encode_refresh(self, user_id: str) -> str:
        raise NotImplementedError

    def decode(self, token: str) -> dict:
        raise NotImplementedError


class RefreshTokenCoder(Protocol):
    def encode_access(self, telegram_username: str) -> str:
        raise NotImplementedError

    def encode_refresh(self, telegram_username: str) -> str:
        raise NotImplementedError

    def decode(self, token: str) -> dict:
        raise NotImplementedError
