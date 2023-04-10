from fastapi import FastAPI

from app.infrastructure.connect import database

from app.presentation.di.stubs import (
    provide_database_stub,
    provide_get_items_stub,
    provide_get_item_by_id_stub,
    provide_create_item_stub,
    provide_delete_item_stub,
    provide_update_item_stub
)

from app.presentation.di.provides import (
    provide_get_items,
    provide_get_item_by_id,
    provide_create_item,
    provide_delete_item,
    provide_update_item
)

def setup_di(app: FastAPI):
    app.dependency_overrides.update({
        provide_database_stub: lambda: database
    })

    app.dependency_overrides.update({
        provide_get_items_stub: provide_get_items,
        provide_get_item_by_id_stub: provide_get_item_by_id,
        provide_create_item_stub: provide_create_item,
        provide_delete_item_stub: provide_delete_item,
        provide_update_item_stub: provide_update_item
    })