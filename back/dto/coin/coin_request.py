from typing import List

from pydantic import BaseModel

from dto.order.order_request import OrderBase
from dto.trade_lot.trade_lot_request import TradeLotBase


class CoinBase(BaseModel):
    name: str
    price: float
    gold: float
    silver: float
    bronze: float

    class Config:
        from_attributes = True


class CoinCreate(CoinBase):
    pass

class CoinUpdate(CoinBase):
    id: int

class CoinResponse(CoinBase):
    id: int
    orders: List[OrderBase]
    trade_lots: List[TradeLotBase]
