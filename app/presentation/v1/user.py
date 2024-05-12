from typing import Optional

from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile, status
from fastapi.responses import JSONResponse
from app.core.picture.dto.picture import PictureCreate
from app.core.picture.usecases.create_picture import CreatePictureUseCase
from app.core.picture.usecases.delete_picture_by_user_id import (
    DeletePictureByUserIDUseCase,
)
from app.core.token.usecases.get_access_token_by_jwt import GetAccessTokenByJwtUseCase
from app.core.user.dto.user import (
    UserId,
    UserSignIn,
    UserSignUpRaw,
    UserUpdate,
    UserUpdateWithId,
)
from app.core.user.exceptions.user import AuthError
from app.core.user.usecases.delete_user import DeleteUserUseCase
from app.core.user.usecases.get_user_by_id import GetUserByIdUseCase
from app.core.user.usecases.logout import LogoutUseCase
from app.core.user.usecases.sign_in import SignInUseCase
from app.core.user.usecases.sign_up import SignUpUseCase
from app.core.user.usecases.update_user import UpdateUserUseCase
from app.presentation.bearer import JWTBearer
from app.presentation.di import (
    provide_create_picture_stub,
    provide_delete_picture_by_user_id_stub,
    provide_delete_user_stub,
    provide_get_access_token_by_jwt_stub,
    provide_get_user_by_id_stub,
    provide_logout_stub,
    provide_sign_in_stub,
    provide_sign_up_stub,
    provide_update_user_stub,
)

router = APIRouter()


@router.post(path="/sign_up")
async def sign_up(
    email: str = Form(),
    raw_password: str = Form(),
    full_name: str = Form(),
    date_of_birth: str = Form(),
    picture: UploadFile = File(...),
    telegram_id: Optional[int] = Form(None),
    telegram_username: Optional[str] = Form(None),
    sign_up_use_case: SignUpUseCase = Depends(provide_sign_up_stub),
    create_picture_use_case: CreatePictureUseCase = Depends(
        provide_create_picture_stub
    ),
):
    try:
        sign_up_use_case.execute(
            user=UserSignUpRaw(
                email=email,
                raw_password=raw_password,
                full_name=full_name,
                date_of_birth=date_of_birth,
                picture_id=create_picture_use_case.execute(
                    PictureCreate(file=picture)
                ).id,
                telegram_id=telegram_id,
                telegram_username=telegram_username,
            )
        )
    except AuthError as e:
        return JSONResponse(content={"message": str(e)}, status_code=404)
    return {"chat_message": "user successfully created"}


@router.post(path="/sign_in")
async def sign_in(
    user: UserSignIn, sign_in_use_case: SignInUseCase = Depends(provide_sign_in_stub)
):
    try:
        access_token = sign_in_use_case.execute(user=user)
    except AuthError as e:
        return JSONResponse(content={"message": str(e)}, status_code=422)
    return {"user_id": access_token.user_id, "jwt_token": access_token.jwt_token}


@router.get(path="/self/")
async def get_self_user_info(
    get_user_by_id_use_case: GetUserByIdUseCase = Depends(provide_get_user_by_id_stub),
    jwt: str = Depends(JWTBearer()),
    get_access_token_by_jwt_use_case: GetAccessTokenByJwtUseCase = Depends(
        provide_get_access_token_by_jwt_stub
    ),
):
    user_id = get_access_token_by_jwt_use_case.execute(jwt).user_id
    try:
        user = get_user_by_id_use_case.execute(UserId(id=user_id))
    except TypeError:
        return HTTPException(
            status_code=400, detail="no user with such id"
        )
    return user


@router.get(path="/info/{user_id}")
async def get_user_info(
    user_id: str,
    get_user_by_id_use_case: GetUserByIdUseCase = Depends(provide_get_user_by_id_stub),
):
    try:
        user = get_user_by_id_use_case.execute(UserId(id=user_id))
    except AuthError as e:
        return JSONResponse(content={"message": str(e)}, status_code=404)
    return {
        "id": user.id,
        "full_name": user.full_name,
        "email": user.email,
        "date_of_birth": user.date_of_birth,
        "picture_id": user.picture_id,
        "telegram_id": user.telegram_id,
        "telegram_username": user.telegram_username,
    }


@router.post(path="/logout/")
async def logout(
    logout_use_case: LogoutUseCase = Depends(provide_logout_stub),
    jwt: str = Depends(JWTBearer()),
    get_access_token_by_jwt_use_case: GetAccessTokenByJwtUseCase = Depends(
        provide_get_access_token_by_jwt_stub
    ),
):
    user_id = get_access_token_by_jwt_use_case.execute(jwt).user_id
    logout_use_case.execute(UserId(id=user_id))
    return {"message": "success"}


@router.put(path="/info/")
async def update_user_info(
    email: Optional[str] = Form(None),
    password: Optional[str] = Form(None),
    full_name: Optional[str] = Form(None),
    date_of_birth: Optional[str] = Form(None),
    picture: Optional[UploadFile] = File(None),
    telegram_id: Optional[int] = Form(None),
    telegram_username: Optional[str] = Form(None),
    update_user_use_case: UpdateUserUseCase = Depends(provide_update_user_stub),
    jwt: str = Depends(JWTBearer()),
    get_access_token_by_jwt_use_case: GetAccessTokenByJwtUseCase = Depends(
        provide_get_access_token_by_jwt_stub
    ),
    delete_picture_by_user_id_use_case: DeletePictureByUserIDUseCase = Depends(
        provide_delete_picture_by_user_id_stub
    ),
    create_picture_use_case: CreatePictureUseCase = Depends(
        provide_create_picture_stub
    ),
):
    user_id = get_access_token_by_jwt_use_case.execute(jwt).user_id

    picture_id = None
    if picture != None:
        delete_picture_by_user_id_use_case.execute(user_id_obj=UserId(id=user_id))
        picture_id = create_picture_use_case.execute(
            picture_create=PictureCreate(file=picture)
        ).id

    updated_user = update_user_use_case.execute(
        UserUpdateWithId(
            id=user_id,
            user_update=UserUpdate(
                email=email,
                password=password,
                full_name=full_name,
                date_of_birth=date_of_birth,
                picture_id=picture_id,
                telegram_id=telegram_id,
                telegram_username=telegram_username,
            ),
        )
    )
    return updated_user


@router.delete(path="/", dependencies=[Depends(JWTBearer())])
async def delete(
    delete_user_use_case: DeleteUserUseCase = Depends(provide_delete_user_stub),
    delete_picture_by_user_id_use_case: DeletePictureByUserIDUseCase = Depends(
        provide_delete_picture_by_user_id_stub
    ),
    jwt: str = Depends(JWTBearer()),
    get_access_token_by_jwt_use_case: GetAccessTokenByJwtUseCase = Depends(
        provide_get_access_token_by_jwt_stub
    ),
):
    user_id = get_access_token_by_jwt_use_case.execute(jwt).user_id

    delete_user_use_case.execute(user_id=UserId(id=user_id))
    delete_picture_by_user_id_use_case.execute(user_id_obj=UserId(id=user_id))
    return {"message": "user was deleted"}
