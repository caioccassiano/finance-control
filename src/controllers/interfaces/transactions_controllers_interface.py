from abc import ABC, abstractmethod

class CreateTransactionControllerInterface(ABC):

  @abstractmethod
  def create_transaction(self, data):
    pass


class ListTransactionsControllerInterface(ABC):

  @abstractmethod
  def list_transactions_by_user(self, user_id):
    pass


  