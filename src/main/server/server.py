from flask import Flask
from src.models.config.connection import db_connection_handler
from src.main.routes.users_bank_route import users_bank_routes_bp
from src.main.routes.accounts_bank_routes import accounts_bank_routes_bp
from src.models.config.base import Base
from src.models.db_tables.transactions import Transactions

db_connection_handler.connect_to_db()
engine = db_connection_handler.get_engine()
Base.metadata.create_all(engine)

app = Flask(__name__)

app.register_blueprint(users_bank_routes_bp)
app.register_blueprint(accounts_bank_routes_bp)


