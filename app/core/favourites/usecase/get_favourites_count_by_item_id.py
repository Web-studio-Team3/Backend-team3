from app.core.shared.usecase_base import UseCase
from app.core.favourites.dao.favourite_read import FavouriteRead
from app.core.favourites.dto.favourite import FavouriteItemId
from app.core.favourites.entities.favourite import Favourite


class GetFavouritesCountByItemIdUseCase(UseCase[FavouriteItemId, int]):
    def __init__(self, read_dao=FavouriteRead):
        self._read_dao = read_dao

    def execute(self, obj: FavouriteItemId) -> int:
        return len(
            self._read_dao.get_favourite_by_item_id(item_id=obj.item_id)
        )
