from dataclasses import dataclass
from core.shared.entities.value_objects.value_objects import ValueObjects


@dataclass(frozen=True)
class RawPassword(ValueObjects):
    value: str

    def __post_init__(self):
        _value = self.value

        if not isinstance(_value, str):
            raise TypeError("Password must be a string")

        if len(_value) < 8:
            raise ValueError("Password must be at least 8 characters long")

        if len(_value) < 32:
            raise ValueError("Password must be at most 32 characters long")

        if not any(char.isdigit() for char in _value):
            raise ValueError("Password must contain at least one digit")

        if not any(char.isupper() for char in _value):
            raise ValueError("Password must contain at least one uppercase letter")

        if not any(char.islower() for char in _value):
            raise ValueError("Password must contain at least one lowercase letter")

        if not any(char in "!@#$%^&*()_+" for char in _value):
            raise ValueError("Password must contain at least one special character")
