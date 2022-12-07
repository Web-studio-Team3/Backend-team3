from fastapi import APIRouter

from routes.user import user_router
from routes.category import category_router
from routes.item import item_router
from routes.photo_item_relation import relation_router

router = APIRouter()

router.include_router(user_router, prefix="/users", tags=["users"])
router.include_router(category_router, prefix="/categories", tags=["categories"])
router.include_router(item_router, prefix="/items", tags=["items"])
router.include_router(relation_router)
