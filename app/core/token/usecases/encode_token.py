from app.core.token.dao.token_coder import TokenCoder
from decouple import config
import jwt
import time

JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")


class EncodeToken(TokenCoder):
    def encode(self, user_id: str) -> str:
        return jwt.encode({
            "user_id": user_id,
            "expires": time.time() + 86400
        },
            JWT_SECRET,
            algorithm=JWT_ALGORITHM
        )
