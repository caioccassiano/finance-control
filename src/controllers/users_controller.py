from src.models.repositories.interfaces.users_repository_interface import UsersRepositoryInterface
from src.drivers.password_handler import PasswordHandler
from src.models.schemas.users_schemas import CreateUser, UserOut
from pydantic import ValidationError
from src.drivers.jwt_handler import JwtHandler
from .interfaces.users_controller_interface import UsersCreateControllerInterface, LoginCreatorControllerInterface, UserDeleteControllerInterface



class UsersCreateController(UsersCreateControllerInterface):
  def __init__(self, repository: UsersRepositoryInterface):
    self.__repository = repository
    self.__password_handler = PasswordHandler()

  def create_user(self, data:dict):
    validated_data = self.__validate_body(data=data)
    password = validated_data.password
    hashed_password = self.__create_hash_password(password)
    user_data = {
      "username": validated_data.username,
      "email": validated_data.email,
      "password": hashed_password
    }
    new_user = self.__create_user_in_db(user_data)
    return self.__formated_response(new_user).model_dump()

  def __validate_body(self, data:dict):
    try:
      validated = CreateUser(**data)
      return validated
    except ValidationError as e:
      raise e
  
  def __create_hash_password(self, password):
    hashed_password = self.__password_handler.encrypt_password(password)
    return hashed_password
  
  def __create_user_in_db(self, user_data):
    try:
      new_user = self.__repository.create_user(
        username= user_data["username"],
        email= user_data["email"],
        password= user_data["password"]
      )
      return new_user
    except Exception as e:
      raise e
  
  def __formated_response(self, new_user):
    return UserOut(
      id = new_user["id"],
      username= new_user["username"],
      email = new_user["email"]
    )


class LoginCreatorController(LoginCreatorControllerInterface):
  def __init__(self, repository:UsersRepositoryInterface):
    self.__repository = repository
    self.__jwt_handler = JwtHandler()
    self.__password_handler = PasswordHandler()

  def login(self, username:str, password:str)-> dict:
    user = self.__find_user(username)
    if not user:
      raise Exception("User not found!")
    user_id = user.id
    hashed_password = user.password
    self.__check_password(password=password, hashed_password=hashed_password)
    token = self.__create_user_token(user_id)
    return self.__format_response(username, token)




  def __find_user(self, username:str):
    return self.__repository.get_user_by_username(username)
  
  def __check_password(self, password, hashed_password)->bool:
    try:
      self.__password_handler.check_password(password, hashed_password )
      return True
    except Exception as e:
      raise e
  
  def __create_user_token(self, user_id:int)->str:
    payload = {"user_id": user_id}
    token = self.__jwt_handler.create_jwt_token(payload)

    return token
  
  def __format_response(self, username:str, token:str)->dict:
    return {
      "access": True,
      "username": username,
      "token":token
    }


class UserDeleteController(UserDeleteControllerInterface):
  def __init__(self, repository:UsersRepositoryInterface)-> None:
    self.__repository = repository

  def delete_user(self, user_id:int):
    return self.__repository.delete_user(user_id=user_id)

  


