from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy import Enum as SqlEnum
from sqlalchemy.orm import relationship

from database.database import Base, engine
from enums.lot_status import LotStatus


class TradeLot(Base):
    __tablename__ = "trade_lot"

    id = Column(Integer, primary_key=True, index=True)
    coin_id = Column(Integer, ForeignKey("coin.id"), nullable=False)
    trade_status = Column(SqlEnum(LotStatus), default=LotStatus.NOT_STARTED)

    coin = relationship("Coin", back_populates="trade_lots")
    bit = relationship("Bit", back_populates="trade_lot")

TradeLot.metadata.create_all(bind=engine)
