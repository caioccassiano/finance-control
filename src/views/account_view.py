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
    token_uid = http_request.token_infos.get("user_id")

    self.__validate_inputs(user_id, token_uid)
    self.__verify_user_auth(user_id, token_uid)

    response = self.__controller.create_account(user_id)
    return HttpResponse(
      body={"data": response}, status_code=201
    )

  def __validate_inputs(self, user_id, token_uid)->None:
    user_id = int(user_id)
    if not(user_id and token_uid):
      raise Exception("Missing user_id or token_uid")
    if not (isinstance(user_id,int) and isinstance(token_uid, int)):
      raise Exception("IDs must be integers")
  
  def __verify_user_auth(self, user_id:int, token_uid:int)->None:
    self.__verify_user.verify_user_auth(user_id, token_uid)
    


class ListAccountsByUserView(ViewInterface):
  def __init__(self, controller: ListAccountsByUserIdControllerInterface):
    self.__controller = controller
    self.__verify_user = VerifyUserAuth()

  def handle(self, http_request:HttpRequest)->HttpResponse:
    user_id = http_request.params.get("user_id")
    token_uid = http_request.token_infos.get("user_id")

    self.__validate_inputs(user_id, token_uid)
    self.__verify_user_auth(user_id, token_uid)

    response = self.__controller.list_account(user_id)
    return HttpResponse(
      body={"data": response}, status_code=200
    )

  def __validate_inputs(self, user_id, token_uid)->None:
    user_id = int(user_id)
    if not(user_id and token_uid):
      raise Exception("Missing user_id or token_uid")
    if not (isinstance(user_id,int) and isinstance(token_uid, int)):
      raise Exception("IDs must be integers")
  
  def __verify_user_auth(self, user_id:int, token_uid:int)->None:
    self.__verify_user.verify_user_auth(user_id, token_uid)


class UserDeleteAccountView(ViewInterface):
  def __init__(self, controller:DeleteAccountControllerInterface):
    self.__controller = controller
    self.__verify_user =VerifyUserAuth()

  def handle(self, http_request: HttpRequest)->HttpResponse:
    user_id = http_request.params.get("user_id")
    account_id = http_request.params.get("account_id")
    token_uid = http_request.token_infos.get("user_id")

    self.__validate_inputs(user_id, account_id, token_uid)
    self.__verify_user.verify_user_auth(user_id, token_uid)
    
    response = self.__controller.delete(account_id)

    return HttpResponse(
      body=response, status_code=204
    )


  def __validate_inputs(self, user_id, account_id, token_uid)->None:
    user_id = int(user_id)
    account_id = int(account_id)
    if not user_id or not token_uid or not account_id:
      raise Exception("Missing informations")
    if not (isinstance(user_id,int) or not isinstance(token_uid, int or not isinstance(account_id, int))):
      raise Exception("IDs must be integers")
    

