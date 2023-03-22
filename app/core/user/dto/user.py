from app.shared.dto_base import BaseDto


class UserSignUpRaw(BaseDto):
    email: str
    raw_password: str
    full_name: str
    date_of_birth: str

    class Config:
        schema_extra = {
            "example": {
                "email": "user@gmail.com",
                "raw_password": "12345",
                "full_name": "Jane Doe",
                "date_of_birth": "01-01-2000"
            }
        }


class UserSignUpHash(BaseDto):
    email: str
    hashed_password: str
    full_name: str
    date_of_birth: str


class UserId(BaseDto):
    id: str


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
    full_name: str
    date_of_birth: str
