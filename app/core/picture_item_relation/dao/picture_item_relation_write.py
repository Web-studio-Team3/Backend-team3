from typing import Protocol
from app.core.picture_item_relation.dto.picture_item_relation import PictureItemRelation


class PictureItemRelationWrite(Protocol):
    def create(self, picture_item_relation: PictureItemRelation) -> PictureItemRelation:
        raise NotImplementedError

    def delete(self, id: str) -> None:
        raise NotImplementedError
    
    def update(self, picture_item_relation: PictureItemRelation) -> PictureItemRelation:
        raise NotImplementedError
