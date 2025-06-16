from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from datetime import datetime, timezone
from src.models.config.base import Base


class Account(Base):
  __tablename__ = "account"
  
  id = Column(Integer, primary_key=True, autoincrement=True)
  user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
  saldo = Column(Float, server_default=None)
  created_at = Column(DateTime, default=datetime.now(timezone.utc))

  