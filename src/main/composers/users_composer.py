from src.models.config.connection import db_connection_handler
from src.models.repositories.users_repository import UsersRepository
from src.controllers.users_controller import LoginCreatorController, UsersCreateController, UserDeleteController
from src.views.users_view import UsersCreateView, UsersLoginView, UsersDeleteView

def user_creator_composer():
  conn = db_connection_handler
  model = UsersRepository(conn)
  controller = UsersCreateController(model)
  view = UsersCreateView(controller)

  return view

def user_login_composer():
  conn = db_connection_handler
  model = UsersRepository(conn)
  controller = LoginCreatorController(model)
  view = UsersLoginView(controller)

  return view

def user_delete_composer():
  conn = db_connection_handler
  model = UsersRepository(conn)
  controller = UserDeleteController(model)
  view = UsersDeleteView(controller)

  return view



