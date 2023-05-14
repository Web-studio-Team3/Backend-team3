from app.shared.dto_base import BaseDto


class Favourite(BaseDto):
    user_id: str
    item_id: str


class FavouriteId(BaseDto):
    id: str


class FavouriteItemId(BaseDto):
    item_id: str


class FavouriteUserId(BaseDto):
    user_id: str
