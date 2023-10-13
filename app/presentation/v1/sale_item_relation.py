from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination import Page, paginate

from app.core.sale_item.dto.sale_item_relation import (
    SaleItemRelation,
    SaleItemRelationId,
    SaleItemRelationItemId,
    SaleItemRelationUserId
)

from app.core.sale_item.entities.sale_item_relation import SaleItemRelation as SaleItemRelationDataClass

from app.core.sale_item.usecase.create_sale_item_relation import CreateSaleItemRelationUseCase
from app.core.sale_item.usecase.delete_sale_item_relation import DeleteSaleItemRelationUseCase
from app.core.sale_item.usecase.get_sale_item_relation_by_id import GetSaleItemRelationByIdUseCase
from app.core.sale_item.usecase.get_sale_item_relation_by_item_id import GetSaleItemRelationByItemIdUseCase
from app.core.sale_item.usecase.get_sale_item_relation_by_user_id import GetSaleItemRelationByUserIdUseCase

from app.core.token.usecases.get_access_token_by_jwt import GetAccessTokenByJwtUseCase
from app.presentation.bearer import JWTBearer

from app.presentation.di import (
    provide_create_sale_item_relation_stub,
    provide_delete_sale_item_relation_stub,
    provide_get_sale_item_relation_by_id_stub,
    provide_get_sale_item_relation_by_item_id_stub,
    provide_get_sale_item_relation_by_user_id_stub,
    provide_get_access_token_by_jwt_stub,
)

router = APIRouter()


@router.post(path="/")
async def create(
    item_id: str,
    create_sale_item_relation_use_case: CreateSaleItemRelationUseCase =
    Depends(provide_create_sale_item_relation_stub),
    jwt: str = Depends(JWTBearer()),
    get_access_token_by_jwt_use_case: GetAccessTokenByJwtUseCase = 
    Depends(provide_get_access_token_by_jwt_stub),
):
    user_id = get_access_token_by_jwt_use_case.execute(jwt).user_id

    sale_item_relation_id = create_sale_item_relation_use_case.execute(
        obj=SaleItemRelation(user_id=user_id, item_id=item_id)
    )
    return {
        "id": sale_item_relation_id.id
    }


@router.delete(path="/{sale_item_relation_id}")
async def delete(
    sale_item_relation_id: str,
    delete_sale_item_relation_use_case: DeleteSaleItemRelationUseCase =
    Depends(provide_delete_sale_item_relation_stub),
    jwt: str = Depends(JWTBearer()),
    get_access_token_by_jwt_use_case: GetAccessTokenByJwtUseCase = 
    Depends(provide_get_access_token_by_jwt_stub),
    get_sale_item_realtion_by_id_use_case: GetSaleItemRelationByIdUseCase =
    Depends(provide_get_sale_item_relation_by_id_stub)
):
    try:
        sale_item_relation = get_sale_item_realtion_by_id_use_case.execute(
            obj=SaleItemRelationId(id=sale_item_relation_id)
        )
    except TypeError:
        raise HTTPException(
            status_code=400,
            detail="No such relation"
        )
    user_id = get_access_token_by_jwt_use_case.execute(token=jwt).user_id
    if (sale_item_relation.user_id != user_id):
        raise HTTPException(
            status_code=403,
            detail="Not allowed for this user"
        )
    
    delete_sale_item_relation_use_case.execute(
        obj=SaleItemRelationId(id=sale_item_relation_id)
    )
    return {
        "chat_message": "sale_item_relation was successfully deleted"
    }


@router.get(path="/{sale_item_relation_id}")
async def get(
    sale_item_relation_id: str,
    get_sale_item_relation_by_id_use_case: GetSaleItemRelationByIdUseCase =
    Depends(provide_get_sale_item_relation_by_id_stub)
):
    try:
        sale_item_relation = get_sale_item_relation_by_id_use_case.execute(
            obj=SaleItemRelationId(id=sale_item_relation_id)
        )
    except TypeError:
        raise HTTPException(
            status_code=400,
            detail="No such relation"
        )
    return sale_item_relation


@router.get(path="/item/{item_id}")
async def get_by_item_id(
    item_id: str,
    get_sale_item_relation_by_item_id_use_case: GetSaleItemRelationByItemIdUseCase =
    Depends(provide_get_sale_item_relation_by_item_id_stub)
):
    try:
        sale_item_relation = get_sale_item_relation_by_item_id_use_case.execute(
            obj=SaleItemRelationItemId(item_id=item_id)
        )
    except TypeError:
        raise HTTPException(
            status_code=400,
            detail="No such relation"
        )

    return sale_item_relation


@router.get(path="/user/{user_id}", response_model=Page[SaleItemRelationDataClass])
async def get_by_user_id(
    user_id: str,
    get_sale_item_relation_by_user_id_use_case: GetSaleItemRelationByUserIdUseCase =
    Depends(provide_get_sale_item_relation_by_user_id_stub)
):
    sale_item_relations = get_sale_item_relation_by_user_id_use_case.execute(
        obj=SaleItemRelationUserId(user_id=user_id)
    )

    return paginate(list(sale_item_relations))
