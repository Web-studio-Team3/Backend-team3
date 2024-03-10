from app.core.favourites.dao.favourite_read import FavouriteRead
from app.core.favourites.dto.favourite import Favourite, FavouriteUserId
from app.core.shared.usecase_base import UseCase


class GetFavouritesByUserIdUseCase(UseCase[FavouriteUserId, list[Favourite]]):
    def __init__(self, read_dao=FavouriteRead):
        self._read_dao = read_dao

    def execute(self, obj: FavouriteUserId) -> list[Favourite]:
        return self._read_dao.get_favourite_by_user_id(user_id=obj.user_id)
