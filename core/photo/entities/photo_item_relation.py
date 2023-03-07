from core.shared.entities.entity import Entity
from dataclasses import dataclass
from uuid import UUID


@dataclass()
class PhotoItemRelation(Entity):
    photo_id: UUID
    item_id: UUID
