from fastapi import FastAPI

from app.infrastracture.connect import database

from app.presentation.di.stubs import (
    provide_database_stub,
    provide_sign_up_stub,
    provide_sign_in_stub,
    provide_get_user_by_id_stub,
    provide_create_token_stub,
    provide_get_user_by_email_stub,
    provide_password_hasher_stub,
    provide_token_decoder_stub,
    provide_token_encoder_stub,
    provide_logout_stub,
    provide_delete_token_by_user_id_stub,
    provide_delete_user_stub,
    provide_update_user_stub,
    provide_create_picture_stub,
    provide_get_picture_stub,
    provide_delete_picture_by_user_id_stub,
    provide_delete_picture_stub,
    provide_database_stub,
    provide_get_items_stub,
    provide_get_item_by_id_stub,
    provide_create_item_stub,
    provide_delete_item_stub,
    provide_update_item_stub,
    provide_create_picture_item_relation_stub,
    provide_delete_picture_item_relation_stub,
    provide_get_picture_item_relation_by_id_stub,
    provide_get_picture_item_relations_by_item_id_stub,
    provide_update_picture_item_relation_stub,
    provide_create_sale_item_relation_stub,
    provide_delete_sale_item_relation_stub,
    provide_get_sale_item_relation_by_id_stub,
    provide_get_sale_item_relation_by_item_id_stub,
    provide_get_sale_item_relation_by_user_id_stub
)

from app.presentation.di.provides import (
    provide_sign_up,
    provide_sign_in,
    provide_get_user_by_id,
    provide_create_token,
    provide_get_user_by_email,
    provide_password_hasher,
    provide_token_decoder,
    provide_token_encoder,
    provide_delete_token_by_user_id,
    provide_logout,
    provide_delete_user,
    provide_update_user,
    provide_create_picture,
    provide_get_picture,
    provide_delete_picture_by_user_id,
    provide_delete_picture,
    provide_get_items,
    provide_get_item_by_id,
    provide_create_item,
    provide_delete_item,
    provide_update_item,
    provide_create_picture_item_relation,
    provide_delete_picture_item_relation,
    provide_get_picture_item_relation_by_id,
    provide_get_picture_item_relations_by_item_id,
    provide_update_picture_item_relation,
    provide_create_sale_item_relation,
    provide_delete_sale_item_relation,
    provide_get_sale_item_relation_by_id,
    provide_get_sale_item_relation_by_item_id,
    provide_get_sale_item_relation_by_user_id
)


def setup_di(app: FastAPI):
    app.dependency_overrides.update({
        provide_database_stub: lambda: database
    })

    app.dependency_overrides.update(
        {
            provide_sign_up_stub: provide_sign_up,
            provide_sign_in_stub: provide_sign_in,
            provide_get_user_by_id_stub: provide_get_user_by_id,
            provide_get_user_by_email_stub: provide_get_user_by_email,
            provide_create_token_stub: provide_create_token,
            provide_password_hasher_stub: provide_password_hasher,
            provide_token_encoder_stub: provide_token_encoder,
            provide_token_decoder_stub: provide_token_decoder,
            provide_delete_token_by_user_id_stub: provide_delete_token_by_user_id,
            provide_logout_stub: provide_logout,
            provide_delete_user_stub: provide_delete_user,
            provide_update_user_stub: provide_update_user,
            provide_create_picture_stub: provide_create_picture,
            provide_get_picture_stub: provide_get_picture,
            provide_delete_picture_by_user_id_stub: provide_delete_picture_by_user_id,
            provide_delete_picture_stub: provide_delete_picture,
            provide_get_items_stub: provide_get_items,
            provide_get_item_by_id_stub: provide_get_item_by_id,
            provide_create_item_stub: provide_create_item,
            provide_delete_item_stub: provide_delete_item,
            provide_update_item_stub: provide_update_item,
            provide_create_picture_item_relation_stub: provide_create_picture_item_relation,
            provide_delete_picture_item_relation_stub: provide_delete_picture_item_relation,
            provide_get_picture_item_relation_by_id_stub: provide_get_picture_item_relation_by_id,
            provide_get_picture_item_relations_by_item_id_stub: provide_get_picture_item_relations_by_item_id,
            provide_update_picture_item_relation_stub: provide_update_picture_item_relation,
            provide_create_sale_item_relation_stub: provide_create_sale_item_relation,
            provide_delete_sale_item_relation_stub: provide_delete_sale_item_relation,
            provide_get_sale_item_relation_by_id_stub: provide_get_sale_item_relation_by_id,
            provide_get_sale_item_relation_by_item_id_stub: provide_get_sale_item_relation_by_item_id,
            provide_get_sale_item_relation_by_user_id_stub: provide_get_sale_item_relation_by_user_id
        }
    )
