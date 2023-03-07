from core.shared.entities.entity import Entity
from dataclasses import dataclass
from uuid import UUID


@dataclass()
class UserItemTrackingRelation(Entity):
    user_id: UUID
    item_id: UUID
