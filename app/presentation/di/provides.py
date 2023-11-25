from typing import Callable, Type

from fastapi import Depends
from pymongo.database import Database

from app.core.category.usecases.create_category import CreateCategoryUseCase
from app.core.category.usecases.delete_category import DeleteCategoryUseCase
from app.core.category.usecases.get_category_all import GetCategoryAllUseCase
from app.core.category.usecases.get_category_by_id import GetCategoryByIdUseCase
from app.core.category.usecases.update_category import UpdateCategoryUseCase

from app.infrastracture.dao.picture_item_relation_write import PictureItemRelationWriteImpl
from app.infrastracture.dao.picture_item_relation_read import PictureItemRelationReadImpl

from app.core.picture_item_relation.usecases.create_picture_item_relation import CreatePictureItemRelationUseCase
from app.core.picture_item_relation.usecases.delete_picture_item_relation import DeletePictureItemRelationUseCase
from app.core.picture_item_relation.usecases.get_picture_item_relations_by_item_id import GetPictureItemRelationsByItemIdUseCase
from app.core.picture_item_relation.usecases.get_picture_item_relation_by_id import GetPictureItemRelationByIdUseCase
from app.core.picture_item_relation.usecases.update_picture_item_relation import UpdatePictureItemRelationUseCase

from app.core.sale_item.usecase.create_sale_item_relation import CreateSaleItemRelationUseCase
from app.core.sale_item.usecase.delete_sale_item_relation import DeleteSaleItemRelationUseCase
from app.core.sale_item.usecase.get_sale_item_relation_by_id import GetSaleItemRelationByIdUseCase
from app.core.sale_item.usecase.get_sale_item_relation_by_item_id import GetSaleItemRelationByItemIdUseCase
from app.core.sale_item.usecase.get_sale_item_relation_by_user_id import GetSaleItemRelationByUserIdUseCase
from app.core.sale_item.usecase.delete_sale_item_relation_by_item_id import DeleteSaleItemRelationByItemIdUseCase
from app.infrastracture.dao.sale_item.sale_item_write import SaleItemRelationWriteImpl
from app.infrastracture.dao.sale_item.sale_item_read import SaleItemRelationReadImpl

from app.infrastracture.dao.sold_item.sold_item_write import SoldItemRelationWriteImpl
from app.infrastracture.dao.sold_item.sold_item_read import SoldItemRelationReadImpl
from app.core.sold_item.usecase.create_sold_item_relation import CreateSoldItemRelationUseCase
from app.core.sold_item.usecase.delete_sold_item_relation import DeleteSoldItemRelationUseCase
from app.core.sold_item.usecase.get_sold_item_relation_by_buyer_id import GetSoldItemRelationByBuyerIdUseCase
from app.core.sold_item.usecase.get_sold_item_relation_by_id import GetSoldItemRelationByIdUseCase
from app.core.sold_item.usecase.get_sold_item_relation_by_item_id import GetSoldItemRelationByItemIdUseCase
from app.core.sold_item.usecase.get_sold_item_relation_by_seller_id import GetSoldItemRelationBySellerIdUseCase
from app.core.sold_item.usecase.delete_sold_item_relation_by_item_id import DeleteSoldItemRelationByItemIdUseCase

from app.infrastracture.dao.favourite.favourite_read import FavouriteReadImpl
from app.infrastracture.dao.favourite.favourite_write import FavouriteWriteImpl
from app.core.favourites.usecase.create_favourite import CreateFavouriteUseCase
from app.core.favourites.usecase.delete_favourite import DeleteFavouriteUseCase
from app.core.favourites.usecase.get_favourite_by_id import GetFavouriteByIdUseCase
from app.core.favourites.usecase.get_favourites_count_by_item_id import GetFavouritesCountByItemIdUseCase
from app.core.favourites.usecase.get_favourites_by_user_id import GetFavouritesByUserIdUseCase
from app.core.favourites.usecase.delete_favourites_by_item_id import DeleteFavouritesByItemIdUseCase

from app.infrastracture.dao.chat_write import ChatWriteDaoImpl
from app.infrastracture.dao.chat_read import ChatReadDaoImpl
from app.core.chat.usecase.get_chat_by_id import GetChatByIdUseCase
from app.core.chat.usecase.create_chat import CreateChatUseCase
from app.core.chat.usecase.delete_chat import DeleteChatUseCase

