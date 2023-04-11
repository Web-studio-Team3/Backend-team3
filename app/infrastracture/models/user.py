from pydantic import BaseModel


class UserModel(BaseModel):
    email: str
    hashed_password: str
    full_name: str
    date_of_birth: str
    picture_id: str
