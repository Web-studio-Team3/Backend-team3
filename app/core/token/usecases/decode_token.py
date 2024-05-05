import time

import jwt
from envparse import Env

from app.core.token.dao.token_coder import TokenCoder

env = Env()
JWT_SECRET = env.str("SECRET", default="please_please_update_me_please")
JWT_ALGORITHM = env.str("ALGORITHM", default="HS256")


class DecodeToken(TokenCoder):
    def decode(self, token: str) -> dict:
        print(time.time())
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=JWT_ALGORITHM)
        print(decoded_token["expires"])
        return decoded_token if decoded_token["expires"] <= time.time() else "The token's lifetime has expired"
