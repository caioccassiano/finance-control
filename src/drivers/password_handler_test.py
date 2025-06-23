from .password_handler import PasswordHandler


password_handler = PasswordHandler()

def test_hashed_password():

  password = "caio123"
  hashed_password = password_handler.encrypt_password(password)
  checked_password = password_handler.check_password(password, hashed_password)
  print(hashed_password)

  assert checked_password

  

