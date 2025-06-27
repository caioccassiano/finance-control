from flask import Flask
from src.models.config.connection import db_connection_handler
from src.main.routes.users_bank_route import users_bank_routes_bp

db_connection_handler.connect_to_db()

app = Flask(__name__)

app.register_blueprint(users_bank_routes_bp)


