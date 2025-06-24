from src.models.db_tables.transactions import TransactionType


class AccountService:
  def update_balance(self, account:int, amount:float, type:TransactionType):
    if type == TransactionType.ENTRADA:
      account.saldo += amount
    elif type == TransactionType.SAIDA:
      account.saldo -= amount
    else:
      raise Exception ("Invalid transaction operation")
    return account


