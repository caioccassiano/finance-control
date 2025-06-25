from src.models.db_tables.transactions import TransactionType


class AccountService:
  def update_balance(self, account, amount:float, type:TransactionType):

    balance = account.saldo

    if type == TransactionType.ENTRADA:
      balance += amount
    elif type == TransactionType.SAIDA:
      balance -= amount
    else:
      raise Exception ("Invalid transaction operation")
    return balance


