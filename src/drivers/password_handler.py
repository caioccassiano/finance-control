import bcrypt

class PasswordHandler:
  def encrypt_password(self, password:str)->str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode("utf-8"), salt=salt)
    hashed_password = hashed.decode("utf-8")
    return hashed_password
  
  def check_password(self, password:str, hashed_password:str)->bool:
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))
  


