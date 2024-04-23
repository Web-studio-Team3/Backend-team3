from fastapi import FastAPI

from app.infrastracture.connect import database
from app.infrastracture.websoket import ChatManager


from app.presentation.di.provides import (
    provide_create_category,
    provide_create_item,
    provide_create_picture,
    provide_create_picture_item_relation,
    provide_create_sale_item_relation,
    provide_create_sold_item_relation,
    provide_create_token,
    provide_delete_category,
    provide_delete_item,
    provide_delete_picture,
    provide_delete_picture_by_user_id,
    provide_delete_picture_item_relation,
    provide_delete_sale_item_relation,
    provide_delete_sold_item_relation,
    provide_delete_token_by_user_id,
    provide_delete_user,
    provide_get_categories,
    provide_get_category_by_id,
    provide_get_item_by_id,
    provide_get_items,
    provide_get_items_by_seller_id,
    provide_get_picture,
    provide_get_picture_item_relation_by_id,
    provide_get_picture_item_relations_by_item_id,
    provide_get_sale_item_relation_by_id,
    provide_get_sale_item_relation_by_item_id,
    provide_get_sale_item_relation_by_user_id,
    provide_get_sold_item_relation_by_buyer_id,
    provide_get_sold_item_relation_by_id,
    provide_get_sold_item_relation_by_item_id,
    provide_get_sold_item_relation_by_seller_id,
    provide_create_favourite,
    provide_delete_favourite,
    provide_get_favourite_by_id,
    provide_get_favourites_count_by_item_id,
    provide_get_access_token_by_jwt,
    provide_delete_sale_item_relation_by_item_id,
    provide_delete_favourites_by_item_id,
    provide_delete_sold_item_relation_by_item_id,
    provide_get_favourites_by_item_id,
    provide_get_favourites_by_user_id,
    provide_create_chat,
    provide_delete_chat,
    provide_get_chat_by_id,
    provide_get_all_messages,
    provide_add_message,
    provide_delete_message,
    provide_delete_all_messages,
    provide_get_user_by_email,
    provide_get_user_by_id,
    provide_logout,
    provide_password_hasher,
    provide_sign_in,
    provide_sign_up,
    provide_token_decoder,
    provide_token_encoder,
    provide_update_category,
    provide_update_item,
    provide_update_picture_item_relation,
    provide_update_user,
    provide_update_chat,
    provide_get_cart_by_user_id,
    provide_create_cart_item,
    provide_delete_cart_item,
)
from app.presentation.di.stubs import (
    provide_add_message_stub,
    provide_create_category_stub,
    provide_create_chat_stub,
    provide_create_favourite_stub,
    provide_create_item_stub,
    provide_create_picture_item_relation_stub,
    provide_create_picture_stub,
    provide_create_sale_item_relation_stub,
    provide_create_sold_item_relation_stub,
    provide_create_token_stub,
    provide_database_stub,
    provide_delete_all_messages_stub,
    provide_delete_category_stub,
    provide_delete_chat_stub,
    provide_delete_favourite_stub,
    provide_delete_favourites_by_item_id_stub,
    provide_delete_item_stub,
    provide_delete_message_stub,
    provide_delete_picture_by_user_id_stub,
    provide_delete_picture_item_relation_stub,
    provide_delete_picture_stub,
    provide_delete_sale_item_relation_by_item_id_stub,
    provide_delete_sale_item_relation_stub,
    provide_delete_sold_item_realtion_by_item_id_stub,
    provide_delete_sold_item_relation_stub,
    provide_delete_token_by_user_id_stub,
    provide_delete_user_stub,
    provide_get_access_token_by_jwt_stub,
    provide_get_all_messages_stub,
    provide_get_categories_stub,
    provide_get_category_by_id_stub,
    provide_get_chat_by_id_stub,
    provide_get_favourite_by_id_stub,
    provide_get_favourites_by_user_id_stub,
    provide_get_favourites_count_by_item_id_stub,
    provide_get_item_by_id_stub,
    provide_get_items_stub,
    provide_get_items_by_seller_id_stub,
    provide_get_picture_item_relation_by_id_stub,
    provide_get_picture_item_relations_by_item_id_stub,
    provide_get_picture_stub,
    provide_get_sale_item_relation_by_id_stub,
    provide_get_sale_item_relation_by_item_id_stub,
    provide_get_sale_item_relation_by_user_id_stub,
    provide_get_sold_item_relation_by_buyer_id_stub,
    provide_get_sold_item_relation_by_id_stub,
    provide_get_sold_item_relation_by_item_id_stub,
    provide_get_sold_item_relation_by_seller_id_stub,
    provide_get_user_by_email_stub,
    provide_get_user_by_id_stub,
    provide_get_favourites_by_item_id_stub,
    provide_logout_stub,
    provide_password_hasher_stub,
    provide_sign_in_stub,
    provide_sign_up_stub,
    provide_token_decoder_stub,
    provide_token_encoder_stub,
    provide_update_category_stub,
    provide_update_item_stub,
    provide_update_picture_item_relation_stub,
    provide_update_user_stub,
    provide_update_chat_stub,
    provide_chat_manager_stub,
    provide_get_cart_by_user_id_stub,
    provide_create_cart_item_stub,
    provide_delete_cart_item_stub,
)


