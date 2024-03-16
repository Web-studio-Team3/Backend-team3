import datetime

import aiohttp
from fastapi import (
    APIRouter,
    Depends,
    Form,
    HTTPException,
    WebSocket,
    WebSocketDisconnect,
    status,
)

from app.core.chat.dto.chat import ChatId, CreateChat, ChatUpdate, ChatUpdateWithId
from app.core.chat.entities.chat import Chat
from app.core.chat.usecase.create_chat import CreateChatUseCase
from app.core.chat.usecase.delete_chat import DeleteChatUseCase
from app.core.chat.usecase.update_chat import UpdateChatUseCase
from app.core.chat.usecase.get_chat_by_id import GetChatByIdUseCase
from app.core.chat_message.dto.message import Message
from app.core.chat_message.usecase.add_message import AddMessageUseCase
from app.core.chat_message.usecase.delete_all_messages import DeleteAllMessagesUseCase
from app.core.chat_message.usecase.delete_message import DeleteMessageUseCase
from app.core.chat_message.usecase.get_all_messages import GetAllMessagesUseCase
from app.core.token.usecases.get_access_token_by_jwt import GetAccessTokenByJwtUseCase
from app.core.user.usecases.get_user_by_id import GetUserByIdUseCase
from app.infrastracture import ConnectionManager
from app.presentation.bearer import JWTBearer
from app.presentation.di import (
    provide_add_message_stub,
    provide_connection_manager_stub,
    provide_create_chat_stub,
    provide_delete_all_messages_stub,
    provide_delete_chat_stub,
    provide_delete_message_stub,
    provide_get_access_token_by_jwt_stub,
    provide_get_all_messages_stub,
    provide_get_chat_by_id_stub,
    provide_update_chat_stub
)

router = APIRouter()


# Работа в веб-сокетом


async def connect_user(user_id):
    async with aiohttp.ClientSession() as session:
        async with session.ws_connect(
            f"http://localhost:8000/api/chat/ws/{user_id}"
        ) as ws:
            async for msg in ws:
                if msg.type == aiohttp.WSMsgType.TEXT:
                    add_message(user_id, msg)


@router.websocket("{chat_id}/ws/{client_id}")
async def websocket_endpoint(
    websocket: WebSocket,
    manager: ConnectionManager = Depends(provide_connection_manager_stub),
):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"{data}", websocket)
            await manager.broadcast(f"{data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)


# Работа с чатом


@router.get("/{item_id}/chat/{chat_id}")
async def get_chat_by_id(
    chat_id: str,
    get_chat_by_id: GetChatByIdUseCase = Depends(provide_get_chat_by_id_stub),
    get_all_messages: GetAllMessagesUseCase = Depends(provide_get_all_messages_stub),
    get_access_token_by_jwt_use_case: GetAccessTokenByJwtUseCase = Depends(
        provide_get_access_token_by_jwt_stub
    ),
    manager: ConnectionManager = Depends(provide_connection_manager_stub),
):
    try:
        print("получение чата...")
        chat = get_chat_by_id.execute(ChatId(id=chat_id))
        print(f"чат{chat}")
        if chat not in manager.chats:
            manager.chats.append(chat)
        else:
            pass

        messages = get_all_messages.execute(id=chat.messages_id)
        return messages
    except TypeError:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="No chat with such id"
        )


@router.post("/{item_id}/{chat_id}")
async def create_chat(
    seller_id: str,
    buyer_id: str,
    create_chat_use_case: CreateChatUseCase = Depends(provide_create_chat_stub),
):
    try:
        print("1")
        create_chat_use_case.execute(
            obj=CreateChat(seller_id=seller_id, buyer_id=buyer_id)
        )
    except Exception as e:
        print("2")
        return HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e)
        )


@router.delete("/{chat_id}")
async def delete_chat(
    chat_id: str,
    delete_chat: DeleteChatUseCase = Depends(provide_delete_chat_stub),
):
    delete_chat.execute(chat_id=chat_id)


# @router.put("/{chat_id}")
# async def update_chat(
#     chat_id: str,
#     chat=ChatUpdate,
#     update_chat_use_case: UpdateChatUseCase = Depends(provide_update_chat_stub)
# ):
#     update_chat = update_chat_use_case.execute(
#         ChatUpdateWithId(id=chat_id, chat_update=chat)
#     )
#     return update_chat


# Работа с сообщениями


async def add_message(
    user_name: str,
    message: str = Form(),
    add_message: AddMessageUseCase = Depends(provide_add_message_stub),
):
    try:
        add_message(
            message=Message(
                user_name=user_name,
                date_time=str(datetime.datetime.now()),
                message=message,
            )
        )
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e)
        )


@router.delete("/{chat_id}/{message_id}")
async def delete_message(
    message_id: str,
    delete_message: DeleteMessageUseCase = Depends(provide_delete_message_stub),
):
    delete_message.execute(message_id)


@router.get("/{chat_id}/messages")
async def get_all_messages(
    get_all_messages: GetAllMessagesUseCase = Depends(provide_get_all_messages_stub),
):
    try:
        messages = get_all_messages.execute()
        return messages
    except TypeError:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No items")
