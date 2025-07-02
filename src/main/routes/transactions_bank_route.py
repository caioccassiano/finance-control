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
  summary: Cria uma nova transação para a conta do usuário.
  description: Cria uma transação vinculada à conta de um usuário. Campos `type` e `category` são enums e aceitam apenas valores específicos.
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
      description: "ID do usuário responsável pela transação."
    - in: path
      name: account_id
      required: true
      type: integer
      description: "ID da conta onde a transação será registrada."
    - in: header
      name: Authorization
      required: true
      type: string
      description: "JWT token com prefixo Bearer. Exemplo: Bearer eyJhbGciOiJI..."
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
            example: 250.0
            description: Valor da transação.
          type:
            type: string
            enum: [entrada, saida]
            example: entrada
            description: "Tipo da transação. Valores possíveis: `entrada` (receita), `saida` (despesa)."
          category:
            type: string
            enum: [lazer, saude, alimentacao, outros, transporte, educacao, moradia]
            example: outros
            description: "Categoria da transação. Valores possíveis: `lazer`, `saude`, `alimentacao`, `outros`, `transporte`, `educacao`, `moradia`."
          description:
            type: string
            example: Salário de Julho
            description: "Descrição opcional para a transação."
  responses:
    201:
      description: Transação criada com sucesso.
    400:
      description: Dados inválidos.
    401:
      description: Não autorizado (token inválido ou ausente).
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
