from fastapi import (
    APIRouter,
    Depends,
    WebSocket,
    WebSocketDisconnect,
    status,
    HTTPException,
    Form)

from app.core.chat.dto.chat import CreateChat, ChatId
from app.core.chat_message.dto.message import Message

from app.core.chat.usecase.create_chat import CreateChatUseCase
from app.core.chat.usecase.get_chat_by_id import GetChatByIdUseCase
from app.core.chat.usecase.delete_chat import DeleteChatUseCase

from app.core.chat_message.usecase.add_message import AddMessageUseCase
from app.core.chat_message.usecase.delete_message import DeleteMessageUseCase
from app.core.chat_message.usecase.delete_all_messages import DeleteAllMessagesUseCase
from app.core.chat_message.usecase.get_all_messages import GetAllMessagesUseCase

from app.presentation.di import (
    provide_get_chat_by_id_stub,
    provide_create_chat_stub,
    provide_delete_chat_stub,
    provide_get_all_messages_stub,
    provide_add_message_stub,
    provide_delete_message_stub,
    provide_delete_all_messages_stub
)

import aiohttp

router = APIRouter()


class Chat:
    def __init__(self):
        self.id
        self.usr
        self.seller


class ConnectionManager:
    def __init__(self):
        self.chats = list

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast_to_caht(self, message: str, chat: Chat):
        for connection in chat:
            await connection.send_text(message)


manager = ConnectionManager()


# Работа в веб-сокетом
async def connect_user(client_id):
    async with aiohttp.ClientSession() as session:
        async with session.ws_connect(f'http://localhost:8000/api/chat/ws/{client_id}') as ws:
            async for msg in ws:
                if msg.type == aiohttp.WSMsgType.TEXT:
                    add_message(client_id, msg)


@router.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"{data}", websocket)
            await manager.broadcast(f"{data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)


# Работа с чатом
@router.get("{item_id}/{user_id}/{chat_id}")
async def get_chat_by_id(
        user_id,
        chat_id: str,
        get_chat_by_id: GetChatByIdUseCase = Depends(
            provide_get_chat_by_id_stub
        ),
        get_all_messages: GetAllMessagesUseCase = Depends(
            provide_get_all_messages_stub
        )
):
    try:
        chat = get_chat_by_id.execute(ChatId(id=chat_id))
        if chat not in manager.chats:
            manager.chats.append(chat)
        else:
            for i in manager.chats:
                if chat.id == i.id:
                    chat = i
        match user_id:
            case chat.seller_id:
                connect_user(user_id)
            case chat.buyer_id:
                connect_user(user_id)
        messages = get_all_messages.execute(id=chat.messages_id)
        return messages
    except TypeError:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No chat with such id"
        )


@router.post("/{item_id}/{chat_id}")
async def create_chat(
        item_id,
        seller_id = str,
        buyer_id = str,
        create_chat: CreateChatUseCase = Depends(provide_create_chat_stub)
):
    try:
        create_chat.execute(
            chat=CreateChat(
                seller_id=seller_id,
                buyer_id=buyer_id,
                item_id=item_id,
                messages_id=None
            )
        )
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(e)
        )


@router.delete("/{chat_id}")
async def delete_chat(
        chat_id: str,
        message_id: str,
        delete_chat: DeleteChatUseCase = Depends(provide_delete_chat_stub)
):
    delete_chat.execute(chat_id=chat_id, message_id=message_id)


# Работа с сообщениями
async def add_message(
        user_name: str = Form(),
        message = str,
        add_message: AddMessageUseCase = Depends(provide_add_message_stub)
):
    try:
        add_message(message=Message(
            user_name=user_name,
            datetime=str(11),
            message=message
        ))
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(e)
        )


@router.delete("/{chat_id}/{message_id}")
async def delete_all_messages(
        messages_id: str,
        delete_all_messages: DeleteAllMessagesUseCase = Depends(
            provide_delete_all_messages_stub)
):
    delete_all_messages.execute(messages_id)


@router.delete("/{chat_id}/{message_id}")
async def delete_message(
        message_id: str,
        delete_message: DeleteMessageUseCase = Depends(
            provide_delete_message_stub)
):
    delete_message.execute(message_id)


@router.get("/{chat_id}/messages")
async def get_all_messages(
        get_all_messages: GetAllMessagesUseCase = Depends(
            provide_get_all_messages_stub)
):
    try:
        messages = get_all_messages()
    except TypeError:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No items"
        )
