from src.models.repositories.interfaces.accounts_repository_interface import AccountsRepositoryInterface
from src.models.schemas.accounts_schemas import AccountOut
from .interfaces.account_controller_interface import CreateAccountControllerInterface, ListAccountsByUserIdControllerInterface, DeleteAccountControllerInterface


class CreateAccountController(CreateAccountControllerInterface):
  def __init__(self, account_repository: AccountsRepositoryInterface ):
    self.__account_repo = account_repository

  def create_account(self, user_id):
    new_account = self.__account_repo.create_account(user_id)
    if not user_id:
      raise Exception ("User does not exist")
    formatted_response = self.__format_response(new_account).model_dump()
    return formatted_response
  
  def __format_response(self, new_account)->AccountOut:
    account_id = new_account["id"]
    account, username = self.__account_repo.get_account_by_id(account_id)
    return AccountOut(
      user_id = account.user_id,
      saldo = account.saldo,
      created_at = account.created_at,
      username = username
    )


class ListAccountsByUserIdController(ListAccountsByUserIdControllerInterface):
  def __init__(self, account_repository: AccountsRepositoryInterface):
    self.__account_repo = account_repository

  def list_account(self, user_id):
    accounts= self.__account_repo.get_account_by_user_id(user_id)
    formatted_response = self.__format_response(accounts)
    return formatted_response


  def __format_response (self, accounts)->AccountOut:
    account_len = len(accounts)
    return [
      AccountOut(
        user_id = account.id,
        saldo = account.saldo,
        created_at = account.created_at,
        username = username
      ).model_dump()
      for account, username in accounts
    ]
  

class DeleteAccountController(DeleteAccountControllerInterface):
  def __init__(self, account_repository: AccountsRepositoryInterface ):
    self.__account_repo = account_repository

  def delete(self, account_id):
    self.__account_repo.delete_account(account_id)
    return True
  
  
