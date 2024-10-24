from enum import Enum
from typing import Dict, Any


class UserRole(Enum):
    OWNER = "owner"
    ADMIN = "admin"
    USER = "user"

    def __str__(self):
        return self.value

    def dict(self) -> str:
        return self.value
