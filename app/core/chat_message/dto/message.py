from app.shared.dto_base import BaseDto

# ID сообщений
class MessagesId(BaseDto):
    id: str

# Объект сообщения
class Message(BaseDto):
    chat_id: str
   # user_name: str
    date_time: str
    message: str
