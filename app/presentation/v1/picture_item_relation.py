from fastapi import APIRouter, Depends

from app.core.picture_item_relation.dto.picture_item_relation import (
    PictureItemRelation,
    PictureItemRelationId,
    PictureItemRelationItemId
)
from app.core.picture_item_relation.usecases.create_picture_item_relation import CreatePictureItemRelationUseCase
from app.core.picture_item_relation.usecases.get_picture_item_relation_by_id import GetPictureItemRelationByIdUseCase
from app.core.picture_item_relation.usecases.get_picture_item_relations_by_item_id import GetPictureItemRelationsByItemIdUseCase
from app.core.picture_item_relation.usecases.delete_picture_item_relation import DeletePictureItemRelationUseCase
from app.core.picture_item_relation.usecases.update_picture_item_relation import UpdatePictureItemRelationUseCase

from app.core.sale_item.usecase.get_sale_item_relation_by_user_id import GetSaleItemRelationByUserIdUseCase
from app.core.sale_item.dto.sale_item_relation import SaleItemRelationUserId

from app.core.token.usecases.get_access_token_by_jwt import GetAccessTokenByJwtUseCase

from app.presentation.bearer import JWTBearer

from app.presentation.di import (
    provide_create_picture_item_relation_stub,
    provide_get_picture_item_relation_by_id_stub,
    provide_delete_picture_item_relation_stub,
    provide_update_picture_item_relation_stub,
    provide_get_picture_item_relations_by_item_id_stub,
    provide_get_access_token_by_jwt_stub,
    provide_get_sale_item_relation_by_user_id_stub,
)

router = APIRouter()


@router.post(path="/")
async def create(
    picture_item_relation: PictureItemRelation,
    picture_item_relation_create_use_case: CreatePictureItemRelationUseCase =
    Depends(provide_create_picture_item_relation_stub),
    jwt: str = Depends(JWTBearer()),
    get_access_token_by_jwt_use_case: GetAccessTokenByJwtUseCase = 
    Depends(provide_get_access_token_by_jwt_stub),
    get_sale_items_by_user_id_use_case: GetSaleItemRelationByUserIdUseCase =
    Depends(provide_get_sale_item_relation_by_user_id_stub),
):
    sale_item_relations = get_sale_items_by_user_id_use_case.execute(
        SaleItemRelationUserId(
            user_id=get_access_token_by_jwt_use_case.execute(jwt).user_id
        )
    )
    if (not any(
        sale_item_relation.item_id == picture_item_relation.item_id for sale_item_relation in sale_item_relations
    )):
        return {
            "message": "Not allowed for this user"
        }
    
    created_picture_item_relation = picture_item_relation_create_use_case.execute(
        picture_item_relation)
    return {
        "id":created_picture_item_relation.id,
        "picture_id":created_picture_item_relation.picture_id,
        "item_id":created_picture_item_relation.item_id,
    }


@router.get(path="/{picture_item_relation_id}")
async def get(
    picture_item_relation_id: str,
    get_picture_item_relation_use_case: GetPictureItemRelationByIdUseCase =
    Depends(provide_get_picture_item_relation_by_id_stub)
):
    picture_item_relation = get_picture_item_relation_use_case.execute(
        PictureItemRelationId(id=picture_item_relation_id)
    )
    return picture_item_relation


@router.get(path="/item/{item_id}")
async def get_by_item_id(
    item_id: str,
    get_picuture_item_relations_by_item_id_use_case: GetPictureItemRelationsByItemIdUseCase =
    Depends(provide_get_picture_item_relations_by_item_id_stub)
):
    relations = get_picuture_item_relations_by_item_id_use_case.execute(
        PictureItemRelationItemId(
            item_id=item_id
        )
    )
    return list(relations)


@router.put(path="/{picture_item_relation_id}")
async def update(
    picture_item_relation: PictureItemRelation,
    picture_item_relation_update_use_case: UpdatePictureItemRelationUseCase =
    Depends(provide_update_picture_item_relation_stub),
    jwt: str = Depends(JWTBearer()),
    get_access_token_by_jwt_use_case: GetAccessTokenByJwtUseCase = 
    Depends(provide_get_access_token_by_jwt_stub),
    get_sale_items_by_user_id_use_case: GetSaleItemRelationByUserIdUseCase =
    Depends(provide_get_sale_item_relation_by_user_id_stub),
):
    
    sale_item_relations = get_sale_items_by_user_id_use_case.execute(
        SaleItemRelationUserId(
            user_id=get_access_token_by_jwt_use_case.execute(jwt).user_id
        )
    )
    if (not any(
        sale_item_relation.item_id == picture_item_relation.item_id for sale_item_relation in sale_item_relations
    )):
        return {
            "message": "Not allowed for this user"
        }
    
    return picture_item_relation_update_use_case.execute(picture_item_relation)


@router.delete(path="/{picture_item_relation_id}")
async def delete(
    picture_item_relation_id: str,
    delete_picture_item_relation_use_case: DeletePictureItemRelationUseCase =
    Depends(provide_delete_picture_item_relation_stub),
    jwt: str = Depends(JWTBearer()),
    get_access_token_by_jwt_use_case: GetAccessTokenByJwtUseCase = 
    Depends(provide_get_access_token_by_jwt_stub),
    get_sale_items_by_user_id_use_case: GetSaleItemRelationByUserIdUseCase =
    Depends(provide_get_sale_item_relation_by_user_id_stub),
    get_picture_item_realtion_use_case: GetPictureItemRelationByIdUseCase =
    Depends(provide_get_picture_item_relation_by_id_stub)
):
    picture_item_relation = get_picture_item_realtion_use_case.execute(
        PictureItemRelationId(id=picture_item_relation_id)
    )
    sale_item_relations = get_sale_items_by_user_id_use_case.execute(
        SaleItemRelationUserId(
            user_id=get_access_token_by_jwt_use_case.execute(jwt).user_id
        )
    )
    if (not any(
        sale_item_relation.item_id == picture_item_relation.item_id for sale_item_relation in sale_item_relations
    )):
        return {
            "message": "Not allowed for this user"
        }
    
    delete_picture_item_relation_use_case.execute(
        PictureItemRelationId(id=picture_item_relation_id)
    )
    return {
        "message": "picture_item_relation was deleted"
    }
