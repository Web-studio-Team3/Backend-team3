from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class User:
    id: str
    email: str
    hashed_password: str
    full_name: str
    date_of_birth: date
    picture_id: str
    telegram_id: Optional[int]
    telegram_username: Optional[str]
    telegram_token: Optional[str]
