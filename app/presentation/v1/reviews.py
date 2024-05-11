from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination import Page, paginate

from app.core.review.dto.review import (
    ReviewItemId,
    Review,
    CreateReviewRequest,
    ReviewUpdateWithId,
    ReviewUserId,
    ReviewUpdate,
    ReviewId
)
from app.core.user.dto.user import (
    UserId,
)
from app.core.review.entities.review import Review as ReviewDataClass

from app.core.token.usecases.get_access_token_by_jwt import GetAccessTokenByJwtUseCase
from app.presentation.bearer import JWTBearer
from app.presentation.di import (
    provide_get_reviews_by_item_id_stub,
    provide_get_access_token_by_jwt_stub,
    provide_create_review_stub,
    provide_get_user_by_id_stub,
    provide_get_reviews_by_user_id_stub,
    provide_update_review_stub,
    provide_delete_review_stub,
)
from app.core.user.usecases.get_user_by_id import GetUserByIdUseCase
from app.core.review.usecase.get_reviews_by_item_id import (
    GetReviewsByItemIdUseCase,
)
from app.core.review.usecase.create_review import (
    CreateReviewUseCase,
)
from app.core.review.usecase.get_reviews_by_user_id import (
    GetReviewsByUserIdUseCase,
)
from app.core.review.usecase.update_review import (
    UpdateReviewUseCase,
)
from app.core.review.usecase.delete_review import (
    DeleteReviewUseCase,
)

router = APIRouter()

@router.get(path="/{item_id}", response_model=Page[ReviewDataClass])
async def get_reviews_by_item_id(
    item_id: str,
    get_reviews_by_item_id_use_case: GetReviewsByItemIdUseCase = Depends(
        provide_get_reviews_by_item_id_stub
    ),
):
    reviews = get_reviews_by_item_id_use_case.execute(
        obj=ReviewItemId(item_id=item_id)
    )
    return paginate(list(reviews))


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
    get_reviews_by_user_id_use_case: GetReviewsByUserIdUseCase = Depends(
        provide_get_reviews_by_user_id_stub
    ),
):
    user_id = get_access_token_by_jwt_use_case.execute(jwt).user_id
    try:
        user = get_user_by_id_use_case.execute(UserId(id=user_id))
    except TypeError:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="no user with such id"
        )
    
    reviews = get_reviews_by_user_id_use_case.execute(
        obj=ReviewUserId(user_id=user_id)
    )
    if any(review.item_id == request.item_id for review in reviews):
        return {"chat message": "You have already reviewed this item"}
    
    review_id = create_review_use_case.execute(
        obj=Review(
            user_id=user_id, 
            item_id=request.item_id, 
            text=request.text, 
            full_name=user.full_name, 
            rating=request.rating
        )
    )
    return {"id": review_id}

@router.put(path='/{review_id}')
async def update_review(
    review_id: str,
    review: ReviewUpdate,
    update_review_use_case: UpdateReviewUseCase = Depends(provide_update_review_stub),
    jwt: str = Depends(JWTBearer()),
    get_access_token_by_jwt_use_case: GetAccessTokenByJwtUseCase = Depends(
        provide_get_access_token_by_jwt_stub
    ),
    get_reviews_by_user_id_use_case: GetReviewsByUserIdUseCase = Depends(
        provide_get_reviews_by_user_id_stub
    ),
):
    user_id = get_access_token_by_jwt_use_case.execute(jwt).user_id
    
    reviews = get_reviews_by_user_id_use_case.execute(
        obj=ReviewUserId(user_id=user_id)
    )

    if not any(review.id == review_id for review in reviews):
        return {"chat message": "You can only update reviews that you created"}
    
    updated_item = update_review_use_case.execute(ReviewUpdateWithId(
        id=review_id,
        review_update=review
    ))
    return updated_item


@router.delete(path="/{review_id}")
async def delete_review(
    review_id: str,
    delete_review_use_case: DeleteReviewUseCase = Depends(
        provide_delete_review_stub
    ),
    jwt: str = Depends(JWTBearer()),
    get_access_token_by_jwt_use_case: GetAccessTokenByJwtUseCase = Depends(
        provide_get_access_token_by_jwt_stub
    ),
    get_reviews_by_user_id_use_case: GetReviewsByUserIdUseCase = Depends(
        provide_get_reviews_by_user_id_stub
    ),
):
    user_id = get_access_token_by_jwt_use_case.execute(jwt).user_id
    
    reviews = get_reviews_by_user_id_use_case.execute(
        obj=ReviewUserId(user_id=user_id)
    )

    if not any(review.id == review_id for review in reviews):
        return {"chat message": "You can only delete reviews that you created"}
    
    delete_review_use_case.execute(review_id=ReviewId(id=review_id))
    return {"chat_message": "Review deleted"}
