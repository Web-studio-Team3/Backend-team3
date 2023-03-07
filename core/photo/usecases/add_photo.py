from core.shared.usecase.usecase import UseCase
from core.photo import entities
from core.photo import dto
from core.photo.protocols.dao.photo_write import PhotoWrite
from core.shared.protocols import Committer


class AddPhoto(UseCase[dto.Photo, None]):
    def __init__(
            self,
            dao: PhotoWrite,
            committer: Committer
    ):
        self._dao = dao
        self._committer = committer

    async def execute(self, photo_dto: dto.Photo) -> None:
        photo = entities.Photo(url=photo_dto.url)

        await self._dao.create(photo)
