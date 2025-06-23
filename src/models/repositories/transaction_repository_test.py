from .transactions import TransactionRepository
from src.models.config.base import Base
from src.models.config.connection import db_connection_handler
from src.models.db_tables.users import Users
from src.models.db_tables.account import Accounts
from src.models.db_tables.transactions import Transactions, TransactionType, TransactionCategory
import pytest


db_connection_handler.connect_to_db()
engine = db_connection_handler.get_engine()
Base.metadata.create_all(engine)

@pytest.mark.skip(reason="interact with db")
def test_create_transaction():
  mock_connection = db_connection_handler

  data = Transactions(
    user_id= 3,
    account_id= 1,
    description= "Comida",
    amount= 156.45,
    type= TransactionType.ENTRADA,
    category= TransactionCategory.ALIMENTACAO
  )
  
  repo = TransactionRepository(mock_connection)
  response = repo.create_transaction(data)
  print(response)

@pytest.mark.skip(reason="interact with db")
def test_get_user_by_user_id():
  mock_connection = db_connection_handler
  user_id = 3
  repo = TransactionRepository(mock_connection)

  transactions = repo.get_transaction_by_user_id(user_id)

  print(transactions)

  
@pytest.mark.skip(reason="interact with db")
def test_get_transaction_by_id():
  mock_connection = db_connection_handler
  transaction_id = 3
  repo = TransactionRepository(mock_connection)

  response = repo.get_transaction_by_id(2)
  print(response)
  print(response.amount)


