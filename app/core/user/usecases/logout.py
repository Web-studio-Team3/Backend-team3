from app.core.shared.usecase_base import UseCase

from app.core.user.dto.user import UserId

from app.core.token.usecases.delete_token_by_user_id import DeleteTokenByUserIdUseCase
from app.core.token.dto.token import AccessTokenUserIdDto


class LogoutUseCase(UseCase[UserId, None]):
    def __init__(
            self,
            delete_token_use_case: DeleteTokenByUserIdUseCase
    ):
        self._delete_token_use_case = delete_token_use_case

    def execute(self, user_id: UserId) -> None:
        self._delete_token_use_case.execute(
            AccessTokenUserIdDto(user_id=user_id.id)
        )
