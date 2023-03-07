from core.shared.entities.value_objects.value_objects import ValueObjects
from dataclasses import dataclass
import re


@dataclass(frozen=True)
class Email(ValueObjects, str):
    value: str

    def __post_init__(self):
        v = self.value

        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        if not isinstance(v, str):
            raise TypeError("Email must be a string")

        if not re.fullmatch(regex, v):
            raise ValueError("Email must be valid")
