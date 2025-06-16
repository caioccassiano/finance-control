from .connection import db_connection_handler
from sqlalchemy.engine import Engine
import pytest

@pytest.mark.skip(reason="interation with db")
def test_db_connection():
  assert db_connection_handler.get_engine() is None

  db_connection_handler.connect_to_db()
  db_engine = db_connection_handler.get_engine()

  assert db_engine is not None
  assert isinstance(db_engine, Engine)

