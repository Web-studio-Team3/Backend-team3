from fastapi import APIRouter
from app.presentation.v1 import user
from app.presentation.v1 import picture

router = APIRouter(prefix="/api")
router.include_router(user.router, prefix="/users", tags=["users"])
router.include_router(picture.router, prefix="/picture", tags=["pictures"])