from app.infrastracture.dao.message_write import MessageWriteDaoImpl
from app.infrastracture.dao.message_read import MessageReadDaoImpl
from app.core.chat_message.usecase.get_all_messages import GetAllMesagesUseCase
from app.core.chat_message.usecase.add_message import AddMessageUseCase
from app.core.chat_message.usecase.delete_message import DeleteMessageUseCase
from app.core.chat_message.usecase.delete_all_messages import DeleteAllMessagesUseCase



from app.core.chat.usecase.create_chat import CreateChatUseCase
from app.core.chat.usecase.delete_chat import DeleteChatUseCase
from app.core.chat.usecase.get_chat_by_id import GetChatByIdUseCase
from app.core.chat_message.usecase.add_message import AddMessageUseCase
from app.core.chat_message.usecase.delete_all_messages import DeleteAllMessagesUseCase
from app.core.chat_message.usecase.delete_message import DeleteMessageUseCase
from app.core.chat_message.usecase.get_all_messages import GetAllMessagesUseCase
from app.core.favourites.usecase.create_favourite import CreateFavouriteUseCase
from app.core.favourites.usecase.delete_favourite import DeleteFavouriteUseCase
from app.core.favourites.usecase.delete_favourites_by_item_id import (
    DeleteFavouritesByItemIdUseCase,
)
from app.core.favourites.usecase.get_favourite_by_id import GetFavouriteByIdUseCase
from app.core.favourites.usecase.get_favourites_by_user_id import (
    GetFavouritesByUserIdUseCase,
)
from app.core.favourites.usecase.get_favourites_count_by_item_id import (
    GetFavouritesCountByItemIdUseCase,
)
from app.core.item.usecases.create_item import CreateItemUseCase
from app.core.item.usecases.delete_item import DeleteItemUseCase
from app.core.item.usecases.get_item_all import GetItemAllUseCase
from app.core.item.usecases.get_item_by_id import GetItemByIdUseCase
from app.core.item.usecases.update_item import UpdateItemUseCase
from app.core.picture.picture_helper import PictureHelper
from app.core.picture.usecases.create_picture import CreatePictureUseCase
from app.core.picture.usecases.delete_picture_by_id import DeletePictureByIDUseCase
from app.core.picture.usecases.delete_picture_by_user_id import (
    DeletePictureByUserIDUseCase,
)
from app.core.picture.usecases.get_picture_by_id import GetPictureByIdUseCase
from app.core.picture_item_relation.usecases.create_picture_item_relation import (
    CreatePictureItemRelationUseCase,
)
from app.core.picture_item_relation.usecases.delete_picture_item_relation import (
    DeletePictureItemRelationUseCase,
)
from app.core.picture_item_relation.usecases.get_picture_item_relation_by_id import (
    GetPictureItemRelationByIdUseCase,
)
from app.core.picture_item_relation.usecases.get_picture_item_relations_by_item_id import (
    GetPictureItemRelationsByItemIdUseCase,
)
from app.core.picture_item_relation.usecases.update_picture_item_relation import (
    UpdatePictureItemRelationUseCase,
)
from app.core.sale_item.usecase.create_sale_item_relation import (
    CreateSaleItemRelationUseCase,
)
from app.core.sale_item.usecase.delete_sale_item_relation import (
    DeleteSaleItemRelationUseCase,
)
from app.core.sale_item.usecase.delete_sale_item_relation_by_item_id import (
    DeleteSaleItemRelationByItemIdUseCase,
)
from app.core.sale_item.usecase.get_sale_item_relation_by_id import (
    GetSaleItemRelationByIdUseCase,
)
from app.core.sale_item.usecase.get_sale_item_relation_by_item_id import (
    GetSaleItemRelationByItemIdUseCase,
)
from app.core.sale_item.usecase.get_sale_item_relation_by_user_id import (
    GetSaleItemRelationByUserIdUseCase,
)
from app.core.sold_item.usecase.create_sold_item_relation import (
    CreateSoldItemRelationUseCase,
)
from app.core.sold_item.usecase.delete_sold_item_relation import (
    DeleteSoldItemRelationUseCase,
)
from app.core.sold_item.usecase.delete_sold_item_relation_by_item_id import (
    DeleteSoldItemRelationByItemIdUseCase,
)
from app.core.sold_item.usecase.get_sold_item_relation_by_buyer_id import (
    GetSoldItemRelationByBuyerIdUseCase,
)
from app.core.sold_item.usecase.get_sold_item_relation_by_id import (
    GetSoldItemRelationByIdUseCase,
)
from app.core.sold_item.usecase.get_sold_item_relation_by_item_id import (
    GetSoldItemRelationByItemIdUseCase,
)
from app.core.sold_item.usecase.get_sold_item_relation_by_seller_id import (
    GetSoldItemRelationBySellerIdUseCase,
)
from app.core.token.dao.token_coder import TokenCoder
from app.core.token.usecases.create_token import CreateTokenUseCase
from app.core.token.usecases.decode_token import DecodeToken
from app.core.token.usecases.delete_token_by_user_id import DeleteTokenByUserIdUseCase
from app.core.token.usecases.encode_token import EncodeToken
from app.core.token.usecases.get_access_token_by_jwt import GetAccessTokenByJwtUseCase
from app.core.user.dao.password_hasher import PasswordHasher
from app.core.user.usecases.delete_user import DeleteUserUseCase
from app.core.user.usecases.get_user_by_email import GetUserByEmailUseCase
from app.core.user.usecases.get_user_by_id import GetUserByIdUseCase
from app.core.user.usecases.logout import LogoutUseCase
from app.core.user.usecases.password_hasher import PasswordHasherImp
from app.core.user.usecases.sign_in import SignInUseCase
from app.core.user.usecases.sign_up import SignUpUseCase
from app.core.user.usecases.update_user import UpdateUserUseCase
from app.infrastracture.dao.base import BaseDao, Dao
from app.infrastracture.dao.category_read import CategoryReadDaoImpl
from app.infrastracture.dao.category_write import CategoryWriteDaoImpl
from app.infrastracture.dao.chat_read import ChatReadDaoImpl
from app.infrastracture.dao.chat_write import ChatWriteDaoImpl
from app.infrastracture.dao.favourite.favourite_read import FavouriteReadImpl
from app.infrastracture.dao.favourite.favourite_write import FavouriteWriteImpl
from app.infrastracture.dao.item_read import ItemReadDaoImpl
from app.infrastracture.dao.item_write import ItemWriteDaoImpl
from app.infrastracture.dao.message_read import MessageReadDaoImpl
from app.infrastracture.dao.message_write import MessageWriteDaoImpl
from app.infrastracture.dao.picture_item_relation_read import (
    PictureItemRelationReadImpl,
)
from app.infrastracture.dao.picture_item_relation_write import (
    PictureItemRelationWriteImpl,
)
from app.infrastracture.dao.picture_read import PictureReadImpl
from app.infrastracture.dao.picture_write import PictureWriteImpl
from app.infrastracture.dao.sale_item.sale_item_read import SaleItemRelationReadImpl
from app.infrastracture.dao.sale_item.sale_item_write import SaleItemRelationWriteImpl
from app.infrastracture.dao.sold_item.sold_item_read import SoldItemRelationReadImpl
from app.infrastracture.dao.sold_item.sold_item_write import SoldItemRelationWriteImpl
from app.infrastracture.dao.token_read import TokenReadDaoImpl
from app.infrastracture.dao.token_write import TokenWriteDaoImpl
from app.infrastracture.dao.user_read import UserReadDaoImpl
from app.infrastracture.dao.user_write import UserWriteDaoImpl
from app.presentation.di.stubs import (
    provide_create_picture_stub,
    provide_create_token_stub,
    provide_database_stub,
    provide_delete_token_by_user_id_stub,
    provide_password_hasher_stub,
    provide_token_encoder_stub,
)


