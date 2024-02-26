from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile, status

from app.core.category.dto.category import (
    CategoryCreate,
    CategoryId,
    CategoryUpdate,
    CategoryUpdateWithId,
)
from app.core.category.usecases.create_category import CreateCategoryUseCase
from app.core.category.usecases.delete_category import DeleteCategoryUseCase
from app.core.category.usecases.get_category_all import GetCategoryAllUseCase
from app.core.category.usecases.get_category_by_id import GetCategoryByIdUseCase
from app.core.category.usecases.update_category import UpdateCategoryUseCase
from app.presentation.di import (
    provide_create_category_stub,
    provide_delete_category_stub,
    provide_get_categories_stub,
    provide_get_category_by_id_stub,
    provide_update_category_stub,
)

router = APIRouter()


@router.get(path="/")
async def get_category_all(
    get_category_all_use_case: GetCategoryAllUseCase = Depends(
        provide_get_categories_stub
    ),
):
    try:
        categories = get_category_all_use_case.execute()
    except TypeError:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="No categories"
        )
    return categories


@router.get(path="/{category_id}")
async def get_category_by_id(
    category_id: str,
    get_category_by_id_use_case: GetCategoryByIdUseCase = Depends(
        provide_get_category_by_id_stub
    ),
):
    try:
        category = get_category_by_id_use_case.execute(CategoryId(id=category_id))
    except TypeError:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="No category with such id"
        )
    return {
        "id": category.id,
        "title": category.title,
        "childs": category.childs,
    }


@router.post(path="/")
async def create_category(
    title: str = Form(),
    childs: list = Form(),
    create_category_use_case: CreateCategoryUseCase = Depends(
        provide_create_category_stub
    ),
):
    try:
        category_id = create_category_use_case.execute(
            category=CategoryCreate(title=title, childs=childs)
        ).id
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e)
        )
    return {"category_id": category_id}


@router.put(path="/{category_id}")
async def update_category(
    category_id: str,
    category: CategoryUpdate,
    update_category_use_case: UpdateCategoryUseCase = Depends(
        provide_update_category_stub
    ),
):
    updated_category = update_category_use_case.execute(
        CategoryUpdateWithId(id=category_id, category_update=category)
    )
    return updated_category


@router.delete(path="/{category_id}")
async def delete_category(
    category_id: str,
    delete_category_use_case: DeleteCategoryUseCase = Depends(
        provide_delete_category_stub
    ),
):
    delete_category_use_case.execute(category_id=CategoryId(id=category_id))
    return {"chat_message": "Category deleted"}
