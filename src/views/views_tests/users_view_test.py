from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.users_view import UsersCreateView, UsersDeleteView, UsersLoginView


class MockController:
  def create_user(self, data):
    return {"alguma": "coisa"}
  

def test_handle_create_user():
  body= {
    "username": "MyUsername",
    "password": "password123",
    "email": "user@github.com"
  }

  request = HttpRequest(body=body)

  mock_controller = MockController()
  view = UsersCreateView(mock_controller)

  response = view.handle(request)
  print()
  print(response)
  print(response.body)

  assert isinstance(response, HttpResponse)
  assert response.body == {"data": {"alguma":"coisa"}}
  assert response.status_code == 201
  