def get_pymongo_dao(dao_type: Type[Dao]) -> Callable[[Database], Dao]:
    def _get_dao(database: Database = Depends(provide_database_stub)) -> Dao:
        return dao_type(database)

    return _get_dao


def provide_sign_up(
    dao: BaseDao = Depends(get_pymongo_dao(UserWriteDaoImpl)),
    password_hasher: PasswordHasher = Depends(provide_password_hasher_stub),
) -> SignUpUseCase:
    return SignUpUseCase(dao, password_hasher)


def provide_sign_in(
    token_read_dao: BaseDao = Depends(get_pymongo_dao(TokenReadDaoImpl)),
    create_token_use_case: CreateTokenUseCase = Depends(provide_create_token_stub),
    user_read_dao: BaseDao = Depends(get_pymongo_dao(UserReadDaoImpl)),
    password_hasher: PasswordHasher = Depends(provide_password_hasher_stub),
) -> SignInUseCase:
    return SignInUseCase(
        token_read_dao=token_read_dao,
        create_token_use_case=create_token_use_case,
        user_read_dao=user_read_dao,
        password_hasher=password_hasher,
    )


def provide_get_user_by_id(
    dao: BaseDao = Depends(get_pymongo_dao(UserReadDaoImpl)),
) -> GetUserByIdUseCase:
    return GetUserByIdUseCase(dao)


