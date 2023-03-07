from dataclasses import dataclass
from dataclasses import field
from uuid import UUID
import uuid


@dataclass()
class Entity:
    id: UUID = field(init=False, default=None)

    @classmethod
    def generate_id(cls) -> UUID:
        return uuid.uuid4()
