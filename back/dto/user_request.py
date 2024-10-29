from pydantic import BaseModel

from enums.role import UserRole


class UserRequest(BaseModel):
    login: str
    password: str
    full_name: str
    email: str
    role: UserRole
    # def __init__(self, login: str, password: str, full_name: str, email: str, role: UserRole):
    #     self._login = login
    #     self._password = password
    #     self._full_name = full_name
    #     self._email = email
    #     self._role = role
    #
    # def login(self) -> str:
    #     return self._login
    #
    # def password(self) -> str:
    #     return self._password
    #
    # def full_name(self) -> str:
    #     return self._full_name
    #
    # def email(self) -> str:
    #     return self._email
    #
    # def role(self) -> UserRole:
    #     return self._role


class UserUpdate(UserRequest):
    id: int


class UserResponse(UserRequest):
    id: int
    orders: list