def provide_create_token(
    token_write_dao: BaseDao = Depends(get_pymongo_dao(TokenWriteDaoImpl)),
    token_coder: TokenCoder = Depends(provide_token_encoder_stub),
) -> CreateTokenUseCase:
    return CreateTokenUseCase(dao=token_write_dao, token_coder=token_coder)


def provide_delete_token_by_user_id(
    token_write_dao: BaseDao = Depends(get_pymongo_dao(TokenWriteDaoImpl)),
) -> DeleteTokenByUserIdUseCase:
    return DeleteTokenByUserIdUseCase(token_write_dao=token_write_dao)


def provide_logout(
    delete_token_use_case: DeleteTokenByUserIdUseCase = Depends(
        provide_delete_token_by_user_id_stub
    ),
) -> LogoutUseCase:
    return LogoutUseCase(delete_token_use_case=delete_token_use_case)


def provide_get_user_by_email(
    dao: BaseDao = Depends(get_pymongo_dao(UserReadDaoImpl)),
) -> GetUserByEmailUseCase:
    return GetUserByEmailUseCase(dao)


def provide_password_hasher() -> PasswordHasherImp:
    return PasswordHasherImp()


def provide_token_encoder() -> EncodeToken:
    return EncodeToken()


def provide_token_decoder() -> DecodeToken:
    return DecodeToken()


def provide_update_user(
    user_write_dao: BaseDao = Depends(get_pymongo_dao(UserWriteDaoImpl)),
    user_read_dao: BaseDao = Depends(get_pymongo_dao(UserReadDaoImpl)),
    password_hasher: PasswordHasher = Depends(provide_password_hasher_stub),
) -> UpdateUserUseCase:
    return UpdateUserUseCase(
        user_write_dao=user_write_dao,
        user_read_dao=user_read_dao,
        password_hasher=password_hasher,
    )


def provide_delete_user(
    user_write_dao: BaseDao = Depends(get_pymongo_dao(UserWriteDaoImpl)),
    delete_token_by_user_id_use_case: DeleteTokenByUserIdUseCase = Depends(
        provide_delete_token_by_user_id_stub
    ),
) -> DeleteUserUseCase:
    return DeleteUserUseCase(
        user_write_dao=user_write_dao,
        delete_token_by_user_id_use_case=delete_token_by_user_id_use_case,
    )


def provide_create_picture(
    picture_write_dao: BaseDao = Depends(get_pymongo_dao(PictureWriteImpl)),
) -> CreatePictureUseCase:
    return CreatePictureUseCase(
        write_dao=picture_write_dao, picture_helper=PictureHelper()
    )


def provide_get_picture(
    picture_read_dao: BaseDao = Depends(get_pymongo_dao(PictureReadImpl)),
) -> GetPictureByIdUseCase:
    return GetPictureByIdUseCase(read_dao=picture_read_dao)


def provide_delete_picture(
    picture_write_dao: BaseDao = Depends(get_pymongo_dao(PictureWriteImpl)),
    picture_read_dao: BaseDao = Depends(get_pymongo_dao(PictureReadImpl)),
) -> DeletePictureByIDUseCase:
    return DeletePictureByIDUseCase(
        write_dao=picture_write_dao,
        read_dao=picture_read_dao,
        picture_helper=PictureHelper(),
    )


def provide_delete_picture_by_user_id(
    get_user_by_id_use_case: BaseDao = Depends(provide_get_user_by_id),
    delete_picture_use_case: BaseDao = Depends(provide_delete_picture),
) -> DeletePictureByUserIDUseCase:
    return DeletePictureByUserIDUseCase(
        get_user_by_id_use_case=get_user_by_id_use_case,
        delete_picture_use_case=delete_picture_use_case,
    )


