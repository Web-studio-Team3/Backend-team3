from pydantic import BaseModel


class AccessTokenModel(BaseModel):
    user_id: str
    jwt_token: str


class RefreshTokenModel(BaseModel):
    telegram_username: str
    jwt_token: str
