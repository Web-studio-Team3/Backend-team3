from dataclasses import dataclass

from fastapi import File, UploadFile
from pydantic import BaseModel


@dataclass
class PictureCreate:
    file: UploadFile = File(...)


class PictureId(BaseModel):
    id: str

    class Config:
        orm_mode = True
