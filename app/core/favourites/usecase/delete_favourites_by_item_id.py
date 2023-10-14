from app.core.shared.usecase_base import UseCase
from app.core.favourites.dao.favourite_write import FavouriteWrite
from app.core.favourites.dao.favourite_read import FavouriteRead
from app.core.favourites.dto.favourite import FavouriteItemId

class DeleteFavouritesByItemIdUseCase(UseCase[FavouriteItemId, None]):
    def __init__(
        self,
        write_dao: FavouriteWrite,
        read_dao: FavouriteRead
    ):
        self._write_dao = write_dao
        self._read_dao = read_dao

    def execute(self, obj: FavouriteItemId) -> None:
        try:
            favourites = self._read_dao.get_favourite_by_item_id(item_id=obj.item_id)
        except TypeError:
            return
        
        for favourite in favourites:
            self._write_dao.delete(favourite_id=favourite.id)
