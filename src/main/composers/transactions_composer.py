from src.models.config.connection import db_connection_handler
from src.models.repositories.transactions import TransactionRepository
from src.controllers.transactions_controller import CreateTransactionController, ListTransactionsByUserController
from src.views.transactions_view import CreateTransactionView, ListTransactionsByUserView

from src.models.repositories.accounts import AccountsRepository

def create_transaction_composer():
  conn = db_connection_handler
  model_trans = TransactionRepository(conn)
  model_acc = AccountsRepository(conn)
  controller = CreateTransactionController(model_trans, model_acc)
  view = CreateTransactionView(controller)

  return view

def list_transactions_composer():
  conn = db_connection_handler
  model = TransactionRepository(conn)
  controller = ListTransactionsByUserController(model)
  view = ListTransactionsByUserView(controller)
  
  return view


