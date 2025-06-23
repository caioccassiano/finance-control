from pydantic import BaseModel, EmailStr
from datetime import datetime

class CreateUser(BaseModel):
  username: str
  password: str
  email: EmailStr

class UserOut(BaseModel):
  id: int
  username: str
  email: str
  created_at: datetime

  class Config:
    orm_mode = True

class UserbyUsername(BaseModel):
  username: str