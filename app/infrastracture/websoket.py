from fastapi import WebSocket

from app.core.chat.entities.chat import Chat


class ConnectionManager:
    def __init__(self):
        self.active_connections = list[WebSocket]

    async def connect(self, websocket: WebSocket):
        if not self.active_connections.count() == 2:
            await websocket.accept()
            self.active_connections.append(websocket)
        else:
            raise Exception('There can be only 2 connections in total')

    async def disconnect(self, websocket: WebSocket):
        if not self.active_connections.count() == 0:
            self.active_connections.remove(websocket)
        return "Chat is empty"

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast_to_chat(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


class ChatManager:
    def __init__(self):
        self.active_chats = dict()

    def Get_connection_manager(self, chat_id: str):
        return self.active_chats.get(chat_id)

    def Add_connection_manager(self, chat_id: str):
        self.active_chats[chat_id] = ConnectionManager()
        ChatManager.Get_connection_manager(chat_id)