from shared.dto import BaseDto
from uuid import UUID


class UserItemTrackingRelation(BaseDto):
    user_id: UUID
    item_id: UUID


class UserItemTrackingRelationId(BaseDto):
    relation_id: UUID


class UserItemTrackingRelationDelete(UserItemTrackingRelationId):
    pass


class GetUserItemTrackingRelations(BaseDto):
    user_id: UUID
