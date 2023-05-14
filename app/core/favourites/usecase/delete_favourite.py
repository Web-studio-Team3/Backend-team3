from app.core.shared.usecase_base import UseCase
from app.core.favourites.dao.favourite_write import FavouriteWrite
from app.core.favourites.dto.favourite import FavouriteId


class DeleteFavouriteUseCase(UseCase[FavouriteId, None]):
    def __init__(self, write_dao: FavouriteWrite):
        self._write_dao = write_dao

    def execute(self, obj: FavouriteId) -> None:
        self._write_dao.delete(favourite_id=obj.id)
