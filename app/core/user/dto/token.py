from app.shared.dto_base import BaseDto


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
