from dataclasses import dataclass
from datetime import date


@dataclass
class User:
    id: str
    email: str
    hashed_password: str
    full_name: str
    date_of_birth: date
