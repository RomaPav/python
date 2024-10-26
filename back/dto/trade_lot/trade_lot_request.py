from typing import Any, List

from pydantic import BaseModel

from enums.lot_status import LotStatus


class TradeLotBase(BaseModel):
    coin_id: int
    trade_status: LotStatus

    class Config:
        from_attributes = True


class TradeLotCreate(TradeLotBase):
    pass

class TradeLotUpdate(TradeLotBase):
    id: int


class TradeLotResponse(TradeLotBase):
    id: int
    coin: Any
