from src.controllers.interfaces.users_controller_interface import UsersCreateControllerInterface, LoginCreatorControllerInterface, UserDeleteControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class UsersCreateView():
  def __init__(self, controller:UsersCreateControllerInterface):
    self.__controller = controller

  def create(self, request:HttpRequest)->HttpResponse:
    data = request.body
    response = self.__controller.create_user(data=data)
    return HttpResponse(
      body={"data": response}, status_code=201
    )


