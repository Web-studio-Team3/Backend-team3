from core.shared.entities.entity import Entity
from dataclasses import dataclass
from core.user.entities import value_objects
from datetime import date
from uuid import UUID


@dataclass
class User(Entity):
    email: value_objects.Email
    hashed_password: value_objects.HashedPassword
    fullname: str
    date_of_birth: date
    photo_id: UUID
