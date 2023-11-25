from fastapi import HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.core.token.usecases.decode_token import DecodeToken
from app.infrastracture.connect import database


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> str:
        credentials: HTTPAuthorizationCredentials = await super(
            JWTBearer, self
        ).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=403, detail="Invalid authentication scheme."
                )
            if not self.is_token_exist(credentials.credentials):
                raise HTTPException(status_code=403, detail="Token doesn't exist")
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(
                    status_code=403, detail="Invalid token or expired token."
                )
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    @staticmethod
    def is_token_exist(token: str) -> bool:
        access_token = database["token"].find_one({"jwt_token": token})
        if not access_token:
            return False
        else:
            return True

    @staticmethod
    def verify_jwt(jwt_token: str) -> bool:
        is_token_valid: bool = False
        payload = DecodeToken().decode(jwt_token)
        if payload:
            is_token_valid = True
        return is_token_valid
