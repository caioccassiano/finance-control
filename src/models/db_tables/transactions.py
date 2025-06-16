from sqlalchemy import Column, Integer, String, Float, Enum
from src.models.config.base import Base
from enum import Enum as PyEnum


class TransactionType(PyEnum):
  ENTRADA = "entrada"
  SAIDA = "saida"


class TransactionCategory(PyEnum):
  LAZER = "lazer"
  SAUDE = "saude"
  ALIMENTACAO = "alimentacao"
  OUTROS = "outros"
  TRANSPORTE = "transporte"
  EDUCACAO = "educacao"
  MORADIA = "moradia"



class Transactions(Base):
  __tablename__= "transactions"

  id = Column(Integer, primary_key=True, autoincrement=True)
  description = Column(String, nullable=True, default=None)
  amount = Column(Float, nullable=False)
  type = Column(Enum(TransactionType), nullable=False)
  category = Column(Enum(TransactionCategory), nullable = False)


  