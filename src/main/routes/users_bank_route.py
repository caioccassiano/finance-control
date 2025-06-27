from flask import Blueprint, jsonify, request, g
from src.views.http_types.http_request import HttpRequest
from src.main.composers.users_composer import user_creator_composer, user_login_composer, user_delete_composer

from src.main.middleware.auth_jwt import auth_verify_jwt

users_bank_routes_bp = Blueprint("users_routes", __name__)

@users_bank_routes_bp.route("/bank/user/create", methods=["POST"])
def create_user():
  http_request = HttpRequest(body=request.json)
  http_response = user_creator_composer().handle(http_request)

  return jsonify(http_response.body), http_response.status_code

@users_bank_routes_bp.route("/bank/user/login", methods=["POST"])
def login_user():
  http_request = HttpRequest(body=request.json)
  http_response = user_login_composer().handle(http_request)

  return jsonify(http_response.body), http_response.status_code


@users_bank_routes_bp.route("/bank/user/delete", methods=["DELETE"])
@auth_verify_jwt
def delete_user(user_id):
  http_request = HttpRequest(
    body=request.json,
    params={"user_id": user_id},
    token_infos = g.token_informations,
    headers = request.headers
  )
  http_response = user_delete_composer().handle(http_request)
  return jsonify(http_response.body), http_response.status_code

