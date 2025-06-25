from .account_controller import CreateAccountController
from unittest.mock import MagicMock
from src.models.schemas.accounts_schemas import AccountOut

def test_create_account():
  mock_repo = MagicMock()
  
  mock_repo.create_account.return_value = MagicMock(user_id=1)

  account_mock = MagicMock(
    id=123,
    user_id=1,
    saldo=100.00,
    create_at="2024-06-25T10:00:00"
  )
  username = "test_user"
  mock_repo.get_account_by_id.return_value = (account_mock, username)

  controller = CreateAccountController(mock_repo)

  result = controller.create_account(account_mock.user_id)

  print(result)

  assert isinstance(result, AccountOut)
  assert result.user_id == 1
  assert result.saldo == 100.00
  assert result.username == "test_user"

  