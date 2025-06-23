from unittest.mock import MagicMock
from src.controllers.users_controller import UsersCreateController

def test_create_user_controller_basico():
    repo = MagicMock()
    controller = UsersCreateController(repository=repo)

    repo.create_user.return_value = {
        "id": 42,
        "username": "lucas",
        "email": "lucas@email.com",
        "created_at": "2025-06-23T22:00:00"
    }

    data = {
        "username": "lucas",
        "password": "1234",
        "email": "lucas@email.com"
    }
    result = controller.create_user(data)

    print(result)

    assert result.username == "lucas"
    assert result.email == "lucas@email.com"
    assert hasattr(result, "id")
    repo.create_user.assert_called_once()
