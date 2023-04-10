from typing import Type, Callable
from pymongo.database import Database
from fastapi import Depends

from app.infrastructure.dao.base import BaseDao, Dao
from app.infrastructure.dao.item_write import ItemWriteDaoImpl
from app.infrastructure.dao.item_read import ItemReadDaoImpl

from app.core.item.usecases.get_item_all import GetItemAllUseCase
from app.core.item.usecases.get_item_by_id import GetItemByIdUseCase
from app.core.item.usecases.create_item import CreateItemUseCase
from app.core.item.usecases.delete_item import DeleteItemUseCase
from app.core.item.usecases.update_item import UpdateItemUseCase

from app.presentation.di.stubs import (
    provide_database_stub,
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