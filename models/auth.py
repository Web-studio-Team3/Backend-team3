from pydantic import BaseModel, EmailStr, Field
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from bson import ObjectId
from typing import Optional, Union, Any
from datetime import datetime, date, timedelta

from .user import UserModel


# class Login(BaseModel):
#     email: str
#     password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None


class UserInDBModel(UserModel):
    hashed_password: str

# password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# def get_hashed_password(password: str) -> str:
#     return password_context.hash(password)


# def verify_password(password: str, hashed_pass: str) -> bool:
#     return password_context.verify(password, hashed_pass)