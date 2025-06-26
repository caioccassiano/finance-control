

class VerifyUserAuth():
  def verify_user_auth(self, user_id: int, headers_user_id:int)->bool:
    if user_id != headers_user_id:
      raise Exception("User not authenticated!")
    return True