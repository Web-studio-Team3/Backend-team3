from app.core.user.dao.password_hasher import PasswordHasher
import bcrypt


class PasswordHasherImp(PasswordHasher):
    def hash(self, raw_password: str) -> str:
        return bcrypt.hashpw(raw_password.encode("utf8"), bcrypt.gensalt()).decode("utf8")

    def check_password(self, raw_password: str, hashed_password: str) -> bool:

        return bcrypt.checkpw(raw_password.encode("utf8"), hashed_password.encode("utf8"))
