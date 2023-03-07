from core.shared.usecase.usecase import UseCase
from core.user.services import AuthService
from core.user import dto


class LogoutUserUseCase(UseCase):
    def __init__(self, auth_service: AuthService):
        self._auth_service = auth_service

    async def execute(self, user: dto.UserLogout) -> None:
        await self._auth_service.logout(user)
