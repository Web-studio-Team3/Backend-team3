from core.shared.entities.entity import Entity
from dataclasses import dataclass


@dataclass()
class Photo(Entity):
    url: str
