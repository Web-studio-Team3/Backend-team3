from fastapi import Form, APIRouter, UploadFile, File
from bson import ObjectId
from app.core.picture.picture_helper import save_picture, delete_picture

from models.user import UserModel
from config.db import db
from schemas.user import userEntity, usersEntity

user_router = APIRouter()


@user_router.get('/')
async def find_all_users():
    return usersEntity(db.user.find())


@user_router.post('/')
async def create_user(
        email: str = Form(),
        password: str = Form(),
        fullname: str = Form(),
        date_of_birth: str = Form(),
        photo: UploadFile = File(...)):
    photo_url = save_picture(file=photo)
    user = UserModel(
        email=email,
        password=password,
        fullname=fullname,
        date_of_birth=date_of_birth,
        photo_url=photo_url
    )
    userId = db.user.insert_one(user.dict(exclude_none=True)).inserted_id
    return userEntity(db.user.find_one({'_id': ObjectId(userId)}))


# @user_router.post('/users/', response_model=UserModel)
# async def create_user(user: UserModel = Body(...)):
#     db.user.insert_one(jsonable_encoder(user))
#     return usersEntity(db.user.find())

@user_router.get('/{user_id}')
async def find_one_user(user_id):
    return userEntity(db.user.find_one({"_id": ObjectId(user_id)}))


@user_router.put('/{user_id}')
async def update_user(user_id, user: UserModel):
    db.user.find_one_and_update({"_id": ObjectId(user_id)}, {
        "$set": dict(user)
    })
    return userEntity(db.user.find_one({"_id": ObjectId(user_id)}))


@user_router.put("/{user_id}/update_photo")
async def update_photo(user_id: str, photo: UploadFile = File(...)):
    user = userEntity(db.user.find_one({"_id": ObjectId(user_id)}))
    delete_picture(user.get("photo_url"))
    new_photo_url = save_picture(photo)
    user.update({
        "photo_url": new_photo_url
    })
    db.user.find_one_and_update(
        {"_id": ObjectId(user_id)},
        {"$set": dict(user)}
    )
    return userEntity(db.user.find_one({"_id": ObjectId(user_id)}))


@user_router.delete('/{user_id}')
async def delete_user(user_id):
    user = userEntity(db.user.find_one_and_delete({'_id': ObjectId(user_id)}))
    delete_picture(user.get("photo_url"))
    return usersEntity(db.user.find())
