from flask import Blueprint, jsonify, request, g
from src.views.http_types.http_request import HttpRequest
from src.main.middleware.auth_jwt import auth_verify_jwt
from src.main.composers.transactions_composer import create_transaction_composer, list_transactions_composer

transactions_bank_routes_bp = Blueprint("transactions_routes", __name__)

@transactions_bank_routes_bp.route("/bank/users/<user_id>/account/<account_id>/transactions/create", methods = ["POST"])
@auth_verify_jwt
def create_transaction(user_id, account_id):
  http_request = HttpRequest(
    body = request.json,
    params = {"user_id": user_id, "account_id":account_id},
    token_infos=g.token_informations
  )

  http_response = create_transaction_composer().handle(http_request)

  return jsonify(http_response.body), http_response.status_code


