from core.shared.usecase.usecase import UseCase
from core.photo import entities
from core.photo import dto
from core.photo.protocols.dao.photo_item_relation_write import PhotoRelationWrite
from core.shared.protocols import Committer
from sqlalchemy.exc import IntegrityError


class AddPhotoItemRelation(UseCase[dto.PhotoItemRelation, None]):
    def __init__(
            self,
            dao: PhotoRelationWrite,
            committer: Committer
    ):
        self._dao = dao
        self._committer = committer

    async def execute(self, photo_item_relation_dto: dto.PhotoItemRelation) -> None:
        photo_item_relation = entities.PhotoItemRelation(
            item_id=photo_item_relation_dto.item_id,
            photo_id=photo_item_relation_dto.photo_id
        )

        await self._dao.create(relation=photo_item_relation)

        try:
            await self._committer.commit()
        except IntegrityError:
            await self._committer.rollback()
            raise ValueError("Photo or item not found")
