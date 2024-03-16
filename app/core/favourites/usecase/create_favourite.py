from app.core.favourites.dao.favourite_write import FavouriteWrite
from app.core.favourites.dto.favourite import Favourite, FavouriteId
from app.core.shared.usecase_base import UseCase


class CreateFavouriteUseCase(UseCase[Favourite, FavouriteId]):
    def __init__(self, write_dao: FavouriteWrite):
        self._write_dao = write_dao

    def execute(self, obj: Favourite) -> FavouriteId:
        return self._write_dao.create(favourite=obj)
