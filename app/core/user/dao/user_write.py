from typing import Protocol

from app.core.user.dto.user import UserId, UserSignUpHash, UserUpdateWithId, UserUpdatePasswordWithId


class UserWrite(Protocol):
    def create(self, user: UserSignUpHash) -> None:
        raise NotImplementedError

    def delete(self, user_id: UserId) -> None:
        raise NotImplementedError

    def update(self, user: UserUpdateWithId) -> None:
        raise NotImplementedError
    
    def update_password(self, user: UserUpdatePasswordWithId) -> None:
        raise NotImplementedError
