from abc import ABC, abstractmethod

class AccountsRepositoryInterface(ABC):

  @abstractmethod
  def create_account(self, user_id): pass


  @abstractmethod
  def get_account_by_user_id(self, user_id)-> list: pass


  @abstractmethod
  def delete_account(self, account_id): pass

  @abstractmethod
  def update_balance(self, account_id, amount): pass


