from app.core.shared.usecase_base import UseCase
from app.core.favourites.dao.favourite_read import FavouriteRead
from app.core.favourites.dto.favourite import (
    FavouriteId,
    Favourite
)


class GetFavouriteByIdUseCase(UseCase[FavouriteId, Favourite]):
    def __init__(self, read_dao=FavouriteRead):
        self._read_dao = read_dao

    def execute(self, obj: FavouriteId) -> Favourite:
        return self._read_dao.get_favourite_by_id(id=obj.id)
