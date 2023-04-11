from fastapi import APIRouter, Depends, status, HTTPException, UploadFile, File

from app.core.picture.usecases.create_picture import CreatePictureUseCase
from app.core.picture.usecases.get_picture_by_id import GetPictureByIdUseCase
from app.core.picture.usecases.delete_picture_by_id import DeletePictureByIDUseCase
from app.core.picture.dto.picture import PictureCreate, PictureId

from app.presentation.di import (
    provide_create_picture_stub, provide_get_picture_stub,
    provide_delete_picture_stub
)

router = APIRouter()


@router.post(path="/")
async def create(
        picture: UploadFile = File(...),
        create_picture_use_case: CreatePictureUseCase = Depends(
            provide_create_picture_stub
        )
):
    created_picture = create_picture_use_case.execute(PictureCreate(file=picture))
    return {
        "id": created_picture.id,
        "url": created_picture.picture_url
    }


@router.get(path="/{picture_id}")
async def get(
        picture_id: str,
        get_picture_by_id: GetPictureByIdUseCase = Depends(
            provide_get_picture_stub
        )
):
    return get_picture_by_id.execute(picture_id_obj=PictureId(
        id=picture_id
    ))


@router.delete(path="/{picture_id}")
async def delete(
        picture_id: str,
        delete_picture_by_id_use_case: DeletePictureByIDUseCase = Depends(
            provide_delete_picture_stub
        )
):
    return delete_picture_by_id_use_case.execute(picture_id_obj=PictureId(
        id=picture_id
    ))
