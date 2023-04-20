from typing import Type, Callable
from pymongo.database import Database
from fastapi import Depends

from app.infrastracture.dao.base import BaseDao, Dao
from app.infrastracture.dao.user_write import UserWriteDaoImpl
from app.infrastracture.dao.token_read import TokenReadDaoImpl
from app.infrastracture.dao.user_read import UserReadDaoImpl
from app.infrastracture.dao.token_write import TokenWriteDaoImpl
from app.infrastracture.dao.picture_write import PictureWriteImpl
from app.infrastracture.dao.picture_read import PictureReadImpl

from app.core.user.dao.password_hasher import PasswordHasher
from app.core.user.usecases.sign_up import SignUpUseCase
from app.core.user.usecases.sign_in import SignInUseCase
from app.core.user.usecases.get_user_by_id import GetUserByIdUseCase
from app.core.user.usecases.get_user_by_email import GetUserByEmailUseCase
from app.core.user.usecases.logout import LogoutUseCase
from app.core.user.usecases.update_user import UpdateUserUseCase
from app.core.user.usecases.delete_user import DeleteUserUseCase
from app.core.user.usecases.password_hasher import PasswordHasherImp

from app.core.token.usecases.create_token import CreateTokenUseCase
from app.core.token.usecases.encode_token import EncodeToken
from app.core.token.usecases.decode_token import DecodeToken
from app.core.token.usecases.delete_token_by_user_id import DeleteTokenByUserIdUseCase
from app.core.token.dao.token_coder import TokenCoder

from app.core.picture.usecases.create_picture import CreatePictureUseCase
from app.core.picture.usecases.get_picture_by_id import GetPictureByIdUseCase
from app.core.picture.usecases.delete_picture_by_id import DeletePictureByIDUseCase
from app.core.picture.usecases.delete_picture_by_user_id import DeletePictureByUserIDUseCase
from app.core.picture.picture_helper import PictureHelper

from app.infrastructure.dao.item_write import ItemWriteDaoImpl
from app.infrastructure.dao.item_read import ItemReadDaoImpl

from app.core.item.usecases.get_item_all import GetItemAllUseCase
from app.core.item.usecases.get_item_by_id import GetItemByIdUseCase
from app.core.item.usecases.create_item import CreateItemUseCase
from app.core.item.usecases.delete_item import DeleteItemUseCase
from app.core.item.usecases.update_item import UpdateItemUseCase

from app.presentation.di.stubs import (
    provide_database_stub,
    provide_create_token_stub,
    provide_password_hasher_stub,
    provide_token_encoder_stub,
    provide_delete_token_by_user_id_stub,
    provide_create_picture_stub
)


def get_pymongo_dao(
        dao_type: Type[Dao]
) -> Callable[[Database], Dao]:
    def _get_dao(
            database: Database = Depends(provide_database_stub)
    ) -> Dao:
        return dao_type(database)

    return _get_dao


def provide_sign_up(
        dao: BaseDao = Depends(
            get_pymongo_dao(UserWriteDaoImpl)
        ),
        password_hasher: PasswordHasher = Depends(
            provide_password_hasher_stub
        )
) -> SignUpUseCase:
    return SignUpUseCase(dao, password_hasher)


def provide_sign_in(
        token_read_dao: BaseDao = Depends(
            get_pymongo_dao(TokenReadDaoImpl)
        ),
        create_token_use_case: CreateTokenUseCase = Depends(
            provide_create_token_stub
        ),
        user_read_dao: BaseDao = Depends(
            get_pymongo_dao(UserReadDaoImpl)
        ),
        password_hasher: PasswordHasher = Depends(
            provide_password_hasher_stub
        ),
) -> SignInUseCase:
    return SignInUseCase(
        token_read_dao=token_read_dao,
        create_token_use_case=create_token_use_case,
        user_read_dao=user_read_dao,
        password_hasher=password_hasher
    )


def provide_get_user_by_id(
        dao: BaseDao = Depends(
            get_pymongo_dao(UserReadDaoImpl)
        )
) -> GetUserByIdUseCase:
    return GetUserByIdUseCase(dao)


def provide_create_token(
        token_write_dao: BaseDao = Depends(
            get_pymongo_dao(TokenWriteDaoImpl)
        ),
        token_coder: TokenCoder = Depends(provide_token_encoder_stub)
) -> CreateTokenUseCase:
    return CreateTokenUseCase(dao=token_write_dao, token_coder=token_coder)


def provide_delete_token_by_user_id(
        token_write_dao: BaseDao = Depends(
            get_pymongo_dao(TokenWriteDaoImpl)
        )
) -> DeleteTokenByUserIdUseCase:
    return DeleteTokenByUserIdUseCase(token_write_dao=token_write_dao)


