from .interfaces.accounts_repository_interface import AccountsRepositoryInterface
from src.models.db_tables.account import Accounts
from src.models.db_tables.users import Users


class AccountsRepository(AccountsRepositoryInterface):
  def __init__(self, db_connection_handler)-> None:
    self.__db_connection = db_connection_handler


  def create_account(self, user_id):
    with self.__db_connection as db:
      try:

        new_account = Accounts(
          user_id = user_id
        )
        db.add(new_account)
        db.commit()
        return {
          "New account":{
            "user_id": new_account.user_id,
            "account_id": new_account.id
          }
        }
      except Exception as exception:
        db.rollback()
        raise exception
      
  
  def get_account_by_user_id(self, user_id) -> list[Accounts, str]:
    with self.__db_connection as db:
      try:
        accounts = db.query(Accounts, Users.username).join(Users,Accounts.user_id == Users.id).filter(Accounts.user_id == user_id).all()
        return accounts
      except Exception as excpetion:
        db.rollback()
        raise excpetion
      

  def update_balance(self, account_id: int, amount:float)-> bool:
    with self.__db_connection as db:
      try:
        account = db.query(Accounts).filter(Accounts.id == account_id).first()
        if account is None:
          raise Exception("Account does not existis")
        account.saldo += amount
        db.commit()
        return True
      except Exception as exception:
        db.rollback()
        raise exception
      

  def delete_account(self, account_id) -> bool:
    with self.__db_connection as db:
      try:
        account = db.query(Accounts).filter(Accounts.id == account_id).first()
        if account is None:
          raise Exception("Account does not existis")
        db.delete(account)
        db.commit()
        return True
      except Exception as e:
        db.rollback()
        raise e
      
      
    
      
    
