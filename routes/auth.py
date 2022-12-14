from fastapi import APIRouter, HTTPException, status, Depends
from bson import ObjectId, objectid
from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm
# from dotenv import load_dotenv
import os

from auth.jwt import create_access_token, authenticate_user, get_current_active_user
from models.auth import Token, UserModel
from config.db import db

auth_router = APIRouter(tags=["auth"])

# load_dotenv()
# SECRET_KEY = os.environ.get("SECRET_KEY")
# ALGORITHM = os.environ.get("ALGORITHM")
# ACCESS_TOKEN_EXPIRE_MINUTES = os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES")
SECRET_KEY = "50ca754d2e10c0c894e7f4d962b05adb6d59afe048b0efd7d02af8843eb2fba1"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

@auth_router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    print(ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM)
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@auth_router.get("/users/me/", response_model=UserModel)
async def read_users_me(current_user: UserModel = Depends(get_current_active_user)):
    return current_user
