import uuid
from dataclasses import dataclass, field


@dataclass
class Entity:
    id: uuid.UUID = field(init=False, default=None)

    @classmethod
    def generate_id(cls) -> uuid.UUID:
        return uuid.uuid4()
