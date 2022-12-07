from pydantic import BaseModel, EmailStr, Field
from bson import ObjectId
from typing import Optional
from datetime import datetime, date


class UserModel(BaseModel):
    # id: str
    email: Optional[EmailStr] = Field(...)
    password: Optional[str] = Field(...)
    fullname: Optional[str] = Field(...)
    date_of_birth: Optional[datetime] = None
    photo_url: Optional[str] = Field(...)

    class Config:
        # allow_population_by_field_name = True
        # arbitrary_types_allowed = True
        # json_encoders = {
            # ObjectId: str,
        # }
        schema_extra = {
            "example": {
                "email": "jdoedaaads@gmail.com",
                "password": "31321231244",
                "fullname": "Jane Doe",
                "date_of_birth": datetime.utcnow(),
                "photo_url": "some_photo_url",
            }
        }