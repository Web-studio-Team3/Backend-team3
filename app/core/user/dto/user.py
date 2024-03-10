from typing import Optional

from app.shared.dto_base import BaseDto


class UserSignUpRaw(BaseDto):
    email: str
    raw_password: str
    full_name: str
    date_of_birth: str
    picture_id: str

    class Config:
        schema_extra = {
            "example": {
                "email": "user@gmail.com",
                "raw_password": "12345",
                "full_name": "Jane Doe",
                "date_of_birth": "01-01-2000",
                "picture_id": "642aab64757e9f5d986662c1",
            }
        }


class UserSignUpHash(BaseDto):
    email: str
    hashed_password: str
    full_name: str
    date_of_birth: str
    picture_id: str


class UserId(BaseDto):
    id: str


class UserUpdate(BaseDto):
    email: Optional[str]
    password: Optional[str]
    full_name: Optional[str]
    date_of_birth: Optional[str]
    picture_id: Optional[str]


class UserUpdateWithId(BaseDto):
    id: str
    user_update: UserUpdate


class UserGetByEmailReq(BaseDto):
    email: str


class UserGetByEmailResp(BaseDto):
    user_id: str
    hashed_password: str


class UserSignIn(BaseDto):
    email: str
    raw_password: str


class UserInfo(BaseDto):
    id: str
    email: str
    hashed_password: str
    full_name: str
    date_of_birth: str
