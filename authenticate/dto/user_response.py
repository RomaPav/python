from enums.role import UserRole


class UserResponse:
    def __init__(self, login: str, password: str, full_name: str, email: str, token: str, role: UserRole):
        self._login = login
        self._password = password
        self._token = token
        self._full_name = full_name
        self._email = email
        self._role = role

    def login(self) -> str:
        return self._login

    def password(self) -> str:
        return self._password

    def full_name(self) -> str:
        return self._full_name

    def email(self) -> str:
        return self._email

    def token(self) -> str:
        return self._token

    def role(self) -> UserRole:
        return self._role
