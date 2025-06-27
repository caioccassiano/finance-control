from flask import Blueprint, jsonify, request, g
from src.views.http_types.http_request import HttpRequest
from src.main.middleware.auth_jwt import auth_verify_jwt
from src.main.composers.accounts_composer import list_accounts_composer, create_account_composer, delete_account_composer


accounts_bank_routes_bp = Blueprint("accounts_routes", __name__)

@accounts_bank_routes_bp.route("/bank/account/create/<user_id>", methods = ["POST"])
@auth_verify_jwt
def create_account(user_id):
  http_request = HttpRequest(
    params={"user_id": user_id},
    token_infos = g.token_informations
  )
  http_response = create_account_composer().handle(http_request)

  return jsonify({"data": http_response.body}), http_response.status_code




