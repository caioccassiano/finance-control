from abc import ABC, abstractmethod

class UsersCreateControllerInterface(ABC):
  
  @abstractmethod
  def create_user(self, data:dict): pass


class LoginCreatorControllerInterface(ABC):

  @abstractmethod
  def login(self, username, password)->dict: pass



class UserDeleteControllerInterface(ABC):

  @abstractmethod
  def delete_user(self, username): pass





