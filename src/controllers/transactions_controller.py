from src.models.repositories.interfaces.transactions_repository import TransactionRepositoryInterface
from src.models.repositories.interfaces.accounts_repository_interface import AccountsRepositoryInterface
from src.models.schemas.transaction_schemas import TransactionCreateSchema, TransactionResponseSchema
from src.services.account_services import AccountService

class CreateTransactionController():
  def __init__(self, 
               trans_repository:TransactionRepositoryInterface,
               acc_repository:AccountsRepositoryInterface
               ):
    self.__trans_repository = trans_repository
    self.__acc_repository = acc_repository
    self.__service = AccountService()

  def create_transaction(self, data):
    validated_data = self.__validate_body(data=data)
    new_transaction = self.__create_transaction(validated_data)
    new_balance = self.__create_new_balance(new_transaction)
    account_id = validated_data.account_id
    self.__update_balance(account_id, new_balance)
    formatted_response = self.__format_response(new_transaction)
    return formatted_response


  
  def __validate_body(self, data):
    try:
      validated_data = TransactionCreateSchema(**data)
      return validated_data
    except Exception as e:
      raise e
    
  def __create_transaction(self, validated_data):
    try:
      new_transaction = self.__trans_repository.create_transaction(validated_data)
      return new_transaction
    except Exception as e:
      raise e
    
  def __create_new_balance(self, new_transaction):
    account = self.__acc_repository.get_account_by_id(new_transaction.account_id)
    amount = new_transaction.amount
    type = new_transaction.type
    new_balance = self.__service.update_balance(account, amount, type)
    return new_balance
  
  def __update_balance(self, account_id:int, new_balance:float):
    return self.__acc_repository.update_balance(account_id, new_balance)
  
  def __format_response(self, new_transaction):
    return TransactionResponseSchema(
      user_id= new_transaction.user_id,
      account_id = new_transaction.account_id,
      description = new_transaction.description,
      amount = new_transaction.amount,
      type = new_transaction.type,
      category = new_transaction.category,
      id = new_transaction.id,
      created_at = new_transaction.created_at
    )
  
    
    


