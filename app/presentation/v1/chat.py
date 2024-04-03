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
from app.core.user.dto.user import UserId
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


from app.infrastracture.websoket import ConnectionManager
from app.presentation.bearer import JWTBearer
from app.core.user.usecases.get_user_by_id import GetUserByIdUseCase


from app.infrastracture.websoket import ChatManager


from app.presentation.di import (
    provide_add_message_stub,
    provide_create_chat_stub,
    provide_delete_all_messages_stub,
    provide_delete_chat_stub,
    provide_delete_message_stub,
    provide_get_access_token_by_jwt_stub,
    provide_get_all_messages_stub,
    provide_get_chat_by_id_stub,
    provide_update_chat_stub,
    provide_get_user_by_id_stub,
    provide_chat_manager_stub,
)

router = APIRouter()
# Работа в веб-сокетом


async def connect_user(user_id: str):
    async with aiohttp.ClientSession() as session:
        async with session.ws_connect(
            f"http://localhost:8000/api/chat/ws/{user_id}"
        ) as ws:
            async for msg in ws:
                if msg.type == aiohttp.WSMsgType.TEXT:
                    add_message(user_id, msg)


@router.websocket("/ws/{chat_id}")
async def websocket_endpoint(
    websocket: WebSocket,
    chat_id: str,
    chat_manager: ChatManager = Depends(provide_chat_manager_stub),
):
    manager = chat_manager.Get_connection_manager(chat_id)
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"{data}", websocket)
            await manager.broadcast(f"{data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)


# Работа с чатом
@router.get("/{chat_id}")
async def get_chat_by_id(
    chat_id: str,
    get_all_messages: GetAllMessagesUseCase = Depends(provide_get_all_messages_stub),
    get_chat_by_id: GetChatByIdUseCase = Depends(provide_get_chat_by_id_stub),
    chat_manager: ChatManager = Depends(provide_chat_manager_stub),
):
    try:
        if not(chat_id in chat_manager.active_chats):
            chat_manager.Add_connection_manager(chat_id)
        chat = get_chat_by_id.execute(chat_id)
        messages = get_all_messages.execute(chat.messages_id)
        return messages
    except TypeError:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="No chat with such id"
        )


@router.post("/")
async def create_chat(
    seller_id: str,
    buyer_id: str,
    create_chat_use_case: CreateChatUseCase = Depends(provide_create_chat_stub),
):
    try:
        await create_chat_use_case.execute(
            obj=CreateChat(seller_id=seller_id, buyer_id=buyer_id)
        )
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e)
        )


@router.delete("/{chat_id}")
async def delete_chat(
    chat_id: str,
    delete_chat: DeleteChatUseCase = Depends(provide_delete_chat_stub),
):
    delete_chat.execute(chat_id=chat_id)


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