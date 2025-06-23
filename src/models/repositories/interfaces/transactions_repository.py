from abc import ABC, abstractmethod

class TransactionRepositoryInterface(ABC):

  @abstractmethod
  def create_transaction():pass

  @abstractmethod
  def get_transaction_by_user_id():pass

  @abstractmethod
  def get_transaction_by_id():pass


  