from fastapi import APIRouter, Body, Form
from fastapi.encoders import jsonable_encoder
from bson import ObjectId

from models.user import UserModel
from config.db import db
from schemas.user import userEntity, usersEntity

user_router = APIRouter()

@user_router.get('/users/', tags=["users"])
async def find_all_users():
    return usersEntity(db.user.find())

@user_router.post('/users/', tags=["users"])
async def create_user(user: UserModel):
    userId = db.user.insert_one(user.dict(exclude_none=True)).inserted_id
    return userEntity(db.user.find_one({'_id': ObjectId(userId)}))

# @user_router.post('/users/', response_model=UserModel)
# async def create_user(user: UserModel = Body(...)):
#     db.user.insert_one(jsonable_encoder(user))
#     return usersEntity(db.user.find())

@user_router.get('/users/{user_id}', tags=["users"])
async def find_one_user(user_id):
    return userEntity(db.user.find_one({"_id": ObjectId(user_id)}))

@user_router.put('/users/{user_id}', tags=["users"])
async def update_user(user_id, user: UserModel):
    db.user.find_one_and_update({"_id": ObjectId(user_id)}, {
        "$set": dict(user)
    })
    return userEntity(db.user.find_one({"_id": ObjectId(user_id)}))

@user_router.delete('/users/{user_id}', tags=["users"])
async def delete_user(user_id):
    db.user.find_one_and_delete({'_id': ObjectId(user_id)})
    return usersEntity(db.user.find())
