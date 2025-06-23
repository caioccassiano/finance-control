from pydantic import BaseModel
from datetime import datetime

class CreateAccount(BaseModel):
  user_id: int
  saldo: float

class AccountOut(CreateAccount):
  created_at: datetime
  username: str

  class Config:
    orm_mode = True


class AccountUpdateBalance(BaseModel):
  account_id: int
  amount: float


class GetAccountById(BaseModel):
  account_id: int