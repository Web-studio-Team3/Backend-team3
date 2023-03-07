from shared.dto import BaseDto
from datetime import date
from uuid import UUID


class UserId(BaseDto):
    user_id: UUID


class DeleteUser(UserId):
    pass


class UpdateUser(UserId):
    email: str
    full_name: str
    date_of_birth: date
    photo_id: UUID


class User(BaseDto):
    email: str
    full_name: str
    date_of_birth: date
    photo_id: UUID


class UserLogin(User):  # ?
    email: str  # зачем email если он есть у User?
    password: str


class UserRegister(User):  # ?
    email: str  # зачем email если он есть у User?
    raw_password: str


class UserLogout(BaseDto):  # ?
    session_id: UUID
