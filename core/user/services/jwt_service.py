from core.user.protocols.jwt_service import JwtService
import jwt
from settings import Settings


class JwtServiceImp(JwtService):
    settings = Settings()

    def encode(self, payload: dict) -> str:
        pass

    def decode(self, token: str) -> dict:
        pass
