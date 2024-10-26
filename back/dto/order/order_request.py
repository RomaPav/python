from typing import Any, List

from pydantic import BaseModel


class OrderBase(BaseModel):
    coin_id: int
    user_id: int

    class Config:
        from_attributes = True

class OrderCreate(OrderBase):
    pass




class OrderResponse(OrderBase):
    id: int
    coin: Any
    user: Any