def get_pymongo_dao(dao_type: Type[Dao]) -> Callable[[Database], Dao]:
    def _get_dao(database: Database = Depends(provide_database_stub)) -> Dao:
        return dao_type(database)

    return _get_dao


def provide_get_items(
    dao: BaseDao = Depends(get_pymongo_dao(ItemReadDaoImpl)),
) -> GetItemAllUseCase:
    return GetItemAllUseCase(dao)


def provide_get_item_by_id(
    dao: BaseDao = Depends(get_pymongo_dao(ItemReadDaoImpl)),
) -> GetItemByIdUseCase:
    return GetItemByIdUseCase(dao)


def provide_create_item(
    dao: BaseDao = Depends(get_pymongo_dao(ItemWriteDaoImpl)),
) -> CreateItemUseCase:
    return CreateItemUseCase(dao)


def provide_update_item(
    item_write_dao: BaseDao = Depends(get_pymongo_dao(ItemWriteDaoImpl)),
    item_read_dao: BaseDao = Depends(get_pymongo_dao(ItemReadDaoImpl)),
) -> UpdateItemUseCase:
    return UpdateItemUseCase(item_write_dao=item_write_dao, item_read_dao=item_read_dao)


def provide_delete_item(
    item_write_dao: BaseDao = Depends(get_pymongo_dao(ItemWriteDaoImpl)),
) -> DeleteItemUseCase:
    return DeleteItemUseCase(item_write_dao=item_write_dao)


def provide_get_categories(
    dao: BaseDao = Depends(get_pymongo_dao(CategoryReadDaoImpl)),
) -> GetCategoryAllUseCase:
    return GetCategoryAllUseCase(dao)


def provide_get_category_by_id(
    dao: BaseDao = Depends(get_pymongo_dao(CategoryReadDaoImpl)),
) -> GetCategoryByIdUseCase:
    return GetCategoryByIdUseCase(dao)


def provide_create_category(
    dao: BaseDao = Depends(get_pymongo_dao(CategoryWriteDaoImpl)),
) -> CreateCategoryUseCase:
    return CreateCategoryUseCase(dao)


def provide_update_category(
    category_write_dao: BaseDao = Depends(get_pymongo_dao(CategoryWriteDaoImpl)),
    category_read_dao: BaseDao = Depends(get_pymongo_dao(CategoryReadDaoImpl)),
) -> UpdateCategoryUseCase:
    return UpdateCategoryUseCase(
        category_write_dao=category_write_dao, category_read_dao=category_read_dao
    )


def provide_delete_category(
    category_write_dao: BaseDao = Depends(get_pymongo_dao(CategoryWriteDaoImpl)),
) -> DeleteCategoryUseCase:
    return DeleteCategoryUseCase(category_write_dao=category_write_dao)


def provide_create_picture_item_relation(
    picture_item_relation_write_dao: BaseDao = Depends(
        get_pymongo_dao(PictureItemRelationWriteImpl)
    ),
) -> CreatePictureItemRelationUseCase:
    return CreatePictureItemRelationUseCase(write_dao=picture_item_relation_write_dao)


def provide_delete_picture_item_relation(
    picture_item_relation_write_dao: BaseDao = Depends(
        get_pymongo_dao(PictureItemRelationWriteImpl)
    ),
) -> DeletePictureItemRelationUseCase:
    return DeletePictureItemRelationUseCase(write_dao=picture_item_relation_write_dao)


def provide_get_picture_item_relations_by_item_id(
    picture_item_relation_read_dao: BaseDao = Depends(
        get_pymongo_dao(PictureItemRelationReadImpl)
    ),
) -> GetPictureItemRelationsByItemIdUseCase:
    return GetPictureItemRelationsByItemIdUseCase(
        read_dao=picture_item_relation_read_dao
    )


def provide_get_picture_item_relation_by_id(
    picture_item_relation_read_dao: BaseDao = Depends(
        get_pymongo_dao(PictureItemRelationReadImpl)
    ),
) -> GetPictureItemRelationByIdUseCase:
    return GetPictureItemRelationByIdUseCase(read_dao=picture_item_relation_read_dao)


