from src.models.db_tables.transactions import Transactions
from .interfaces.transactions_repository import TransactionRepositoryInterface


class TransactionRepository(TransactionRepositoryInterface):
  def __init__(self, db_connection_handler):
    self.__db_connection = db_connection_handler

  def create_transaction(self, data):
    with self.__db_connection as db:
      try:
        new_transaction = Transactions(
          user_id = data.user_id,
          account_id = data.account_id,
          description = data.description,
          amount = data.amount,
          type = data.type,
          category = data.category,
        )
        db.add(new_transaction)
        db.commit()
        return new_transaction
      except Exception as e:
        db.rollback()
        raise e
      

  def get_transaction_by_user_id(self, user_id)->list[Transactions]:
    with self.__db_connection as db:
      try:
        transactions = db.query(Transactions).filter(
          Transactions.user_id == user_id).all()
        return transactions
      
      except Exception as e:
        db.rollback()
        raise e

  def get_transaction_by_id(self, transaction_id):
    with self.__db_connection as db:
      try:
        transaction = db.query(Transactions).filter(Transactions.id == transaction_id).first()
        return transaction
      except Exception as e:
        db.rollback()
        raise e
