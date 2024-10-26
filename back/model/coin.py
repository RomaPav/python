from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

from database.database import Base, engine


class Coin(Base):
    __tablename__ = "coin"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float, nullable=False)
    gold = Column(Float, nullable=False)
    silver = Column(Float, nullable=False)
    bronze = Column(Float, nullable=False)

    orders = relationship("Order", back_populates="coin")
    trade_lots = relationship("TradeLot", back_populates="coin")

Coin.metadata.create_all(bind=engine)