from fastapi import APIRouter, Depends
from fastapi_pagination import Page, paginate

from app.core.favourites.dto.favourite import (
    Favourite,
    FavouriteId,
    FavouriteItemId,
    FavouriteUserId,
)
from app.core.favourites.entities.favourite import Favourite as FavouriteDataClass
from app.core.favourites.usecase.create_favourite import CreateFavouriteUseCase
from app.core.favourites.usecase.delete_favourite import DeleteFavouriteUseCase
from app.core.favourites.usecase.get_favourite_by_id import GetFavouriteByIdUseCase
from app.core.favourites.usecase.get_favourites_by_user_id import (
    GetFavouritesByUserIdUseCase,
)
from app.core.favourites.usecase.get_favourites_count_by_item_id import (
    GetFavouritesCountByItemIdUseCase,
)
from app.core.token.usecases.get_access_token_by_jwt import GetAccessTokenByJwtUseCase
from app.presentation.bearer import JWTBearer
from app.presentation.di import (
    provide_create_favourite_stub,
    provide_delete_favourite_stub,
    provide_get_access_token_by_jwt_stub,
    provide_get_favourite_by_id_stub,
    provide_get_favourites_by_user_id_stub,
    provide_get_favourites_count_by_item_id_stub,
)

router = APIRouter()


@router.post(path="/")
async def create(
    item_id: FavouriteItemId,
    create_favourite_use_case: CreateFavouriteUseCase = Depends(
        provide_create_favourite_stub
    ),
    jwt: str = Depends(JWTBearer()),
    get_access_token_by_jwt_use_case: GetAccessTokenByJwtUseCase = Depends(
        provide_get_access_token_by_jwt_stub
    ),
):
    user_id = get_access_token_by_jwt_use_case.execute(jwt).user_id
    favourite_id = create_favourite_use_case.execute(
        obj=Favourite(user_id=user_id, item_id=item_id.item_id)
    )
    return {"id": favourite_id.id}


@router.delete(path="/{favourite_id}")
async def delete(
    favourite_id: str,
    delete_favourite_use_case: DeleteFavouriteUseCase = Depends(
        provide_delete_favourite_stub
    ),
    jwt: str = Depends(JWTBearer()),
    get_access_token_by_jwt_use_case: GetAccessTokenByJwtUseCase = Depends(
        provide_get_access_token_by_jwt_stub
    ),
    get_favourites_by_user_id: GetFavouritesByUserIdUseCase = Depends(
        provide_get_favourites_by_user_id_stub
    ),
):
    user_id = get_access_token_by_jwt_use_case.execute(jwt).user_id
    favourites = get_favourites_by_user_id.execute(FavouriteUserId(user_id=user_id))
    if not any(favourite.user_id == user_id for favourite in favourites):
        return {"message": "Not allowed for this user"}

    delete_favourite_use_case.execute(obj=FavouriteId(id=favourite_id))
    return {"chat_message": "favourite was successfully deleted"}


@router.get(path="/{favourite_id}")
async def get(
    favourite_id: str,
    get_favourite_by_id_use_case: GetFavouriteByIdUseCase = Depends(
        provide_get_favourite_by_id_stub
    ),
    jwt: str = Depends(JWTBearer()),
    get_access_token_by_jwt_use_case: GetAccessTokenByJwtUseCase = Depends(
        provide_get_access_token_by_jwt_stub
    ),
):
    favourite = get_favourite_by_id_use_case.execute(obj=FavouriteId(id=favourite_id))

    user_id = get_access_token_by_jwt_use_case.execute(jwt).user_id
    if user_id != favourite.user_id:
        return {"message": "Not allowed for this user"}

    return favourite


@router.get(path="/item/{item_id}")
async def get_count_of_favourites_by_item(
    item_id: str,
    get_favourites_count_by_item_id_use_case: GetFavouritesCountByItemIdUseCase = Depends(
        provide_get_favourites_count_by_item_id_stub
    ),
):
    favourites_count = get_favourites_count_by_item_id_use_case.execute(
        obj=FavouriteItemId(item_id=item_id)
    )
    return {"count": favourites_count}


@router.get(path="/user/", response_model=Page[FavouriteDataClass])
async def get_by_user(
    get_favourites_by_user_id_use_case: GetFavouritesByUserIdUseCase = Depends(
        provide_get_favourites_by_user_id_stub
    ),
    jwt: str = Depends(JWTBearer()),
    get_access_token_by_jwt_use_case: GetAccessTokenByJwtUseCase = Depends(
        provide_get_access_token_by_jwt_stub
    ),
):
    user_id = get_access_token_by_jwt_use_case.execute(jwt).user_id
    favourites = get_favourites_by_user_id_use_case.execute(
        obj=FavouriteUserId(user_id=user_id)
    )
    return paginate(list(favourites))
