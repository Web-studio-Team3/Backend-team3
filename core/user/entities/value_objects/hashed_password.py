from dataclasses import dataclass
from core.shared.entities.value_objects.value_objects import ValueObjects


@dataclass(frozen=True)
class HashedPassword(ValueObjects, str):
    value: str
