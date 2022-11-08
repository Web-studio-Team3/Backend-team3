from fastapi import FastAPI

from routes.user import user_router
from routes.category import category_router

app = FastAPI()

app.include_router(user_router)
app.include_router(category_router)








# from typing import Union, List, Optional
# import datetime
# from datetime import date, datetime

# from fastapi import FastAPI
# from fastapi import APIRouter, Body, status
# from fastapi.encoders import jsonable_encoder
# from fastapi.responses import Response, JSONResponse
# from pydantic import BaseModel, Field, EmailStr

# import motor.motor_asyncio
# from bson.objectid import ObjectId

# app = FastAPI()

# MONGO_DETAILS = "mongodb://localhost:27017"

# client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

# db = client.baraholka

# class PyObjectId(ObjectId):
#     @classmethod
#     def __get_validators__(cls):
#         yield cls.validate

#     @classmethod
#     def validate(cls, v):
#         if not ObjectId.is_valid(v):
#             raise ValueError("Invalid objectid")
#         return ObjectId(v)

#     @classmethod
#     def __modify_schema__(cls, field_schema):
#         field_schema.update(type="string")


# class UserModel(BaseModel):
#     id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
#     email: EmailStr = Field(...)
#     password: str = Field(...)
#     fullname: str = Field(...)
#     date_of_birth: datetime = Field(...)

#     class Config:
#         allow_population_by_field_name = True
#         arbitrary_types_allowed = True
#         json_encoders = {
#             ObjectId: str,
#         }
#         schema_extra = {
#             "example": {
#                 "email": "jdoedaaads@gmail.com",
#                 "password": "31321231244",
#                 "fullname": "Jane Doe",
#                 "date_of_birth": datetime.utcnow(),
#             }
#         }


# @app.post("/", response_description="Add new user", response_model=UserModel)
# async def create_user(user: UserModel = Body(...)):
#     user = jsonable_encoder(user)
#     new_user = await db["user"].insert_one(user)
#     created_user = await db["user"].find_one({"_id": new_user.inserted_id})
#     return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_user)

# @app.get("/", response_description="List all users", response_model=List[UserModel])
# async def list_users():
#     users = await db["user"].find().to_list(1000)
#     return users


# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: Union[bool, None] = None

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name  , "item_id": item_id}
