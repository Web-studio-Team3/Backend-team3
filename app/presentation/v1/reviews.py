from fastapi import APIRouter, Depends
from fastapi_pagination import Page, paginate

from app.core.review.dto.review import (
    ReviewItemId,
)

from app.core.token.usecases.get_access_token_by_jwt import GetAccessTokenByJwtUseCase
from app.presentation.bearer import JWTBearer
from app.presentation.di import (
    provide_get_reviews_by_item_id_stub,
)
from app.core.review.usecase.get_reviews_by_item_id import (
    GetReviewsByItemIdUseCase,
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
