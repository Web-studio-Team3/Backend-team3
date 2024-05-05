from fastapi import APIRouter, Depends
from fastapi_pagination import Page, paginate

from app.core.cart.dto.cart import (
    CartItem,
    CartUserId,
    CartItemId,
    CartId,
)
from app.core.cart.entities.cart_item import CartItem as CartItemDataClass

from app.core.cart.usecase.get_cart_by_user_id import GetCartByUserIdUseCase
from app.core.cart.usecase.create_cart_item import CreateCartItemUseCase
from app.core.cart.usecase.delete_cart_item import DeleteCartItemUseCase

from app.core.token.usecases.get_access_token_by_jwt import GetAccessTokenByJwtUseCase
from app.presentation.bearer import JWTBearer
from app.presentation.di import (
    provide_get_access_token_by_jwt_stub,
    provide_get_cart_by_user_id_stub,
    provide_create_cart_item_stub,
    provide_delete_cart_item_stub,
)

router = APIRouter()


@router.get(path="/user/", response_model=Page[CartItemDataClass])
async def get_by_user(
    get_cart_by_user_id_use_case: GetCartByUserIdUseCase = Depends(
        provide_get_cart_by_user_id_stub
    ),
    jwt: str = Depends(JWTBearer()),
    get_access_token_by_jwt_use_case: GetAccessTokenByJwtUseCase = Depends(
        provide_get_access_token_by_jwt_stub
    ),
):
    user_id = get_access_token_by_jwt_use_case.execute(jwt).user_id
    cart = get_cart_by_user_id_use_case.execute(
        obj=CartUserId(user_id=user_id)
    )
    return paginate(list(cart))


@router.post(path="/")
async def create(
    item_id: CartItemId,
    create_cart_item_use_case: CreateCartItemUseCase = Depends(
        provide_create_cart_item_stub
    ),
    jwt: str = Depends(JWTBearer()),
    get_access_token_by_jwt_use_case: GetAccessTokenByJwtUseCase = Depends(
        provide_get_access_token_by_jwt_stub
    ),
    get_cart_by_user_id_use_case: GetCartByUserIdUseCase = Depends(
        provide_get_cart_by_user_id_stub
    ),
):
    user_id = get_access_token_by_jwt_use_case.execute(jwt).user_id
    cart = get_cart_by_user_id_use_case.execute(CartUserId(user_id=user_id))
    if any(cart_item.item_id == item_id.item_id for cart_item in cart):
        return {"chat message": "This item is already in your cart"}
    
    cart_id = create_cart_item_use_case.execute(
        obj=CartItem(user_id=user_id, item_id=item_id.item_id)
    )
    return {"id": cart_id.id}


@router.delete(path="/{cart_id}")
async def delete(
    cart_id: str,
    delete_cart_item_use_case: DeleteCartItemUseCase = Depends(
        provide_delete_cart_item_stub
    ),
    jwt: str = Depends(JWTBearer()),
    get_access_token_by_jwt_use_case: GetAccessTokenByJwtUseCase = Depends(
        provide_get_access_token_by_jwt_stub
    ),
    get_cart_by_user_id_use_case: GetCartByUserIdUseCase = Depends(
        provide_get_cart_by_user_id_stub
    ),
):
    user_id = get_access_token_by_jwt_use_case.execute(jwt).user_id
    cart = get_cart_by_user_id_use_case.execute(CartUserId(user_id=user_id))
    if not any(cart_item.user_id == user_id for cart_item in cart):
        return {"chat_message": "Not allowed for this user"}

    delete_cart_item_use_case.execute(obj=CartId(id=cart_id))
    return {"chat_message": "cart item was successfully deleted"}



