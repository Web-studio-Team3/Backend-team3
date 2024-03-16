from app.core.picture.dao.picture_base_use_case import PictureUseCase
from app.core.picture.dao.picture_read import PictureRead
from app.core.picture.dto.picture import PictureId
from app.core.picture.entities.picture import Picture


class GetPictureByIdUseCase(PictureUseCase[PictureId, Picture]):
    def __init__(self, read_dao: PictureRead):
        self._read_dao = read_dao

    def execute(self, picture_id_obj: PictureId) -> Picture:
        return self._read_dao.get_picture_by_id(id=picture_id_obj.id)
