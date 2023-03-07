from core.shared.usecase.usecase import UseCase
from core.photo import dto
from core.photo.protocols.dao.photo_item_relation_write import PhotoRelationWrite
from core.shared.protocols import Committer
from sqlalchemy.exc import IntegrityError


class DeletePhotoItemRelation(UseCase[dto.DeletePhotoItemRelation, None]):
    def __init__(
            self,
            dao: PhotoRelationWrite,
            committer: Committer
    ):
        self._dao = dao
        self._committer = committer

    async def execute(self, photo_item_relation_dto: dto.DeletePhotoItemRelation) -> None:
        await self._dao.delete(relation_id=photo_item_relation_dto.relation_id)

        try:
            await self._committer.commit()
        except IntegrityError:
            await self._committer.rollback()
            raise ValueError("Photo or item not found")
