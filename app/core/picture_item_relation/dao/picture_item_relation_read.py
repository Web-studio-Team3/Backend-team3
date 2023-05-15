from typing import Protocol
from app.core.picture_item_relation.entities.picture_item_relation import PictureItemRelation


class PictureItemRelationRead(Protocol):
    def get_picture_item_relations(self) -> list[PictureItemRelation]:
        raise NotImplementedError

    def get_picture_item_relation_by_id(self, id: str) -> PictureItemRelation:
        raise NotImplementedError
