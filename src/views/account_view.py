from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface
from src.controllers.interfaces.account_controller_interface import CreateAccountControllerInterface, DeleteAccountControllerInterface, ListAccountsByUserIdControllerInterface
from src.services.verify_user import VerifyUserAuth



class CreateAccountView(ViewInterface):
  def __init__(self, controller: CreateAccountControllerInterface):
    self.__controller = controller
    self.__verify_user = VerifyUserAuth()

  def handle(self, http_request:HttpRequest)->HttpResponse:
    user_id = http_request.params.get("user_id")
    headers_user_id = http_request.headers.get("uid")

    self.__validate_inputs(user_id, headers_user_id)
    self.__verify_user_auth(user_id, headers_user_id)

    response = self.__controller.create_account(user_id)
    return HttpResponse(
      body={"data": response}, status_code=201
    )

  def __validate_inputs(self, user_id, headers_user_id)->None:
    if not(user_id and headers_user_id):
      raise Exception("Missing user_id or headers_user_id")
    if not (isinstance(user_id,int) and isinstance(headers_user_id, int)):
      raise Exception("IDs must be integers")
  
  def __verify_user_auth(self, user_id:int, headers_user_id:int)->None:
    self.__verify_user.verify_user_auth(user_id, headers_user_id)
    


class ListAccountsByUserView(ViewInterface):
  def __init__(self, controller: ListAccountsByUserIdControllerInterface):
    self.__controller = controller
    self.__verify_user = VerifyUserAuth()

  def handle(self, http_request:HttpRequest)->HttpResponse:
    user_id = http_request.params.get("user_id")
    headers_user_id = http_request.headers.get("uid")

    self.__validate_inputs(user_id, headers_user_id)
    self.__verify_user_auth(user_id, headers_user_id)

    response = self.__controller.list_account(user_id)
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


class UserDeleteAccountView(ViewInterface):
  def __init__(self, controller:DeleteAccountControllerInterface):
    self.__controller = controller
    self.__verify_user =VerifyUserAuth()

  def handle(self, http_request: HttpRequest)->HttpResponse:
    user_id = http_request.params.get("user_id")
    account_id = http_request.params.get("account_id")
    headers_user_id = http_request.headers.get("uid")

    self.__validate_inputs(user_id, account_id, headers_user_id)
    self.__verify_user.verify_user_auth(user_id, headers_user_id)
    
    response = self.__controller.delete(user_id, account_id)

    return HttpResponse(
      body=response, status_code=200
    )


  def __validate_inputs(self, user_id, account_id, headers_user_id)->None:
    if not user_id or not headers_user_id or not account_id:
      raise Exception("Missing informations")
    if not (isinstance(user_id,int) or not isinstance(headers_user_id, int or not isinstance(account_id, int))):
      raise Exception("IDs must be integers")
    

