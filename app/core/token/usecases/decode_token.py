from app.core.token.dao.token_coder import TokenCoder
from decouple import config
from envparse import Env
import jwt
import time

env = Env()
JWT_SECRET = env.str("SECRET", default="please_please_update_me_please")
JWT_ALGORITHM = env.str("ALGORITHM", default="HS256")


class DecodeToken(TokenCoder):
    def decode(self, token: str) -> dict:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=JWT_ALGORITHM)
        return decoded_token if decoded_token["expires"] >= time.time() else None
