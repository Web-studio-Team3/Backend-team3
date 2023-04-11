from pydantic import BaseModel
from fastapi import File, UploadFile
from dataclasses import dataclass


@dataclass
class PictureCreate:
    file: UploadFile = File(...)


class PictureId(BaseModel):
    id: str

    class Config:
        orm_mode = True
