from core.shared.usecase.usecase import UseCase
from core.photo import dto
from core.photo.protocols.dao.photo_item_relation_read import PhotoRelationRead
from core.shared.protocols import Committer
from sqlalchemy.exc import IntegrityError
from core.photo import entities


class GetPhotoItemRelation(UseCase[dto.GetPhotoItemRelation, entities.PhotoItemRelation]):
    def __init__(
            self,
            dao: PhotoRelationRead,
            committer: Committer
    ):
        self._dao = dao
        self._committer = committer

    async def execute(self, photo_item_relation_dto: dto.GetPhotoItemRelation) -> entities.PhotoItemRelation:
        relation = await self._dao.get_photo_relation_by_id(relation_id=photo_item_relation_dto.relation_id)

        try:
            await self._committer.commit()
        except IntegrityError:
            await self._committer.rollback()
            raise ValueError("Relation not found")

        return relation