def provide_update_picture_item_relation(
    picute_item_relation_write_dao: BaseDao = Depends(
        get_pymongo_dao(PictureItemRelationWriteImpl)
    ),
) -> UpdatePictureItemRelationUseCase:
    return UpdatePictureItemRelationUseCase(write_dao=picute_item_relation_write_dao)


def provide_create_sale_item_relation(
    sale_item_relation_write_dao: BaseDao = Depends(
        get_pymongo_dao(SaleItemRelationWriteImpl)
    ),
) -> CreateSaleItemRelationUseCase:
    return CreateSaleItemRelationUseCase(write_dao=sale_item_relation_write_dao)


def provide_delete_sale_item_relation(
    sale_item_relation_write_dao: BaseDao = Depends(
        get_pymongo_dao(SaleItemRelationWriteImpl)
    ),
) -> DeleteSaleItemRelationUseCase:
    return DeleteSaleItemRelationUseCase(write_dao=sale_item_relation_write_dao)


def provide_get_sale_item_relation_by_id(
    sale_item_relation_read_dao: BaseDao = Depends(
        get_pymongo_dao(SaleItemRelationReadImpl)
    ),
) -> GetSaleItemRelationByIdUseCase:
    return GetSaleItemRelationByIdUseCase(read_dao=sale_item_relation_read_dao)


def provide_get_sale_item_relation_by_item_id(
    sale_item_relation_read_dao: BaseDao = Depends(
        get_pymongo_dao(SaleItemRelationReadImpl)
    ),
) -> GetSaleItemRelationByItemIdUseCase:
    return GetSaleItemRelationByItemIdUseCase(read_dao=sale_item_relation_read_dao)


def provide_get_sale_item_relation_by_user_id(
    sale_item_relation_read_dao: BaseDao = Depends(
        get_pymongo_dao(SaleItemRelationReadImpl)
    ),
) -> GetSaleItemRelationByUserIdUseCase:
    return GetSaleItemRelationByUserIdUseCase(read_dao=sale_item_relation_read_dao)


def provide_create_sold_item_relation(
    sold_item_relation_write_dao: BaseDao = Depends(
        get_pymongo_dao(SoldItemRelationWriteImpl)
    ),
) -> CreateSoldItemRelationUseCase:
    return CreateSoldItemRelationUseCase(write_dao=sold_item_relation_write_dao)


def provide_delete_sold_item_relation(
    sold_item_relation_write_dao: BaseDao = Depends(
        get_pymongo_dao(SoldItemRelationWriteImpl)
    ),
) -> DeleteSoldItemRelationUseCase:
    return DeleteSoldItemRelationUseCase(write_dao=sold_item_relation_write_dao)


def provide_get_sold_item_relation_by_id(
    sold_item_relation_read_dao: BaseDao = Depends(
        get_pymongo_dao(SoldItemRelationReadImpl)
    ),
) -> GetSoldItemRelationByIdUseCase:
    return GetSoldItemRelationByIdUseCase(read_dao=sold_item_relation_read_dao)


def provide_get_sold_item_relation_by_buyer_id(
    sold_item_relation_read_dao: BaseDao = Depends(
        get_pymongo_dao(SoldItemRelationReadImpl)
    ),
) -> GetSoldItemRelationByBuyerIdUseCase:
    return GetSoldItemRelationByBuyerIdUseCase(read_dao=sold_item_relation_read_dao)


def provide_get_sold_item_relation_by_item_id(
    sold_item_relation_read_dao: BaseDao = Depends(
        get_pymongo_dao(SoldItemRelationReadImpl)
    ),
) -> GetSoldItemRelationByItemIdUseCase:
    return GetSoldItemRelationByItemIdUseCase(read_dao=sold_item_relation_read_dao)


def provide_get_sold_item_relation_by_seller_id(
    sold_item_relation_read_dao: BaseDao = Depends(
        get_pymongo_dao(SoldItemRelationReadImpl)
    ),
) -> GetSoldItemRelationBySellerIdUseCase:
    return GetSoldItemRelationBySellerIdUseCase(read_dao=sold_item_relation_read_dao)


def provide_create_favourite(
    favourite_write_dao: BaseDao = Depends(get_pymongo_dao(FavouriteWriteImpl)),
) -> CreateFavouriteUseCase:
    return CreateFavouriteUseCase(write_dao=favourite_write_dao)


