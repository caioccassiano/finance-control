from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class TransactionCreateSchema(BaseModel):
  user_id: int
  account_id: int
  description: Optional[str] = None
  amount: float
  type: str
  category: str


class TransactionResponseSchema(TransactionCreateSchema):
  id:int
  created_at: datetime

  class Config:
    model_config = ConfigDict(from_attributes=True)

class TransactionsUserSchema(BaseModel):
  user_id:int

class TransactionGetId:
  id:int


