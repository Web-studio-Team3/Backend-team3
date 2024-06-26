from app.core.chat.dao.chat_read import ChatRead
from app.core.chat.dto.chat import ChatId
from app.core.chat.entities.chat import Chat
from app.core.shared.usecase_base import UseCase


class GetChatByIdUseCase(UseCase[ChatId, Chat]):
    def __init__(self, read_dao: ChatRead):
        self.read_dao = read_dao

    def execute(self, chat_id: ChatId) -> Chat:
        try:
            chat = self.read_dao.get_by_id(chat_id)
        except TypeError:
            raise TypeError
        return chat
