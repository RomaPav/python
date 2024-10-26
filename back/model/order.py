from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from database.database import Base, engine


class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True, index=True)
    coin_id = Column(Integer, ForeignKey("coin.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("marketplace_users.id"), nullable=False)

    coin = relationship("Coin", back_populates="orders")
    user = relationship("User", back_populates="orders")

Order.metadata.create_all(bind=engine)
