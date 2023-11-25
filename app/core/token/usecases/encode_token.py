import time

import jwt
from decouple import config
from envparse import Env

from app.core.token.dao.token_coder import TokenCoder

env = Env()
JWT_SECRET = env.str("SECRET", default="please_please_update_me_please")
JWT_ALGORITHM = env.str("ALGORITHM", default="HS256")


class EncodeToken(TokenCoder):
    def encode(self, user_id: str) -> str:
        return jwt.encode(
            {"user_id": user_id, "expires": time.time() + 86400},
            JWT_SECRET,
            algorithm=JWT_ALGORITHM,
        )
