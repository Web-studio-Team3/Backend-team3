from app.core.chat.dto.chat import CreateChat, ChatId
from app.core.chat.dao.chat_write import ChatWrite
from app.core.shared.usecase_base import UseCase
from app.core.chat.entities.chat import Chat


class CreateChatUseCase(UseCase[CreateChat, ChatId]):
    def __init__(self, dao: ChatWrite):
        self._dao = dao

    def execute(self, obj: CreateChat) -> ChatId:
        try:
            chat = Chat(
                seller_id=obj.seller_id,
                buyer_id=obj.buyer_id,
                item_id=obj.item_id,
                messages_id=obj.messages_id
            )
        except TypeError:
            raise TypeError
        try:
            print("create item use case")
            return self._dao.create(chat=chat)
        except TypeError:
            raise TypeError
