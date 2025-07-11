from src.controllers.interfaces.users_controller_interface import UsersCreateControllerInterface, LoginCreatorControllerInterface, UserDeleteControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class UsersCreateView(ViewInterface):
  def __init__(self, controller:UsersCreateControllerInterface):
    self.__controller = controller

  def handle(self, http_request:HttpRequest)->HttpResponse:
    data = http_request.body
    response = self.__controller.create_user(data=data)
    return HttpResponse(
      body={"data": response}, status_code=201
    )


class UsersLoginView(ViewInterface):
  def __init__(self, controller: LoginCreatorControllerInterface):
    self.__controller = controller

  def handle(self, http_request: HttpRequest)-> HttpResponse:
    username = http_request.body.get("username")
    password = http_request.body.get("password")

    self.__validate_inputs(username, password)
    response = self.__controller.login(username, password)
    return HttpResponse(
      body={"data": response}, status_code=200
    )

  
  def __validate_inputs(self, username, password)-> None:
    if (
      not username
      or not password
      or not isinstance(username, str)
      or not isinstance(password, str)
    ):
      raise Exception("Invalid inputs")
    


class UsersDeleteView(ViewInterface):
  def __init__(self, controller: UserDeleteControllerInterface):
    self.__controller = controller

  def handle(self, http_request: HttpRequest)-> HttpResponse:
    user_id = http_request.params.get("user_id")
    token_uid = http_request.token_infos.get("user_id")

    self.__validate_inputs(user_id, token_uid)
    response = self.__controller.delete_user(user_id=user_id)
    return HttpResponse(
      body={"data": response}, status_code=200
    )

  def __validate_inputs(self, user_id,  token_uid:any)->None:
    if (
      not user_id
      or not token_uid
      or int(token_uid) != int(user_id)
    ):
      raise Exception("Invalid inputs")
