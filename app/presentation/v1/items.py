from typing import Optional

from bson import ObjectId
from fastapi import APIRouter, Depends, status, HTTPException, Form, UploadFile, File

from app.core.item.dto.item import (
    ItemId, ItemCreate, ItemUpdate, ItemUpdateWithId
)
from app.core.user.dto.user import UserId

from app.core.item.usecases.get_item_all import GetItemAllUseCase
from app.core.item.usecases.get_item_by_id import GetItemByIdUseCase
from app.core.item.usecases.get_items_by_seller_id import GetAllItemsBySellerIdUseCase
from app.core.item.usecases.create_item import CreateItemUseCase
from app.core.item.usecases.delete_item import DeleteItemUseCase
from app.core.item.usecases.update_item import UpdateItemUseCase

from app.core.picture.usecases.create_picture import CreatePictureUseCase
from app.core.picture.dto.picture import PictureCreate

from app.presentation.bearer import JWTBearer
from app.core.token.usecases.get_access_token_by_jwt import GetAccessTokenByJwtUseCase


from app.core.picture_item_relation.usecases.create_picture_item_relation import CreatePictureItemRelationUseCase
from app.core.picture_item_relation.usecases.get_picture_item_relations_by_item_id import GetPictureItemRelationsByItemIdUseCase
from app.core.picture_item_relation.usecases.delete_picture_item_relation import DeletePictureItemRelationUseCase
from app.core.picture_item_relation.dto.picture_item_relation import (
    PictureItemRelation,
    PictureItemRelationItemId,
    PictureItemRelationId
)

from app.presentation.di import (
    provide_get_items_stub,
    provide_get_item_by_id_stub,
    provide_create_item_stub,
    provide_delete_item_stub,
    provide_update_item_stub,
    provide_create_picture_stub,
    provide_create_picture_item_relation_stub,
    provide_get_picture_item_relations_by_item_id_stub,
    provide_delete_picture_item_relation_stub,
    provide_get_access_token_by_jwt_stub,
    provide_get_items_by_seller_id_stub,
)

from elasticsearch import AsyncElasticsearch

router = APIRouter()

es = AsyncElasticsearch("http://elasticsearch:9200")


@router.get(path='/')
async def get_item_all(
    get_item_all_use_case: GetItemAllUseCase = Depends(provide_get_items_stub)
):
    try:
        items = get_item_all_use_case.execute()
    except TypeError:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No items"
        )
    return items


@router.get(path='/{item_id}')
async def get_item_by_id(
    item_id: str,
    get_item_by_id_use_case: GetItemByIdUseCase = Depends(
        provide_get_item_by_id_stub),
    get_picture_items_relation_by_item_id_use_case:
    GetPictureItemRelationsByItemIdUseCase = Depends(
        provide_get_picture_item_relations_by_item_id_stub
    )
):
    try:
        item = get_item_by_id_use_case.execute(ItemId(id=item_id))
        relations = get_picture_items_relation_by_item_id_use_case.execute(
            PictureItemRelationItemId(
                item_id=item_id
            )
        )
    except TypeError:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No item with such id"
        )
    pictures = []
    for relation in relations:
        pictures.append(relation.picture_id)

    return {
        "id": item.id,
        "category_id": item.category_id,
        "title": item.title,
        "description": item.description,
        "condition": item.condition,
        "address": item.address,
        "cost": item.cost,
        "status": item.status,
        "pictures_id": list(pictures),
        "buyer_id": item.buyer_id,
        "seller_id": item.seller_id,
    }


@router.get(path='/seller_id/{seller_id}')
async def get_items_by_seller_id(
        seller_id: str,
        get_all_items_by_seller_id_use_case: GetAllItemsBySellerIdUseCase = Depends(
            provide_get_items_by_seller_id_stub),
):
    try:
        items = get_all_items_by_seller_id_use_case.execute(seller_id)
    except TypeError:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No items"
        )
    return items


@router.post(path="/")
async def create_item(
    category_id: str = Form(),
    title: str = Form(),
    description: str = Form(),
    condition: str = Form(),
    address: str = Form(),
    cost: str = Form(),
    item_status: str = Form(),
    picture: UploadFile = File(...),
    create_item_use_case: CreateItemUseCase = Depends(
        provide_create_item_stub),
    create_picture_use_case: CreatePictureUseCase = Depends(
        provide_create_picture_stub),
    create_picture_item_relation: CreatePictureItemRelationUseCase =
    Depends(provide_create_picture_item_relation_stub),
    jwt: str = Depends(JWTBearer()),
    get_access_token_by_jwt_use_case: GetAccessTokenByJwtUseCase = Depends(
        provide_get_access_token_by_jwt_stub
    ),
):
    try:
        seller_id = get_access_token_by_jwt_use_case.execute(jwt).user_id
        item_id = create_item_use_case.execute(item=ItemCreate(
            category_id=category_id,
            title=title,
            description=description,
            condition=condition,
            address=address,
            cost=cost,
            status=item_status,
            seller_id=seller_id,
        )).id
        if picture:
            picture_id = create_picture_use_case.execute(
                picture_create=PictureCreate(file=picture)
            ).id
            create_picture_item_relation.execute(
                obj=PictureItemRelation(
                    picture_id=picture_id,
                    item_id=item_id)
            )
        es_doc = {
            "category_id": category_id,
            "title": title,
            "description": description,
            "condition": condition,
            "address": address,
            "cost": cost,
            "status": item_status,
            "buyer_id": "null",
            "seller_id": seller_id,
        }
        await es.index(index="items", id=item_id, document=es_doc)
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(e)
        )
    return {
        "item_id": item_id
    }


@router.put(path='/{item_id}')
async def update_item(
    item_id: str,
    item: ItemUpdate,
    update_item_use_case: UpdateItemUseCase = Depends(provide_update_item_stub)
):
    item.seller_id = ObjectId(item.seller_id)
    item.buyer_id = ObjectId(item.buyer_id  )
    updated_item = update_item_use_case.execute(ItemUpdateWithId(
        id=item_id,
        item_update=item
    ))
    return updated_item


@router.delete(path='/{item_id}')
async def delete_item(
    item_id: str,
    delete_item_use_case: DeleteItemUseCase = Depends(
        provide_delete_item_stub),
    get_picture_items_relation_by_item_id_use_case:
    GetPictureItemRelationsByItemIdUseCase = Depends(
        provide_get_picture_item_relations_by_item_id_stub
    ),
    delete_picture_items_relation_use_case: DeletePictureItemRelationUseCase =
    Depends(provide_delete_picture_item_relation_stub)
):
    delete_item_use_case.execute(item_id=ItemId(id=item_id))
    relations = get_picture_items_relation_by_item_id_use_case.execute(
        PictureItemRelationItemId(item_id=item_id)
    )
    for relation in relations:
        delete_picture_items_relation_use_case.execute(
            PictureItemRelationId(id=relation.id)
        )
    return {
        "message": "Item deleted"
    }