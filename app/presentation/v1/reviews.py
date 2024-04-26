from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination import Page, paginate

from app.core.review.dto.review import (
    ReviewItemId,
    Review,
    CreateReviewRequest,
)
from app.core.user.dto.user import (
    UserId,
)

from app.core.token.usecases.get_access_token_by_jwt import GetAccessTokenByJwtUseCase
from app.presentation.bearer import JWTBearer
from app.presentation.di import (
    provide_get_reviews_by_item_id_stub,
    provide_get_access_token_by_jwt_stub,
    provide_create_review_stub,
    provide_get_user_by_id_stub,
)
from app.core.user.usecases.get_user_by_id import GetUserByIdUseCase
from app.core.review.usecase.get_reviews_by_item_id import (
    GetReviewsByItemIdUseCase,
)
from app.core.review.usecase.create_review import (
    CreateReviewUseCase,
)

router = APIRouter()

@router.get(path="/{item_id}")
async def get_reviews_by_item_id(
    item_id: str,
    get_reviews_by_item_id_use_case: GetReviewsByItemIdUseCase = Depends(
        provide_get_reviews_by_item_id_stub
    ),
):
    reviews = get_reviews_by_item_id_use_case.execute(
        obj=ReviewItemId(item_id=item_id)
    )
    return reviews


@router.post(path="/")
async def create(
    request: CreateReviewRequest,
    create_review_use_case: CreateReviewUseCase = Depends(
        provide_create_review_stub
    ),
    jwt: str = Depends(JWTBearer()),
    get_access_token_by_jwt_use_case: GetAccessTokenByJwtUseCase = Depends(
        provide_get_access_token_by_jwt_stub
    ),
    get_user_by_id_use_case: GetUserByIdUseCase = Depends(
        provide_get_user_by_id_stub
    ),
):
    user_id = get_access_token_by_jwt_use_case.execute(jwt).user_id
    try:
        user = get_user_by_id_use_case.execute(UserId(id=user_id))
    except TypeError:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="no user with such id"
        )
    review_id = create_review_use_case.execute(
        obj=Review(user_id=user_id, item_id=request.item_id, text=request.text, full_name=user.full_name)
    )
    return {"id": review_id.id}