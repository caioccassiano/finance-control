from src.models.config.connection import db_connection_handler
from src.models.repositories.accounts import AccountsRepository
from src.controllers.account_controller import CreateAccountController, ListAccountsByUserIdController, DeleteAccountController
from src.views.account_view import CreateAccountView, ListAccountsByUserView, UserDeleteAccountView


def create_account_composer(): 
  conn = db_connection_handler
  model = AccountsRepository(conn)
  controller = CreateAccountController(model)
  view = CreateAccountView(controller)

  return view

def list_accounts_composer():
  conn = db_connection_handler
  model = AccountsRepository(conn)
  controller = ListAccountsByUserIdController(model)
  view = ListAccountsByUserView(controller)

  return view

def delete_account_composer():
  conn = db_connection_handler
  model = AccountsRepository(conn)
  controller = DeleteAccountController(model)
  view = UserDeleteAccountView(controller)

  return view




