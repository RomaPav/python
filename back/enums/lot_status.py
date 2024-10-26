from enum import Enum


class LotStatus(Enum):
    NOT_STARTED = "not_started"
    STARTED = "started"
    CLOSED = "closed"

    def __str__(self):
        return self.value

    def dict(self) -> str:
        return self.value
