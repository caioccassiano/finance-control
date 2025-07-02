from flask import Blueprint, jsonify, request, g
from src.views.http_types.http_request import HttpRequest
from src.main.middleware.auth_jwt import auth_verify_jwt
from src.main.composers.accounts_composer import list_accounts_composer, create_account_composer, delete_account_composer


accounts_bank_routes_bp = Blueprint("accounts_routes", __name__)

@accounts_bank_routes_bp.route("/bank/account/create/<user_id>", methods = ["POST"])
@auth_verify_jwt
def create_account(user_id):
  """
    Creates a new account for a given user.

    ---
    tags:
      - Accounts
    summary: Create account
    description: "Creates a new account for the specified user. Requires a valid JWT token."
    security:
      - Bearer: []
    parameters:
      - in: path
        name: user_id
        schema:
          type: integer
        required: true
        description: "ID of the user to whom the account will belong."
      - in: header
        name: Authorization
        schema:
          type: string
        required: true
        description: "JWT token with Bearer prefix. Example: Bearer eyJhbGciOi..."
    responses:
      201:
        description: Account successfully created
      400:
        description: Invalid input data
      401:
        description: Unauthorized (missing or invalid token)
    """
  http_request = HttpRequest(
    params={"user_id": user_id},
    token_infos = g.token_informations
  )
  http_response = create_account_composer().handle(http_request)

  return jsonify({"data": http_response.body}), http_response.status_code



@accounts_bank_routes_bp.route("/bank/account/users_accounts/<user_id>", methods = ["GET"])
@auth_verify_jwt
def list_accounts(user_id):
  """
    Retrieves all accounts for a given user.

    ---
    tags:
      - Accounts
    summary: List accounts by user
    description: "Returns all accounts associated with the specified user. Requires a valid JWT token in the 'Authorization' header."
    security:
      - Bearer: []
    parameters:
      - in: path
        name: user_id
        schema:
          type: integer
        required: true
        description: "ID of the user whose accounts will be listed."
      - in: header
        name: Authorization
        schema:
          type: string
        required: true
        description: "JWT token with Bearer prefix. Example: Bearer eyJhbGciOi..."
    responses:
      200:
        description: List of accounts successfully returned
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
      401:
        description: Unauthorized (missing or invalid token)
      404:
        description: User not found
    """
  http_request = HttpRequest(
    params = {"user_id": user_id},
    token_infos = g.token_informations
  )

  http_response = list_accounts_composer().handle(http_request)

  return jsonify(http_response.body), http_response.status_code


@accounts_bank_routes_bp.route("/bank/users/<user_id>/accounts/<account_id>", methods = ["DELETE"])
@auth_verify_jwt
def delete_account(user_id, account_id):
  """
    Deletes an account for a user.

    ---
    tags:
      - Accounts
    summary: Delete account
    description: "Deletes the specified account for the user. Requires a valid JWT token in the 'Authorization' header as 'Bearer <token>'."
    security:
      - Bearer: []
    parameters:
      - in: path
        name: user_id
        schema:
          type: integer
        required: true
        description: "The user ID that owns the account."
      - in: path
        name: account_id
        schema:
          type: integer
        required: true
        description: "The account ID to be deleted."
      - in: header
        name: Authorization
        schema:
          type: string
        required: true
        description: "JWT token with Bearer prefix. Example: Bearer eyJhbGciOi..."
    responses:
      200:
        description: Account successfully deleted
      401:
        description: Unauthorized (invalid or missing token)
      403:
        description: Forbidden (not allowed to delete this account)
      404:
        description: User or account not found
    """
  http_request = HttpRequest(
    params={"user_id": user_id, "account_id":account_id},
    token_infos=g.token_informations
  )

  http_response = delete_account_composer().handle(http_request)

  return jsonify(http_response.body), http_response.status_code
