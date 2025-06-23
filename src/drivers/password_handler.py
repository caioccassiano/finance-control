import bcrypt

class PasswordHandler:
  def encrypt_password(self, password:str)->str:
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt=salt)
    return hashed_password
  
  def check_password(self, password:str, hashed_password:str):
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password)
  


