from app.core.chat.dao.chat_write import ChatWrite
from app.core.chat.dto.chat import ChatId, CreateChat
from app.core.chat.entities.chat import Chat
from app.core.shared.usecase_base import UseCase


class CreateChatUseCase(UseCase[CreateChat, ChatId]):
    def __init__(self, write_dao: ChatWrite):
        self.write_dao = write_dao

    def execute(self, obj: CreateChat) -> ChatId:
        try:
            chat = Chat(
                seller_id=obj.seller_id,
                buyer_id=obj.buyer_id,
                messages_id=obj.messages_id,
            )
        except TypeError:
            raise TypeError
        try:
            return self.write_dao.create(chat=chat)
        except TypeError:
            raise TypeError
