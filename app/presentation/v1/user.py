from fastapi import APIRouter, Depends, status, HTTPException, UploadFile, File, Form
from typing import Optional

from app.core.user.dto.user import (
    UserSignUpRaw, UserSignIn, UserId, UserUpdate, UserUpdateWithId
)
from app.core.user.usecases.sign_up import SignUpUseCase
from app.core.user.usecases.sign_in import SignInUseCase
from app.core.user.usecases.get_user_by_id import GetUserByIdUseCase
from app.core.user.usecases.logout import LogoutUseCase
from app.core.user.usecases.update_user import UpdateUserUseCase
from app.core.user.usecases.delete_user import DeleteUserUseCase

from app.core.user.exceptions.user import AuthError

from app.core.picture.usecases.create_picture import CreatePictureUseCase
from app.core.picture.dto.picture import PictureCreate, PictureId
from app.core.picture.usecases.delete_picture_by_id import DeletePictureByIDUseCase
from app.core.picture.usecases.delete_picture_by_user_id import DeletePictureByUserIDUseCase

from app.presentation.bearer import JWTBearer
from app.presentation.di import (
    provide_sign_up_stub,
    provide_sign_in_stub,
    provide_get_user_by_id_stub,
    provide_logout_stub,
    provide_update_user_stub,
    provide_delete_user_stub,
    provide_create_picture_stub,
    provide_delete_picture_stub,
    provide_delete_picture_by_user_id_stub
)

router = APIRouter()


@router.post(path="/sign_up")
async def sign_up(
        email: str = Form(),
        raw_password: str = Form(),
        full_name: str = Form(),
        date_of_birth: str = Form(),
        # user: UserSignUpRaw,
        picture: UploadFile = File(...),
        sign_up_use_case: SignUpUseCase = Depends(provide_sign_up_stub),
        create_picture_use_case: CreatePictureUseCase =
        Depends(provide_create_picture_stub)
):
    try:
        # user.picture_url = create_picture_use_case.execute(
        #     PictureCreate(file=picture)
        # )
        sign_up_use_case.execute(user=UserSignUpRaw(
            email=email,
            raw_password=raw_password,
            full_name=full_name,
            date_of_birth=date_of_birth,
            picture_id=create_picture_use_case.execute(
                PictureCreate(file=picture)
            ).id
        ))
    except AuthError as e:
        return HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(e)
        )
    return {
        "message": "user successfully created"
    }


@router.post(path="/sign_in")
async def sign_in(
        user: UserSignIn,
        sign_in_use_case: SignInUseCase = Depends(provide_sign_in_stub)
):
    try:
        access_token = sign_in_use_case.execute(user=user)
    except AuthError as e:
        return HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(e)
        )
    return {
        "user_id": access_token.user_id,
        "jwt_token": access_token.jwt_token
    }


@router.get(path="/{user_id}", dependencies=[Depends(JWTBearer())])
async def get_user_by_id(
        user_id: str,
        get_user_by_id_use_case: GetUserByIdUseCase = Depends(provide_get_user_by_id_stub)
):
    try:
        user = get_user_by_id_use_case.execute(UserId(id=user_id))
    except TypeError:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="no user with such id"
        )
    return user


@router.post(path="/logout/{user_id}", dependencies=[Depends(JWTBearer())])
async def logout(
        user_id: str,
        logout_use_case: LogoutUseCase = Depends(provide_logout_stub)
):
    logout_use_case.execute(UserId(id=user_id))
    return {
        "message": "success"
    }


@router.put(path="/{user_id}", dependencies=[Depends(JWTBearer())])
async def update(
        user_id: str,
        email: Optional[str] = Form(None),
        password: Optional[str] = Form(None),
        full_name: Optional[str] = Form(None),
        date_of_birth: Optional[str] = Form(None),
        picture: Optional[UploadFile] = File(None),
        update_user_use_case: UpdateUserUseCase = Depends(provide_update_user_stub),
        delete_picture_by_user_id_use_case: DeletePictureByUserIDUseCase =
        Depends(provide_delete_picture_by_user_id_stub),
        create_picture_use_case: CreatePictureUseCase =
        Depends(provide_create_picture_stub)
):
    if picture:
        delete_picture_by_user_id_use_case.execute(
            user_id_obj=UserId(id=user_id)
        )
    updated_user = update_user_use_case.execute(UserUpdateWithId(
        id=user_id,
        user_update=UserUpdate(
            email=email,
            password=password,
            full_name=full_name,
            date_of_birth=date_of_birth,
            picture_id=create_picture_use_case.execute(
                PictureCreate(file=picture)
            ).id
        )
    ))
    return updated_user


@router.delete(path="/{user_id}", dependencies=[Depends(JWTBearer())])
async def delete(
        user_id: str,
        delete_user_use_case: DeleteUserUseCase = Depends(provide_delete_user_stub),
        delete_picture_by_user_id_use_case: DeletePictureByUserIDUseCase =
        Depends(provide_delete_picture_by_user_id_stub)
):
    delete_user_use_case.execute(user_id=UserId(id=user_id))
    delete_picture_by_user_id_use_case.execute(user_id_obj=UserId(id=user_id))
    return {
        "message": "user was deleted"
    }
