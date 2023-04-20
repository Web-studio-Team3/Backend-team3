from app.core.picture.dao.picture_base_use_case import PictureUseCase
from app.core.picture.dao.picture_write import PictureWrite
from app.core.picture.dao.picture_read import PictureRead
from app.core.picture.dto.picture import PictureId
from app.core.picture.picture_helper import PictureHelper


class DeletePictureByIDUseCase(PictureUseCase[PictureId, None]):
    def __init__(
            self,
            write_dao: PictureWrite,
            read_dao: PictureRead,
            picture_helper: PictureHelper
    ):
        self._write_dao = write_dao
        self._read_dao = read_dao
        self._picture_helper = picture_helper

    def execute(self, picture_id_obj: PictureId) -> None:
        picture = self._read_dao.get_picture_by_id(id=picture_id_obj.id)

        self._picture_helper.delete_picture(picture_url=picture.picture_url)
        self._write_dao.delete(id=picture.id)
