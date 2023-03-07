from core.shared.usecase.usecase import UseCase
from core.user import dto

from core.user.protocols.auth_service import AuthService


class RegisterUserUseCase(UseCase):
    def __init__(self, auth_service: AuthService):
        self._auth_service = auth_service

    async def execute(self, user: dto.UserRegister):
        await self._auth_service.register(user)
