from app.core.chat.dao.chat_read import ChatRead
from app.core.chat.dto.chat import ChatId
from app.core.shared.usecase_base import UseCase
from app.core.chat.entities.chat import Chat


class GetChatByIdUseCase(UseCase[ChatId, Chat]):
    def __init__(self, dao: ChatRead):
        self._dao = dao

    def execute(self, chat_id: ChatId) -> Chat:
        try:
            chat = self._dao.get_by_id(chat_id.id)
        except TypeError:
            raise TypeError
        return chat
