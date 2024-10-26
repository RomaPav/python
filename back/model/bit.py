from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from database.database import Base, engine

class Bit(Base):
    __tablename__ = "bit"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("marketplace_users.id"), nullable=True)
    trade_lot_id = Column(Integer, ForeignKey("trade_lot.id"), nullable=False)
    amount = Column(Float, nullable=True)

    trade_lot = relationship("TradeLot", back_populates="bit")
    user = relationship("User", back_populates="bits")

Bit.metadata.create_all(bind=engine)