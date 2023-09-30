from fastapi import APIRouter, Depends
from fastapi_pagination import Page, paginate

from app.core.favourites.dto.favourite import (
    Favourite,
    FavouriteId,
    FavouriteItemId,
    FavouriteUserId
)

from app.core.favourites.entities.favourite import Favourite as FavouriteDataClass

from app.core.favourites.usecase.create_favourite import CreateFavouriteUseCase
from app.core.favourites.usecase.delete_favourite import DeleteFavouriteUseCase
from app.core.favourites.usecase.get_favourite_by_id import GetFavouriteByIdUseCase
from app.core.favourites.usecase.get_favourites_by_item_id import GetFavouritesByItemIdUseCase
from app.core.favourites.usecase.get_favourites_by_user_id import GetFavouritesByUserIdUseCase

from app.presentation.di import (
    provide_create_favourite_stub,
    provide_delete_favourite_stub,
    provide_get_favourite_by_id_stub,
    provide_get_favourites_by_item_id_stub,
    provide_get_favourites_by_user_id_stub
)

router = APIRouter()


@router.post(path="/")
async def create(
    favourite: Favourite,
    create_favourite_use_case: CreateFavouriteUseCase =
    Depends(provide_create_favourite_stub)
):
    favourite_id = create_favourite_use_case.execute(obj=favourite)
    return {
        "id": favourite_id.id
    }


@router.delete(path="/{favourite_id}")
async def delete(
    favourite_id: str,
    delete_favourite_use_case: DeleteFavouriteUseCase =
    Depends(provide_delete_favourite_stub)
):
    delete_favourite_use_case.execute(
        obj=FavouriteId(id=favourite_id))
    return {
        "message": "favourite was successfully deleted"
    }


@router.get(path="/{favourite_id}")
async def get(
    favourite_id: str,
    get_favourite_by_id_use_case: GetFavouriteByIdUseCase =
    Depends(provide_get_favourite_by_id_stub)
):
    favourite = get_favourite_by_id_use_case.execute(
        obj=FavouriteId(id=favourite_id))
    return favourite


@router.get(path="/item/{item_id}", response_model=Page[FavouriteDataClass])
async def get_by_item_id(
    item_id: str,
    get_favourite_by_item_id_use_case: GetFavouritesByItemIdUseCase =
    Depends(provide_get_favourites_by_item_id_stub)
):
    favourites = get_favourite_by_item_id_use_case.execute(
        obj=FavouriteItemId(item_id=item_id)
    )
    return paginate(list(favourites))


@router.get(path="/user/{user_id}", response_model=Page[FavouriteDataClass])
async def get_by_user_id(
    user_id: str,
    get_favourites_by_user_id_use_case: GetFavouritesByUserIdUseCase =
    Depends(provide_get_favourites_by_user_id_stub)
):
    favourites = get_favourites_by_user_id_use_case.execute(
        obj=FavouriteUserId(user_id=user_id))
    return paginate(list(favourites))
