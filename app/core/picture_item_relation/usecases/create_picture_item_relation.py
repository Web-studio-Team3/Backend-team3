from app.core.picture_item_relation.dao.picture_item_relation_write import (
    PictureItemRelationWrite,
)
from app.core.picture_item_relation.dto.picture_item_relation import PictureItemRelation
from app.core.shared.usecase_base import UseCase


class CreatePictureItemRelationUseCase(
    UseCase[PictureItemRelation, PictureItemRelation]
):
    def __init__(self, write_dao: PictureItemRelationWrite):
        self._write_dao = write_dao

    def execute(self, obj: PictureItemRelation) -> PictureItemRelation:
        return self._write_dao.create(obj)
