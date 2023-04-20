from app.core.picture.dao.picture_base_use_case import PictureUseCase

from app.core.user.dto.user import UserId
from app.core.user.usecases.get_user_by_id import GetUserByIdUseCase

from app.core.picture.usecases.delete_picture_by_id import DeletePictureByIDUseCase
from app.core.picture.dto.picture import PictureId


class DeletePictureByUserIDUseCase(PictureUseCase[UserId, None]):
    def __init__(
            self,
            get_user_by_id_use_case: GetUserByIdUseCase,
            delete_picture_use_case: DeletePictureByIDUseCase
    ):
        self._get_user_by_id_use_case = get_user_by_id_use_case
        self._delete_picture_use_case = delete_picture_use_case

    def execute(self, user_id_obj: UserId) -> None:
        user = self._get_user_by_id_use_case.execute(user_id=user_id_obj)
        self._delete_picture_use_case.execute(PictureId(id=user.picture_id))
