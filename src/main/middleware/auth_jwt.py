from flask import request
from src.drivers.jwt_handler import JwtHandler

def auth_verify_jwt():
  jwt_handler = JwtHandler()
  raw_token = request.headers.get("Authorization")
  user_id = request.headers.get("uid")

  if not raw_token or not user_id:
    raise Exception("Invalid inputs")
  
  token = raw_token.split()[1]
  token_informations = jwt_handler.decode_jwt_token(token)
  token_uid = token_informations["user_id"]

  if user_id and token_uid and (int(token_uid) == int(user_id)):
    return token_informations
  raise Exception("User Unauthorized!")

