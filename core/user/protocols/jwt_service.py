from typing import Protocol


class JwtService(Protocol):

    def encode(self, payload: dict) -> str:
        pass

    def decode(self, token: str) -> dict:
        pass