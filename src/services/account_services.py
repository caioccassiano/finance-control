from src.models.db_tables.transactions import TransactionType
from src.models.db_tables.account import Accounts



class AccountService:
  def update_balance(self, saldo:float, amount:float, type:TransactionType):

    balance = saldo

    if type == TransactionType.ENTRADA:
      balance += amount
    elif type == TransactionType.SAIDA:
      balance -= amount
    else:
      raise Exception ("Invalid transaction operation")
    return balance