def setup_di(app: FastAPI):
    chat_manager = ChatManager()
    app.dependency_overrides.update(
         {
             provide_database_stub: lambda: database,
             provide_chat_manager_stub: lambda: chat_manager,
         }
    )

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
            provide_get_items_by_seller_id_stub: provide_get_items_by_seller_id,
            provide_get_categories_stub: provide_get_categories,
            provide_get_category_by_id_stub: provide_get_category_by_id,
            provide_create_category_stub: provide_create_category,
            provide_delete_category_stub: provide_delete_category,
            provide_update_category_stub: provide_update_category,
            provide_create_picture_item_relation_stub: provide_create_picture_item_relation,
            provide_delete_picture_item_relation_stub: provide_delete_picture_item_relation,
            provide_get_picture_item_relation_by_id_stub: provide_get_picture_item_relation_by_id,
            provide_get_picture_item_relations_by_item_id_stub: provide_get_picture_item_relations_by_item_id,
            provide_update_picture_item_relation_stub: provide_update_picture_item_relation,
            provide_create_sale_item_relation_stub: provide_create_sale_item_relation,
            provide_delete_sale_item_relation_stub: provide_delete_sale_item_relation,
            provide_get_sale_item_relation_by_id_stub: provide_get_sale_item_relation_by_id,
            provide_get_sale_item_relation_by_item_id_stub: provide_get_sale_item_relation_by_item_id,
            provide_get_sale_item_relation_by_user_id_stub: provide_get_sale_item_relation_by_user_id,
            provide_create_sold_item_relation_stub: provide_create_sold_item_relation,
            provide_delete_sold_item_relation_stub: provide_delete_sold_item_relation,
            provide_get_sold_item_relation_by_buyer_id_stub: provide_get_sold_item_relation_by_buyer_id,
            provide_get_sold_item_relation_by_id_stub: provide_get_sold_item_relation_by_id,
            provide_get_sold_item_relation_by_item_id_stub: provide_get_sold_item_relation_by_item_id,
            provide_get_sold_item_relation_by_seller_id_stub: provide_get_sold_item_relation_by_seller_id,
            provide_create_favourite_stub: provide_create_favourite,
            provide_delete_favourite_stub: provide_delete_favourite,
            provide_get_favourite_by_id_stub: provide_get_favourite_by_id,
            provide_get_favourites_count_by_item_id_stub: provide_get_favourites_count_by_item_id,
            provide_get_favourites_by_user_id_stub: provide_get_favourites_by_user_id,
            provide_get_access_token_by_jwt_stub: provide_get_access_token_by_jwt,
            provide_delete_sale_item_relation_by_item_id_stub: provide_delete_sale_item_relation_by_item_id,
            provide_delete_favourites_by_item_id_stub: provide_delete_favourites_by_item_id,
            provide_delete_sold_item_realtion_by_item_id_stub: provide_delete_sold_item_relation_by_item_id,
            provide_get_favourites_by_item_id_stub: provide_get_favourites_by_item_id,
            provide_create_chat_stub: provide_create_chat,
            provide_update_chat_stub: provide_update_chat,
            provide_delete_chat_stub: provide_delete_chat,
            provide_get_chat_by_id_stub: provide_get_chat_by_id,
            provide_get_all_messages_stub: provide_get_all_messages,
            provide_add_message_stub: provide_add_message,
            provide_delete_message_stub: provide_delete_message,
            provide_delete_all_messages_stub: provide_delete_all_messages,
            provide_get_cart_by_user_id_stub: provide_get_cart_by_user_id,
            provide_create_cart_item_stub: provide_create_cart_item,
            provide_delete_cart_item_stub: provide_delete_cart_item,
        }
    )
