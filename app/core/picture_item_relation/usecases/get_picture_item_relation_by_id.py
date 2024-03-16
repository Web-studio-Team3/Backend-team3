from app.core.picture_item_relation.dao.picture_item_relation_read import (
    PictureItemRelationRead,
)
from app.core.picture_item_relation.dto.picture_item_relation import (
    PictureItemRelationId,
)
from app.core.picture_item_relation.entities.picture_item_relation import (
    PictureItemRelation,
)
from app.core.shared.usecase_base import UseCase


class GetPictureItemRelationByIdUseCase(
    UseCase[PictureItemRelationId, PictureItemRelation]
):
    def __init__(self, read_dao: PictureItemRelationRead):
        self._read_dao = read_dao

    def execute(self, obj: PictureItemRelationId) -> PictureItemRelation:
        return self._read_dao.get_picture_item_relation_by_id(id=obj.id)
