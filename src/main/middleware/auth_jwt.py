from flask import request, g
from functools import wraps
from src.drivers.jwt_handler import JwtHandler


def auth_verify_jwt(f):

  @wraps(f)
  def wrapper(*args, **kwargs):
    jwt_handler = JwtHandler()
    raw_token = request.headers.get("Authorization")
    user_id = int(request.view_args.get("user_id"))

    if not raw_token or not user_id:
      raise Exception("Invalid inputs")
    
    token = raw_token.split()[1]
    token_informations = jwt_handler.decode_jwt_token(token)
    token_uid = token_informations["user_id"]

    if user_id and token_uid and (int(token_uid) == int(user_id)):
      g.token_informations = token_informations
      return f(*args, **kwargs)
    raise Exception("User Unauthorized!")
  return wrapper
  

