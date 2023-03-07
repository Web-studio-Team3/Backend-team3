from typing import Protocol


class HasherPassword(Protocol):

    def hash(self, password: str) -> str:
        raise NotImplementedError

    def verify_password(self, raw_password: str, hashed_password: str) -> bool:
        raise NotImplementedError
