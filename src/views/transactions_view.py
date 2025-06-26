from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface
from src.services.verify_user import VerifyUserAuth
from src.controllers.interfaces.transactions_controllers_interface import CreateTransactionControllerInterface, ListTransactionsControllerInterface

class CreateTransactionView(ViewInterface):
  def __init__(self, controller:CreateTransactionControllerInterface)->None:
    self.__controller = controller
    self.__verify_user = VerifyUserAuth()

  def handle(self, http_request:HttpRequest)->HttpResponse:
    data = http_request.body
    user_id = http_request.params.get("user_id")
    headers_user_id = http_request.headers.get("uid")

    self.__validate_inputs(user_id, headers_user_id, data)
    self.__verify_user_auth(user_id, headers_user_id)

    data["user_id"] = user_id

    response = self.__controller.create_transaction(data)

    return HttpResponse(
      body={"data": response}, status_code=201
    )

  def __validate_inputs(self, user_id, headers_user_id, data)->None:
    if not(user_id and headers_user_id):
      raise Exception("Missing user_id or headers_user_id")
    if not (isinstance(user_id,int) or not isinstance(headers_user_id, int)or not isinstance(data, dict)):
      raise Exception("IDs must be integers or data must be a dictionary")
  
  def __verify_user_auth(self, user_id:int, headers_user_id:int)->None:
    self.__verify_user.verify_user_auth(user_id, headers_user_id)



class ListTransactionsByUserView(ViewInterface):
  def __init__(self, controller: ListTransactionsControllerInterface)-> None:
    self.__controller = controller
    self.__verify_user = VerifyUserAuth()

  def handle(self, http_request: HttpRequest)-> HttpResponse:
    user_id = http_request.params.get("user_id")
    headers_user_id = http_request.headers.get("uid")

    self.__validate_inputs(user_id, headers_user_id)
    self.__verify_user_auth(user_id, headers_user_id)

    response = self.__controller.list_transactions_by_user(user_id)
    return HttpResponse(
      body={"data": response}, status_code=200
    )

  def __validate_inputs(self, user_id, headers_user_id)->None:
    if not(user_id and headers_user_id):
      raise Exception("Missing user_id or headers_user_id")
    if not (isinstance(user_id,int) and isinstance(headers_user_id, int)):
      raise Exception("IDs must be integers")
  
  def __verify_user_auth(self, user_id:int, headers_user_id:int)->None:
    self.__verify_user.verify_user_auth(user_id, headers_user_id)



    