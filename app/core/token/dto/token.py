from app.shared.dto_base import BaseDto
from pydantic import BaseModel
from fastapi_jwt_auth import AuthJWT


# REFRESH - TOKEN
class RefreshTokenDto(BaseDto):
    telegram_username: str
    token: str


class RefreshTokenUsernameDto(BaseDto):
    telegram_username: str


class RefreshTokenDeleteDto(BaseDto):
    id: str


class RefreshTokenUpdateDto(BaseDto):
    id: str
    telegram_username: str
    token: str


# ACCESS - TOKEN
class AccessTokenDto(BaseDto):
    user_id: str
    token: str


class AccessTokenUserIdDto(BaseDto):
    user_id: str


class AccessTokenDeleteDto(BaseDto):
    id: str


class AccessTokenUpdateDto(BaseDto):
    id: str
    user_id: str
    token: str


# SETTINGS
class Settings(BaseModel):
    authjwt_secret_key: str = "secret"


@AuthJWT.load_config
def get_config():
    return Settings()