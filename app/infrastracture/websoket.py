from fastapi import WebSocket

from app.core.chat_message.dto.message import Message

class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    def __del__(self):
        print("все отключены, объект менеджера удалён")

    async def connect(self, websocket: WebSocket) -> None:
        if not len(self.active_connections) == 2:
            await websocket.accept()
            self.active_connections.append(websocket)
        else:
            raise Exception('There can be only 2 connections in total')

    async def disconnect(self, websocket: WebSocket) -> None:
        if not len(self.active_connections) == 0:
            self.active_connections.remove(websocket)
        del self
        raise Exception("Chat is empty")

    # async def send_personal_message(self, message: str, websocket: WebSocket) -> None:
    #     await websocket.send_text(message)

    async def broadcast(self, data: dict) -> None:
        for connection in self.active_connections:
            await connection.send_json(data.__dict__)


class ChatManager:
    active_chats = dict()

    def Get_connection_manager(self, chat_id: str):
        if chat_id in self.active_chats.keys():
            return self.active_chats.get(chat_id)
        else:
            # print("ужос такого чата нет")
            self.Add_connection_manager(chat_id)
            return self.active_chats[chat_id]

    def Add_connection_manager(self, chat_id: str) -> None:
        self.active_chats[chat_id] = ConnectionManager()
        self.Get_connection_manager(chat_id)
