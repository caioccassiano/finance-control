from src.models.db_tables.users import Users
from src.models.repositories.users_repository import UsersRepository
from src.models.config.connection import db_connection_handler
from src.models.config.base import Base
import pytest
from unittest.mock import MagicMock

db_connection_handler.connect_to_db()
engine = db_connection_handler.get_engine()
Base.metadata.create_all(engine)

@pytest.mark.skip(reason="Interation with db")
def test_create_user():

  mock_connection = db_connection_handler

 
  
  username = "caioccassiano",
  email = "caioccassiano@gmail.com",
  password = "caio123"
  

  repo = UsersRepository(mock_connection)
  response = repo.create_user(username, email, password)
  print (response)

@pytest.mark.skip(reason="Already tested!")
def test_create_user_unitario():
  username = "test_user"
  email = "teste@example.com"
  password = "senha123"

  mock_session = MagicMock()

  mock_connection = MagicMock()

  mock_connection.__enter__.return_value = mock_session


  repo = UsersRepository(mock_connection)

  repo.create_user(username, email, password)

  mock_session.add.assert_called_once()
  mock_session.commit.assert_called_once()


  added_user = mock_session.add.call_args[0][0]
  assert isinstance(added_user, Users)
  assert added_user.username == username
  assert added_user.email == email
  assert added_user.password == password




def test_get_user_by_username():
  
  username = "caioccassiano"

  mock_connection = db_connection_handler

  repo = UsersRepository(mock_connection)

  user = repo.get_user_by_username(username=username)

  print(user)
  print(user.username)



def test_list_users():
  mock_connection = db_connection_handler
  repo = UsersRepository(mock_connection)
  response = repo.list_users()

  print(response)


def test_delete_user():
  username = "rosiclair"
  mock_conneciton = db_connection_handler
  repo = UsersRepository(mock_conneciton)
  repo.delete_user(username)

  






