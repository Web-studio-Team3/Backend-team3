from app.core.shared.usecase_base import UseCase
from app.core.user.dao.user_read import UserRead
from app.core.user.dto.user import UserGetByEmailReq, UserGetByEmailResp


class GetUserByEmailUseCase(UseCase[UserGetByEmailReq, UserGetByEmailResp]):
    def __init__(self, dao: UserRead):
        self._dao = dao

    def execute(self, user_email: UserGetByEmailReq) -> UserGetByEmailResp:
        return self._dao.get_by_email(user_email.email)
