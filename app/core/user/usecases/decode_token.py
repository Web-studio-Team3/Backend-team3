from app.core.user.dao.token_coder import TokenCoder
from decouple import config
import jwt
import time

JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")


class DecodeToken(TokenCoder):
    def decode(self, token: str) -> dict:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=JWT_ALGORITHM)
        return decoded_token if decoded_token["expires"] >= time.time() else None
