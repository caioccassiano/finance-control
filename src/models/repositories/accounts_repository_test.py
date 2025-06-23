from src.models.config.connection import db_connection_handler
from src.models.config.base import Base
from .accounts import AccountsRepository
from src.models.db_tables.account import Accounts
import pytest


db_connection_handler.connect_to_db()
engine = db_connection_handler.get_engine()
Base.metadata.create_all(engine)

@pytest.mark.skip(reason="Interation with db")
def test_create_account():
  mock_connection = db_connection_handler
  user_id = 3
  repo = AccountsRepository(mock_connection)

  response = repo.create_account(user_id)
  print(response)

@pytest.mark.skip(reason="Interation with db")
def test_update_balance():
  mock_connection = db_connection_handler
  amount = 324.45
  account_id = 1
  repo = AccountsRepository(mock_connection)

  repo.update_balance(account_id, amount)

def test_get_account_by_user_id():
  mock_conn = db_connection_handler
  user_id = 3
  repo = AccountsRepository(mock_conn)
  accounts = repo.get_account_by_user_id(user_id)

  print(accounts)

  for account, username in accounts:
    print(account.saldo, username)

  




