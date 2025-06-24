from abc import ABC, abstractmethod

class CreateAccountControllerInterface(ABC):

  @abstractmethod
  def create_account(self, user_id): pass

class ListAccountsByUserIdControllerInterface(ABC):

  @abstractmethod
  def list_account(self, user_id): pass


class DeleteAccountControllerInterface(ABC):
  
  @abstractmethod
  def delete(self, user_id, account_id): pass