from fastapi import APIRouter, Depends, status, HTTPException, UploadFile, File, Form

from app.core.sale_item.dto.sale_item_relation import (
    SaleItemRelation,
    SaleItemRelationId,
    SaleItemRelationItemId,
    SaleItemRelationUserId
)

from app.core.sale_item.usecase.create_sale_item_relation import CreateSaleItemRelationUseCase
from app.core.sale_item.usecase.delete_sale_item_relation import DeleteSaleItemRelationUseCase
from app.core.sale_item.usecase.get_sale_item_relation_by_id import GetSaleItemRelationByIdUseCase
from app.core.sale_item.usecase.get_sale_item_relation_by_item_id import GetSaleItemRelationByItemIdUseCase
from app.core.sale_item.usecase.get_sale_item_relation_by_user_id import GetSaleItemRelationByUserIdUseCase

from app.presentation.di import (
    provide_create_sale_item_relation_stub,
    provide_delete_sale_item_relation_stub,
    provide_get_sale_item_relation_by_id_stub,
    provide_get_sale_item_relation_by_item_id_stub,
    provide_get_sale_item_relation_by_user_id_stub
)

router = APIRouter()


@router.post(path="/")
async def create(
    sale_item_relation: SaleItemRelation,
    create_sale_item_relation_use_case: CreateSaleItemRelationUseCase =
    Depends(provide_create_sale_item_relation_stub)
):
    sale_item_relation_id = create_sale_item_relation_use_case.execute(obj=sale_item_relation)
    return {
        "id": sale_item_relation_id.id
    }


@router.delete(path="/{sale_item_relation_id}")
async def delete(
    sale_item_relation_id: str,
    delete_sale_item_relation_use_case: DeleteSaleItemRelationUseCase =
    Depends(provide_delete_sale_item_relation_stub)
):
    delete_sale_item_relation_use_case.execute(
        obj=SaleItemRelationId(id=sale_item_relation_id))
    return {
        "message": "sale_item_relation was successfully deleted"
    }


@router.get(path="/{sale_item_relation_id}")
async def get(
    sale_item_relation_id: str,
    get_sale_item_relation_by_id_use_case: GetSaleItemRelationByIdUseCase =
    Depends(provide_get_sale_item_relation_by_id_stub)
):
    sale_item_relation = get_sale_item_relation_by_id_use_case.execute(
        obj=SaleItemRelationId(id=sale_item_relation_id))
    return sale_item_relation


@router.get(path="/item/{item_id}")
async def get_by_item_id(
    item_id: str,
    get_sale_item_relation_by_item_id_use_case: GetSaleItemRelationByItemIdUseCase =
    Depends(provide_get_sale_item_relation_by_item_id_stub)
):
    sale_item_relation = get_sale_item_relation_by_item_id_use_case.execute(
        obj=SaleItemRelationItemId(item_id=item_id)
    )
    return sale_item_relation


@router.get(path="/user/{user_id}")
async def get_by_user_id(
    user_id: str,
    get_sale_item_relation_by_user_id_use_case: GetSaleItemRelationByUserIdUseCase =
    Depends(provide_get_sale_item_relation_by_user_id_stub)
):
    sale_item_relations = get_sale_item_relation_by_user_id_use_case.execute(
        obj=SaleItemRelationUserId(user_id=user_id))
    return {
        "items": list(sale_item_relations)
    }
