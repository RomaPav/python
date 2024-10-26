from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy import Enum as SqlEnum
from sqlalchemy.orm import relationship

from database.database import Base, engine
from enums.role import UserRole


class User(Base):
    __tablename__ = "marketplace_users"

    id = Column(Integer, primary_key=True, index=True)
    login = Column(String, unique=True, index=True)
    password = Column(String)
    full_name = Column(String)
    email = Column(String)
    role = Column(SqlEnum(UserRole), default=UserRole.USER)
    is_active = Column(Boolean, default=False)

    orders = relationship("Order", back_populates="user")
    bits = relationship("Bit", back_populates="user")

User.metadata.create_all(bind=engine)
