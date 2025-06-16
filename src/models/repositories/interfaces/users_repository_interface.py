from abc import ABC, abstractmethod

class UsersRepositoryInterface(ABC):

  @abstractmethod
  def create_user(self, username, email, password):pass

  @abstractmethod
  def get_user_by_username(self, username): pass

  @abstractmethod
  def list_users(self): pass

  @abstractmethod
  def delete_user(self,username): pass

