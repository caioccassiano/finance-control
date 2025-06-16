from sqlalchemy import Column, Integer, String
from src.models.config.base import Base

class Users(Base):
  __tablename__ = "users"
  id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
  username = Column(String(length=20), nullable=False, unique=True)
  password = Column(String, nullable=False)
  email = Column(String, nullable=False)



