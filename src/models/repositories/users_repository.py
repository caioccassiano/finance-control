from src.models.db_tables.users import Users
from .interfaces.users_repository_interface import UsersRepositoryInterface


class UsersRepository(UsersRepositoryInterface):
  def __init__(self, db_connection_handler):
    self.__db_connection = db_connection_handler

  def create_user(self, username, email, password):
    with self.__db_connection as db:
      try:
        new_user = Users(
          username = username,
          email = email,
          password = password
        )
        db.add(new_user)
        db.commit()
        return {
          "id": new_user.id,
          "username": new_user.username,
          "email": new_user.email,
        }
      except Exception as exception:
        db.rollback()
        raise exception
      
  def get_user_by_username(self, username):
    with self.__db_connection as db:
      try:
        user = (
          db.query(Users).filter(Users.username == username)
        ).first()
        return user
      except Exception:
        return None


  def list_users(self)->list[Users]:
    with self.__db_connection as db:
      try:
        users = db.query(Users).all()
        return users
      except Exception:
        return None
      
  
  def delete_user(self, username):
    with self.__db_connection as db:
      
        user = db.query(Users).filter(Users.username == username).first()
        if user is None:
          raise Exception("User does not existis")
        try:
          db.delete(user)
          db.commit()
          return True
        except Exception as exception:
          db.rollback()
          raise exception
        


       
  
      




    

      