from dataclasses import dataclass
from dataclasses import field
import uuid


@dataclass
class Entity:
    id: uuid.UUID = field(init=False, default=None)
    
    @classmethod
    def generate_id(cls) -> uuid.UUID:
        return uuid.uuid4()