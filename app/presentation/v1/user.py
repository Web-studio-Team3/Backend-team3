from fastapi import APIRouter, Depends, status, HTTPException

from app.core.user.dto.user import UserSignUpRaw, UserSignIn, UserId
from app.core.user.usecases.sign_up import SignUpUseCase
from app.core.user.usecases.sign_in import SignInUseCase
from app.core.user.usecases.get_user_by_id import GetUserByIdUseCase
from app.core.user.exceptions.user import AuthError

from app.presentation.bearer import JWTBearer
from app.presentation.di import (
    provide_sign_up_stub,
    provide_sign_in_stub,
    provide_get_user_by_id_stub
)

router = APIRouter()


@router.post(path="/sign_up")
async def sign_up(
        user: UserSignUpRaw,
        sign_up_use_case: SignUpUseCase = Depends(provide_sign_up_stub)
):
    try:
        sign_up_use_case.execute(user=user)
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


@router.get(path="", dependencies=[Depends(JWTBearer())])
async def get_user_by_id(
        user_id: UserId,
        get_user_by_id_use_case: GetUserByIdUseCase = Depends(provide_get_user_by_id_stub)
):
    try:
        user = get_user_by_id_use_case.execute(user_id)
    except TypeError:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="no user with such id"
        )
    return user
