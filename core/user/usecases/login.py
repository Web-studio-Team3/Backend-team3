from core.shared.usecase.usecase import UseCase
from core.user import dto
from uuid import UUID

from core.user.services import AuthService


class LoginUserUseCase(UseCase):
    def __init__(self, auth_service: AuthService):
        self._auth_service = auth_service

    async def execute(self, user: dto.UserLogin) -> UUID:
        return await self._auth_service.login(user)
