from fastapi import FastAPI
from functools import lru_cache

from routes.user import user_router
from routes.category import category_router
from routes.item import item_router
from routes.auth import auth_router
# from config.config import Settings

app = FastAPI()

# @lru_cache()
# def get_settings():
#     return Settings()

app.include_router(user_router)
app.include_router(category_router)
app.include_router(item_router)
app.include_router(auth_router)
