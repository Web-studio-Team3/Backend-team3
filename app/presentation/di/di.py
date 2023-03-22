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
    provide_update_user_stub
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
    provide_update_user
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
            provide_update_user_stub: provide_update_user
        }
    )
