from fastapi import APIRouter, Depends
from fastapi_pagination import Page, paginate

from app.core.sold_item.dto.sold_item_relation import (
    SoldItemRelation,
    SoldItemRelationId,
    SoldItemRelationItemId,
    SoldItemRelationBuyerId,
    SoldItemRelationSellerId
)

from app.core.sold_item.entities.sold_item_relation import SoldItemRelation as SoldItemRelationDataClass

from app.core.sold_item.usecase.create_sold_item_relation import CreateSoldItemRelationUseCase
from app.core.sold_item.usecase.delete_sold_item_relation import DeleteSoldItemRelationUseCase
from app.core.sold_item.usecase.get_sold_item_relation_by_buyer_id import GetSoldItemRelationByBuyerIdUseCase
from app.core.sold_item.usecase.get_sold_item_relation_by_id import GetSoldItemRelationByIdUseCase
from app.core.sold_item.usecase.get_sold_item_relation_by_item_id import GetSoldItemRelationByItemIdUseCase
from app.core.sold_item.usecase.get_sold_item_relation_by_seller_id import GetSoldItemRelationBySellerIdUseCase

from app.presentation.di import (
    provide_create_sold_item_relation_stub,
    provide_delete_sold_item_relation_stub,
    provide_get_sold_item_relation_by_buyer_id_stub,
    provide_get_sold_item_relation_by_id_stub,
    provide_get_sold_item_relation_by_item_id_stub,
    provide_get_sold_item_relation_by_seller_id_stub
)

router = APIRouter()


@router.post(path="/")
async def create(
    sold_item_relation: SoldItemRelation,
    create_sold_item_relation_use_case: CreateSoldItemRelationUseCase =
    Depends(provide_create_sold_item_relation_stub)
):
    sold_item_relation_id = create_sold_item_relation_use_case.execute(obj=sold_item_relation)
    return {
        "id": sold_item_relation_id.id
    }


@router.delete(path="/{sold_item_relation_id}")
async def delete(
    sold_item_relation_id: str,
    delete_sold_item_relation_use_case: DeleteSoldItemRelationUseCase =
    Depends(provide_delete_sold_item_relation_stub)
):
    delete_sold_item_relation_use_case.execute(
        obj=SoldItemRelationId(id=sold_item_relation_id ))
    return {
        "message": "sale_item_relation was successfully deleted"
    }


@router.get(path="/{sold_item_relation_id}")
async def get(
    sold_item_relation_id: str,
    get_sold_item_relation_by_id_use_case: GetSoldItemRelationByIdUseCase =
    Depends(provide_get_sold_item_relation_by_id_stub)
):
    sold_item_relation = get_sold_item_relation_by_id_use_case.execute(
        obj=SoldItemRelationId(id=sold_item_relation_id))
    return sold_item_relation


@router.get(path="/item/{item_id}")
async def get_by_item_id(
    item_id: str,
    get_sold_item_relation_by_item_id_use_case: GetSoldItemRelationByItemIdUseCase =
    Depends(provide_get_sold_item_relation_by_item_id_stub)
):
    sold_item_relation = get_sold_item_relation_by_item_id_use_case.execute(
        obj=SoldItemRelationItemId(item_id=item_id)
    )
    return sold_item_relation


@router.get(path="/seller/{seller_id}", response_model=Page[SoldItemRelationDataClass])
async def get_by_seller_id(
    seller_id: str,
    get_sold_item_relation_by_seller_id_use_case: GetSoldItemRelationBySellerIdUseCase =
    Depends(provide_get_sold_item_relation_by_seller_id_stub)
):
    sold_item_relations = get_sold_item_relation_by_seller_id_use_case.execute(
        obj=SoldItemRelationSellerId(seller_id=seller_id))
    return paginate(sold_item_relations)


@router.get(path="/buyer/{buyer_id}", response_model=Page[SoldItemRelationDataClass])
async def get_by_buyer_id(
    buyer_id: str,
    get_sold_item_relation_by_buyer_id_use_case: GetSoldItemRelationByBuyerIdUseCase =
    Depends(provide_get_sold_item_relation_by_buyer_id_stub)
):
    sold_item_relations = get_sold_item_relation_by_buyer_id_use_case.execute(
        obj=SoldItemRelationBuyerId(buyer_id=buyer_id))
    return paginate(sold_item_relations)
