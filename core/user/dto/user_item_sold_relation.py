from shared.dto import BaseDto
from uuid import UUID


class UserItemSoldRelation(BaseDto):
    user_id: UUID
    item_id: UUID


class UserItemSoldRelationId(BaseDto):
    relation_id: UUID


class UserItemSoldRelationDelete(UserItemSoldRelationId):
    pass


class GetUserItemSoldRelations(BaseDto):
    user_id: UUID
