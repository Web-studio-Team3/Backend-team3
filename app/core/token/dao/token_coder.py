from typing import Protocol


class TokenCoder(Protocol):
    def encode(self, user_id: str) -> str:
        raise NotImplementedError

    def decode(self, token: str) -> dict:
        raise NotImplementedError
