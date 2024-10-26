from typing import List, Any

from pydantic import BaseModel

from dto.order.order_request import OrderBase
from dto.trade_lot.trade_lot_request import TradeLotBase


class BitBase(BaseModel):
    user_id: int | None
    trade_lot_id: int
    amount: float | None

    class Config:
        from_attributes = True


class BitCreate(BitBase):
    pass


class BitUpdate(BitBase):
    id: int


class BitResponse(BitBase):
    id: int
    user: Any
    trade_lot: Any
