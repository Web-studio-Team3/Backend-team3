from app.core.shared.usecase_base import UseCase
from app.core.picture_item_relation.dao.picture_item_relation_read import PictureItemRelationRead
from app.core.picture_item_relation.entities.picture_item_relation import PictureItemRelation
from app.core.picture_item_relation.dto.picture_item_relation import PictureItemRelationItemId


class GetPictureItemRelationsByItemIdUseCase(UseCase[PictureItemRelationItemId, list[PictureItemRelation]]):
    def __init__(
            self,
            read_dao: PictureItemRelationRead
    ):
        self._read_dao = read_dao

    def execute(self, obj: PictureItemRelationItemId) -> list[PictureItemRelation]:
        relations = self._read_dao.get_picture_item_relations()
        item_relations = filter(lambda relation: relation.item_id == obj.item_id, relations)

        return item_relations
