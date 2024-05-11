from fastapi import APIRouter

from app.presentation.v1 import (
    categories,
    chat,
    items,
    picture,
    picture_item_relation,
    sale_item_relation,
    sold_item_relation,
    favourite,
    search,
    user,
    cart,
    reviews,
)

router = APIRouter(prefix="/api")
router.include_router(user.router, prefix="/users", tags=["users"])
router.include_router(picture.router, prefix="/pictures", tags=["pictures"])
router.include_router(items.router, prefix='/items', tags=["items"])
router.include_router(categories.router, prefix='/categories', tags=["categories"])
router.include_router(picture_item_relation.router,
                      prefix="/picture_item_relations", tags=["picture_item_relations"])
router.include_router(sale_item_relation.router,
                      prefix="/sale_item_relations", tags=["sale_item_relations"])
router.include_router(sold_item_relation.router,
                      prefix="/sold_item_relations", tags=["sold_item_relations"])
router.include_router(favourite.router, prefix="/favourites", tags=["favourites"])
#router.include_router(search.router, prefix="/search", tags=["search"])
router.include_router(cart.router, prefix="/cart", tags=["cart"])
router.include_router(reviews.router, prefix="/reviews", tags=["review"])

router.include_router(
    picture_item_relation.router,
    prefix="/picture_item_relations",
    tags=["picture_item_relations"],
)
router.include_router(
    sale_item_relation.router,
    prefix="/sale_item_relations",
    tags=["sale_item_relations"],
)
router.include_router(
    sold_item_relation.router,
    prefix="/sold_item_relations",
    tags=["sold_item_relations"],
)
router.include_router(favourite.router, prefix="/favourites", tags=["favourites"])
router.include_router(chat.router, prefix="/chat", tags=["chat"])

