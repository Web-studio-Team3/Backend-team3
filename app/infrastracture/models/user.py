from pydantic import BaseModel
from datetime import date
from app.core.user.entities.user import User


class UserModel(BaseModel):
    email: str
    hashed_password: str
    full_name: str
    date_of_birth: str


def from_entity(user: User) -> UserModel:
    return UserModel(
        email=user.email,
        hashed_password=user.hashed_password,
        full_name=user.full_name,
        date_of_birth=user.date_of_birth
    )
