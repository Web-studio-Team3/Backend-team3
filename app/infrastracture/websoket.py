from fastapi import WebSocket

from app.core.chat.entities.chat import Chat


class ConnectionManager:
    def __init__(self):
        self.active_connections = list[Chat]

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
