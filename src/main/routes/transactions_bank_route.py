from flask import Blueprint, jsonify, request, g
from src.views.http_types.http_request import HttpRequest
from src.main.middleware.auth_jwt import auth_verify_jwt
from src.main.composers.transactions_composer import create_transaction_composer, list_transactions_composer

transactions_bank_routes_bp = Blueprint("transactions_routes", __name__)

@transactions_bank_routes_bp.route("/bank/users/<user_id>/account/<account_id>/transactions/create", methods = ["POST"])
@auth_verify_jwt
def create_transaction(user_id, account_id):
  """
    Creates a new transaction for a user's account.
    With user_id & account_id as path parameters. The remaining required data must be provided in the request body

  ---
  summary: Create a new transaction
  description: "Creates a new transaction for a user's account. Requires a valid JWT token in the Authorization header."
  tags:
    - Transactions
  security:
    - Bearer: []
  consumes:
    - application/json
  produces:
    - application/json
  parameters:
    - in: path
      name: user_id
      required: true
      type: integer
      description: "ID of the user performing the transaction."
    - in: path
      name: account_id
      required: true
      type: integer
      description: "ID of the account where the transaction will be registered."
    - in: header
      name: Authorization
      required: true
      type: string
      description: "JWT token with Bearer prefix. Example: Bearer eyJhbGciOiJI..."
    - in: body
      name: body
      required: true
      schema:
        type: object
        required:
          - amount
          - type
          - category
        properties:
          amount:
            type: number
            example: 250.00
            description: Transaction amount.
          type:
            type: string
            enum: [entrada, saida]
            example: entrada
            description: "Transaction type. Allowed values: 'entrada' (income), 'saida' (expense)."
          category:
            type: string
            enum: [lazer, saude, alimentacao, outros, transporte, educacao, moradia]
            example: outros
            description: "Transaction category. Allowed values: 'lazer', 'saude', 'alimentacao', 'outros', 'transporte', 'educacao', 'moradia'."
          description:
            type: string
            example: Salary for July
            description: Optional transaction description.
  responses:
    201:
      description: Transaction successfully created
      schema:
        type: object
        properties:
          data:
            type: object
            properties:
              id:
                type: integer
                example: 13
              user_id:
                type: integer
                example: 8
              account_id:
                type: integer
                example: 7
              amount:
                type: number
                example: 1250.00
              type:
                type: string
                example: entrada
              category:
                type: string
                example: outros
              description:
                type: string
                example: Salary for July
              created_at:
                type: string
                example: "Wed, 02 Jul 2025 15:37:12 GMT"
    400:
      description: Invalid input data
    401:
      description: Unauthorized (missing or invalid token)
  """
  http_request = HttpRequest(
    body = request.json,
    params = {"user_id": user_id, "account_id":account_id},
    token_infos=g.token_informations
  )

  http_response = create_transaction_composer().handle(http_request)

  return jsonify(http_response.body), http_response.status_code



@transactions_bank_routes_bp.route("/bank/users/<user_id>/get_transactions", methods = ["GET"])
@auth_verify_jwt
def get_transactions_by_user(user_id):
  """
    Retrieves all transactions for the specified user.

    ---
    tags:
      - Transactions
    summary: List user transactions
    description: "Retrieves a list of all transactions for the given user. Requires a valid JWT token in the 'Authorization' header."
    security:
      - Bearer: []
    parameters:
      - in: path
        name: user_id
        schema:
          type: integer
        required: true
        description: "ID of the user whose transactions will be listed."
      - in: header
        name: Authorization
        schema:
          type: string
        required: true
        description: "JWT token with Bearer prefix. Example: Bearer eyJhbGciOi..."
    responses:
      200:
        description: List of transactions returned successfully
      401:
        description: Unauthorized (missing or invalid token)
      404:
        description: User not found
    """
  http_request = HttpRequest(
    params = {"user_id": user_id},
    token_infos=g.token_informations 
  )

  http_response = list_transactions_composer().handle(http_request=http_request)

  return jsonify(http_response.body), http_response.status_code
