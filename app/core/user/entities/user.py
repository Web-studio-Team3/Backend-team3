from dataclasses import dataclass
from uuid import UUID
from datetime import date


@dataclass
class User:
    id: UUID
    email: str
    hashed_password: str
    full_name: str
    date_of_birth: date
