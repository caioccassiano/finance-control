import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")




class DbConnectionHandler:
  def __init__(self):
    self.__connection_string = DATABASE_URL
    self.__engine = None
    self.__session = None
  
  def connect_to_db(self)-> None:
    self.__engine = create_engine(self.__connection_string)
    self.__session = sessionmaker(bind=self.__engine)

  def get_engine(self):
    return self.__engine
  
  def get_session(self):
    if self.__session is None:
      raise Exception("You must call connect_to_db() before using session")
    return self.__session()



db_connection_handler = DbConnectionHandler()


