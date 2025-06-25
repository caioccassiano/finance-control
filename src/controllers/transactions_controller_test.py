import unittest
from unittest.mock import MagicMock
from .transactions_controller import CreateTransactionController, ListTransactionsByUserController
from src.models.schemas.transaction_schemas import TransactionCreateSchema, TransactionResponseSchema
from src.models.db_tables.transactions import TransactionType, TransactionCategory

class TestCreateTransactionController(unittest.TestCase):
  def test_create_transaction_success(self):

    mock_trans_repo = MagicMock()
    mock_acc_repo = MagicMock()
    controller = CreateTransactionController(mock_trans_repo, mock_acc_repo)

    data = {
            "user_id": 2,
            "account_id": 1,
            "amount": 100.0,
            "type": "entrada",
            "description": "Depósito",
            "category": "lazer"
      }
    validated_data = TransactionCreateSchema(**data)

    mock_transaction = MagicMock(
      user_id = 2,
      account_id = 1,
      amount = 100.00,
      type = TransactionType.ENTRADA,
      description = "depósito",
      category = "lazer",
      created_at="2024-06-25T12:00:00"
    )
    mock_trans_repo.create_transaction.return_value = mock_transaction
    mock_acc = MagicMock(saldo=200.0, id=1)
    mock_acc_repo.get_account_by_id.return_value = mock_acc
    mock_acc_repo.update_balance.return_value = True
    
    result = controller.create_transaction(data)

    print(result)

    mock_trans_repo.create_transaction.assert_called_once()
    mock_acc_repo.get_account_by_id.assert_called_once_with(1)
    mock_acc_repo.update_balance.assert_called_once()
    self.assertEqual(result.account_id, 1)
    self.assertEqual(result.amount, 100.0)


class TestListTransactionsByUser(unittest.TestCase):
  def setUp(self):
    self.mock_repo = MagicMock()
    self.controller = ListTransactionsByUser(self.mock_repo)

  def test_list_transactions_by_user_success(self):
    transaction_1 = MagicMock(
            user_id=1,
            account_id=1,
            description='Depósito',
            amount=100.0,
            type='entrada',
            category='salário',
            id=1,
            created_at='2024-06-25T10:00:00'
        )
    transaction_2 = MagicMock(
            user_id=1,
            account_id=1,
            description='Transferência',
            amount=50.0,
            type='saida',
            category='lazer',
            id=2,
            created_at='2024-06-25T11:00:00'
        )
      
    self.mock_repo.get_transaction_by_user_id.return_value = [transaction_1, transaction_2]

    result = self.controller.list_transactions_by_user(user_id = 1)

    print(result)

    self.assertIsInstance(result, list)
    self.assertEqual(len(result), 2)
    self.assertIsInstance(result[0], TransactionResponseSchema)
    self.assertEqual(result[0].description, 'Depósito')
    self.assertEqual(result[1].amount, 50.0)