from app.core.picture_item_relation.dao.picture_item_relation_write import (
    PictureItemRelationWrite,
)
from app.core.picture_item_relation.dto.picture_item_relation import (
    PictureItemRelationId,
)
from app.core.shared.usecase_base import UseCase


class DeletePictureItemRelationUseCase(UseCase[PictureItemRelationId, None]):
    def __init__(self, write_dao: PictureItemRelationWrite):
        self._write_dao = write_dao

    def execute(self, obj: PictureItemRelationId) -> None:
        self._write_dao.delete(id=obj.id)
