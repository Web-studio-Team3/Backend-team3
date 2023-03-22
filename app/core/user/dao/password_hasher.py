from typing import Protocol


class PasswordHasher(Protocol):
    def hash(self, raw_password: str) -> str:
        raise NotImplementedError

    def check_password(self, raw_password: str, hashed_password: str) -> bool:
        raise NotImplementedError
