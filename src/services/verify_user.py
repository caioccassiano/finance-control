

class VerifyUserAuth():
  def verify_user_auth(self, user_id: int, token_id:int)->bool:
    user_id = int(user_id)
    token_id = int(token_id)
    if user_id != token_id:
      raise Exception("User not authenticated!")
    return True