from .users import Users
from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime

from datetime import datetime, timezone
from src.models.config.base import Base


class Accounts(Base):
  __tablename__ = "accounts"
  
  id = Column(Integer, primary_key=True, autoincrement=True)
  user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
  saldo = Column(Float, default=0.0, nullable = False)
  created_at = Column(DateTime, default=datetime.now(timezone.utc))

  