from fastapi import APIRouter, Depends, status, HTTPException

from app.core.item.dto.item import (
    ItemId, ItemCreate, ItemUpdate, ItemUpdateWithId
)

from app.core.item.usecases.get_item_all import GetItemAllUseCase
from app.core.item.usecases.get_item_by_id import GetItemByIdUseCase
from app.core.item.usecases.create_item import CreateItemUseCase
from app.core.item.usecases.delete_item import DeleteItemUseCase
from app.core.item.usecases.update_item import UpdateItemUseCase

from app.presentation.di import (
    provide_get_items_stub,
    provide_get_item_by_id_stub,
    provide_create_item_stub,
    provide_delete_item_stub,
    provide_update_item_stub
)


router = APIRouter()


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
    get_item_by_id_use_case: GetItemByIdUseCase = Depends(provide_get_item_by_id_stub)
):
    try:
        item = get_item_by_id_use_case.execute(ItemId(id=item_id))
    except TypeError:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No item with such id"
        )
    return item


@router.post(path="/")
async def create_item(
    item: ItemCreate,
    create_item_use_case: CreateItemUseCase = Depends(provide_create_item_stub)
):
    try:
        create_item_use_case.execute(item=item)
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(e)
        )
    return {
        "message": "Item successfully created"
    }


@router.put(path='/{item_id}')
async def update_item(
    item_id: str,
    item: ItemUpdate,
    update_item_use_case: UpdateItemUseCase = Depends(provide_update_item_stub)
):
    updated_item = update_item_use_case.execute(ItemUpdateWithId(
        id=item_id,
        item_update=item
    ))
    return updated_item


@router.delete(path='/{item_id}')
async def delete_item(
    item_id: str,
    delete_item_use_case: DeleteItemUseCase = Depends(provide_delete_item_stub)
):
    delete_item_use_case.execute(item_id=ItemId(id=item_id))
    return {
        "message": "Item deleted"
    }