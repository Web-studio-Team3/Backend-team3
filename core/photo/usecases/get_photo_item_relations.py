from core.shared.usecase.usecase import UseCase
from core.photo import dto
from core.photo.protocols.dao.photo_item_relation_read import PhotoRelationRead
from core.shared.protocols import Committer
from sqlalchemy.exc import IntegrityError
from core.photo import entities


class GetPhotoItemRelations(UseCase[dto.GetPhotoItemRelations, list[entities.PhotoItemRelation]]):
    def __init__(
            self,
            dao: PhotoRelationRead,
            committer: Committer
    ):
        self._dao = dao
        self._committer = committer

    async def execute(self, photo_item_relation_dto: dto.GetPhotoItemRelations) -> list[entities.PhotoItemRelation]:
        relations = await self._dao.get_photo_relations_by_item_id(item_id=photo_item_relation_dto.item_id)

        try:
            await self._committer.commit()
        except IntegrityError:
            await self._committer.rollback()
            raise ValueError("Item not found")

        return relations
