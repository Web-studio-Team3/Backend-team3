from core.shared.usecase.usecase import UseCase
from core.photo import entities
from core.photo import dto
from core.photo.protocols.dao.photo_read import PhotoRead
from core.shared.protocols import Committer
from sqlalchemy.exc import IntegrityError


class GetPhoto(UseCase[dto.PhotoGet, entities.Photo]):
    def __init__(
            self,
            dao: PhotoRead,
            committer: Committer
    ):
        self._dao = dao
        self._committer = committer

    async def execute(self, photo_dto: dto.PhotoGet) -> entities.Photo:
        photo = await self._dao.get(photo_id=photo_dto.photo_id)

        try:
            await self._committer.commit()
        except IntegrityError:
            await self._committer.rollback()
            raise ValueError("Photo not found")

        return photo
