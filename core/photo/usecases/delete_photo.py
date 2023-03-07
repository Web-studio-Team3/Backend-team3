from core.shared.usecase.usecase import UseCase
from core.photo import dto
from core.photo.protocols.dao.photo_write import PhotoWrite
from core.shared.protocols import Committer
from sqlalchemy.exc import IntegrityError


class DeletePhoto(UseCase[dto.PhotoGet, None]):
    def __init__(
            self,
            dao: PhotoWrite,
            committer: Committer
    ):
        self._dao = dao
        self._committer = committer

    async def execute(self, photo_dto: dto.PhotoDelete) -> None:
        await self._dao.delete(photo_id=photo_dto.photo_id)

        try:
            await self._committer.commit()
        except IntegrityError:
            await self._committer.rollback()
            raise ValueError("Photo not found")
