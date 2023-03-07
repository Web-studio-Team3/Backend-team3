from ....shared.dto import BaseDto
from uuid import UUID


class PhotoItemRelation(BaseDto):
    photo_id: UUID
    item_id: UUID


class GetPhotoItemRelations(BaseDto):
    item_id: UUID


class GetPhotoItemRelation(BaseDto):
    relation_id: UUID


class DeletePhotoItemRelation(GetPhotoItemRelation):
    pass