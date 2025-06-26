from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.account_view import ListAccountsByUserView, CreateAccountView

class MockCreateController:
  def create_account(self, user_id):
    return {"new":"account"}
  

def test_create_account():
  params = {"user_id":1}
  headers = {"uid":1}

  request = HttpRequest(
    params=params,
    headers=headers
  )

  mock_controller = MockCreateController()

  view = CreateAccountView(mock_controller)

  response = view.handle(request)

  print()
  print(response)

  assert isinstance(response, HttpResponse)
  assert response.body == {"data": {"new": "account"}}
  assert response.status_code == 201


class MockListController:
  def list_account(self, user_id):
    return {
      "accounts":{
        "account-1": 1,
        "account-2": 2,
        "account-3":3

    }}
  
def test_list_accounts():
  params = {"user_id":1}
  headers = {"uid":1}

  request = HttpRequest(
    params=params,
    headers=headers
  )
  mock_controller = MockListController()
  view = ListAccountsByUserView(mock_controller)

  response = view.handle(request)

  print(response)
  print(response.body)


  
