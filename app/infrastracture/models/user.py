from typing import Optional

from pydantic import BaseModel


class UserModel(BaseModel):
    email: str
    hashed_password: str
    full_name: str
    date_of_birth: str
    picture_id: str
    telegram_id: Optional[int]
    telegram_username: Optional[str]
