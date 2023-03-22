from fastapi import APIRouter
from app.presentation.v1 import user

router = APIRouter(prefix="/api")
router.include_router(user.router, prefix="/users", tags=["users"])