def provide_logout(
        delete_token_use_case: DeleteTokenByUserIdUseCase
        = Depends(provide_delete_token_by_user_id_stub)
) -> LogoutUseCase:
    return LogoutUseCase(delete_token_use_case=delete_token_use_case)


def provide_get_user_by_email(
        dao: BaseDao = Depends(
            get_pymongo_dao(UserReadDaoImpl)
        )
) -> GetUserByEmailUseCase:
    return GetUserByEmailUseCase(dao)


def provide_password_hasher() -> PasswordHasherImp:
    return PasswordHasherImp()


def provide_token_encoder() -> EncodeToken:
    return EncodeToken()


def provide_token_decoder() -> DecodeToken:
    return DecodeToken()


def provide_update_user(
        user_write_dao: BaseDao = Depends(
            get_pymongo_dao(UserWriteDaoImpl)
        ),
        user_read_dao: BaseDao = Depends(
            get_pymongo_dao(UserReadDaoImpl)
        ),
        password_hasher: PasswordHasher = Depends(provide_password_hasher_stub)
) -> UpdateUserUseCase:
    return UpdateUserUseCase(
        user_write_dao=user_write_dao,
        user_read_dao=user_read_dao,
        password_hasher=password_hasher
    )


def provide_delete_user(
        user_write_dao: BaseDao = Depends(
            get_pymongo_dao(UserWriteDaoImpl)
        ),
        delete_token_by_user_id_use_case: DeleteTokenByUserIdUseCase =
        Depends(provide_delete_token_by_user_id_stub)
) -> DeleteUserUseCase:
    return DeleteUserUseCase(
        user_write_dao=user_write_dao,
        delete_token_by_user_id_use_case=delete_token_by_user_id_use_case
    )


def provide_create_picture(
        picture_write_dao: BaseDao = Depends(
            get_pymongo_dao(PictureWriteImpl)
        )
) -> CreatePictureUseCase:
    return CreatePictureUseCase(
        write_dao=picture_write_dao,
        picture_helper=PictureHelper()
    )


def provide_get_picture(
        picture_read_dao: BaseDao = Depends(
            get_pymongo_dao(PictureReadImpl)
        )
) -> GetPictureByIdUseCase:
    return GetPictureByIdUseCase(
        read_dao=picture_read_dao
    )


def provide_delete_picture(
        picture_write_dao: BaseDao = Depends(
            get_pymongo_dao(PictureWriteImpl)
        ),
        picture_read_dao: BaseDao = Depends(
            get_pymongo_dao(PictureReadImpl)
        )
) -> DeletePictureByIDUseCase:
    return DeletePictureByIDUseCase(
        write_dao=picture_write_dao,
        read_dao=picture_read_dao,
        picture_helper=PictureHelper()
    )


def provide_delete_picture_by_user_id(
        get_user_by_id_use_case: BaseDao = Depends(provide_get_user_by_id),
        delete_picture_use_case: BaseDao = Depends(provide_delete_picture)
) -> DeletePictureByUserIDUseCase:
    return DeletePictureByUserIDUseCase(
        get_user_by_id_use_case=get_user_by_id_use_case,
        delete_picture_use_case=delete_picture_use_case
    )

def get_pymongo_dao(
    dao_type: Type[Dao]
) -> Callable[[Database], Dao]:
    def _get_dao(
        database: Database = Depends(provide_database_stub)
    ) -> Dao:
        return dao_type(database)
    
    return _get_dao


def provide_get_items(
    dao: BaseDao = Depends(
        get_pymongo_dao(ItemReadDaoImpl)
    )
) -> GetItemAllUseCase:
    return GetItemAllUseCase(dao)


def provide_get_item_by_id(
    dao: BaseDao = Depends(
        get_pymongo_dao(ItemReadDaoImpl)
    )
) -> GetItemByIdUseCase:
    return GetItemByIdUseCase(dao)


def provide_create_item(
    dao: BaseDao = Depends(
        get_pymongo_dao(ItemWriteDaoImpl)
    )
) -> CreateItemUseCase:
    return CreateItemUseCase(dao)


def provide_update_item(
    item_write_dao: BaseDao = Depends(
        get_pymongo_dao(ItemWriteDaoImpl)
    ),
    item_read_dao: BaseDao = Depends(
        get_pymongo_dao(ItemReadDaoImpl)
    )
) -> UpdateItemUseCase:
    return UpdateItemUseCase(
        item_write_dao=item_write_dao,
        item_read_dao=item_read_dao
    )


def provide_delete_item(
    item_write_dao: BaseDao = Depends(
        get_pymongo_dao(ItemWriteDaoImpl)
    ),
) -> DeleteItemUseCase:
    return DeleteItemUseCase(
        item_write_dao=item_write_dao
    )