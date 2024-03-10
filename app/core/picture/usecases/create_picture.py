from app.core.picture.dao.picture_base_use_case import PictureUseCase
from app.core.picture.dao.picture_write import PictureWrite
from app.core.picture.dto.picture import PictureCreate
from app.core.picture.entities.picture import Picture
from app.core.picture.picture_helper import PictureHelper


class CreatePictureUseCase(PictureUseCase[PictureCreate, Picture]):
    def __init__(self, write_dao: PictureWrite, picture_helper: PictureHelper):
        self._write_dao = write_dao
        self._picture_helper = picture_helper

    def execute(self, picture_create: PictureCreate) -> Picture:
        picture_url = self._picture_helper.save_picture(picture_create.file)

        return self._write_dao.create(picture_url=picture_url)