def provide_delete_favourite(
    favourite_write_dao: BaseDao = Depends(get_pymongo_dao(FavouriteWriteImpl)),
) -> DeleteFavouriteUseCase:
    return DeleteFavouriteUseCase(write_dao=favourite_write_dao)


def provide_get_favourite_by_id(
    favourite_read_dao: BaseDao = Depends(get_pymongo_dao(FavouriteReadImpl)),
) -> GetFavouriteByIdUseCase:
    return GetFavouriteByIdUseCase(read_dao=favourite_read_dao)


def provide_get_favourites_count_by_item_id(
    favourite_read_dao: BaseDao = Depends(get_pymongo_dao(FavouriteReadImpl)),
) -> GetFavouritesCountByItemIdUseCase:
    return GetFavouritesCountByItemIdUseCase(read_dao=favourite_read_dao)


def provide_get_favourites_by_user_id(
    favourite_read_dao: BaseDao = Depends(get_pymongo_dao(FavouriteReadImpl)),
) -> GetFavouritesByUserIdUseCase:
    return GetFavouritesByUserIdUseCase(read_dao=favourite_read_dao)


def provide_get_access_token_by_jwt(
    token_read_dao: BaseDao = Depends(get_pymongo_dao(TokenReadDaoImpl)),
) -> GetAccessTokenByJwtUseCase:
    return GetAccessTokenByJwtUseCase(dao=token_read_dao)


def provide_delete_sale_item_relation_by_item_id(
    sale_item_write_dao: BaseDao = Depends(get_pymongo_dao(SaleItemRelationWriteImpl)),
) -> DeleteSaleItemRelationByItemIdUseCase:
    return DeleteSaleItemRelationByItemIdUseCase(write_dao=sale_item_write_dao)


def provide_delete_favourites_by_item_id(
    favourite_write_dao: BaseDao = Depends(get_pymongo_dao(FavouriteWriteImpl)),
    favourite_read_dao: BaseDao = Depends(get_pymongo_dao(FavouriteReadImpl)),
) -> DeleteFavouritesByItemIdUseCase:
    return DeleteFavouritesByItemIdUseCase(
        write_dao=favourite_write_dao, read_dao=favourite_read_dao
    )


def provide_delete_sold_item_relation_by_item_id(
    favourite_write_dao: BaseDao = Depends(get_pymongo_dao(SoldItemRelationWriteImpl)),
    favourite_read_dao: BaseDao = Depends(get_pymongo_dao(SoldItemRelationReadImpl)),
) -> DeleteSoldItemRelationByItemIdUseCase:
    return DeleteSoldItemRelationByItemIdUseCase(
        write_dao=favourite_write_dao, read_dao=favourite_read_dao
    )


def provide_create_chat(
    chat_write_dao: BaseDao = Depends(get_pymongo_dao(ChatWriteDaoImpl)),
) -> CreateChatUseCase:
    return CreateChatUseCase(write_dao=chat_write_dao)


def provide_get_chat_by_id(
    chat_read_dao: BaseDao = Depends(get_pymongo_dao(ChatReadDaoImpl)),
) -> GetChatByIdUseCase:
    return GetChatByIdUseCase(read_dao=chat_read_dao)


def provide_delete_chat(
    chat_write_dao: BaseDao = Depends(get_pymongo_dao(ChatWriteDaoImpl)),
) -> DeleteChatUseCase:
    return DeleteChatUseCase(write_dao=chat_write_dao)


def provide_add_message(
    message_write_dao: BaseDao = Depends(get_pymongo_dao(MessageWriteDaoImpl)),
) -> AddMessageUseCase:
    return AddMessageUseCase(write_dao=message_write_dao)


def provide_delete_message(
    message_write_dao: BaseDao = Depends(get_pymongo_dao(MessageWriteDaoImpl)),
) -> DeleteMessageUseCase:
    return DeleteMessageUseCase(write_dao=message_write_dao)


def provide_delete_all_messages(
    message_write_dao: BaseDao = Depends(get_pymongo_dao(MessageWriteDaoImpl)),
) -> DeleteAllMessagesUseCase:
    return DeleteAllMessagesUseCase(write_dao=message_write_dao)


def provide_get_all_messages(
    message_read_dao: BaseDao = Depends(get_pymongo_dao(MessageReadDaoImpl)),
) -> GetAllMessagesUseCase:
    return GetAllMessagesUseCase(read_dao=message_read_dao)

