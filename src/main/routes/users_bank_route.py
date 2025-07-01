from flask import Blueprint, jsonify, request, g
from src.views.http_types.http_request import HttpRequest
from src.main.composers.users_composer import user_creator_composer, user_login_composer, user_delete_composer

from src.main.middleware.auth_jwt import auth_verify_jwt

users_bank_routes_bp = Blueprint("users_routes", __name__)

@users_bank_routes_bp.route("/bank/user/create", methods=["POST"])
def create_user():
  '''
  Create a new user.

  This endpoint creates a new user in the system.
  All required user data must be provided in the request body

  ---
  tags:
      - Users
  summary: Create user
  description: Register a new user in the system.
  parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            username:
              type: string
              example: mariaaugustav
            email:
              type: string
              example: gutav@email.com
            password:
              type: string
              example: MySecretPassword123
          required:
            - username
            - email
            - password
  responses:
      201:
        description: User successfully created
      400:
        description: Invalid input data
      409:
        description: Email already exists
  
  '''
  http_request = HttpRequest(body=request.json)
  http_response = user_creator_composer().handle(http_request)

  return jsonify(http_response.body), http_response.status_code

@users_bank_routes_bp.route("/bank/user/login", methods=["POST"])
def login_user():
  """
    Authenticates a user in the system and returns a JWT token on success.

  ---
    tags:
      - Users
    summary: Login user
    description: Authenticates a user with username and password. Returns a JWT access token if successful.
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - username
            - password
          properties:
            username:
              type: string
              example: johndoe
            password:
              type: string
              example: MySecretPassword123
    responses:
      200:
        description: Login successful, JWT token returned
        schema:
          type: object
          properties:
            access_token:
              type: string
              example: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...
      401:
        description: Invalid credentials
      400:
        description: Invalid input data
    """
  http_request = HttpRequest(body=request.json)
  http_response = user_login_composer().handle(http_request)

  return jsonify(http_response.body), http_response.status_code


@users_bank_routes_bp.route("/bank/user/delete/<user_id>", methods=["DELETE"])
@auth_verify_jwt
def delete_user(user_id):
  """
    Deletes a user from the system. Requires JWT Token in Authorization header.
    ---
    tags:
      - Users
    summary: "Delete user"
    security:
      - Bearer: []
    description: "Deletes a user by user_id. Requires a valid JWT token in the 'Authorization' header as 'Bearer <token>'."
    parameters:
      - in: path
        name: user_id
        schema:
          type: integer
        required: true
        description: The unique identifier of the user to be deleted.
      - in: header
        name: Authorization
        schema:
          type: string
        required: true
        description: "JWT token with Bearer prefix. Example: 'Bearer eyJhbGciOiJI...'"
    responses:
      200:
        description: User successfully deleted
      401:
        description: Unauthorized (invalid or missing token)
      403:
        description: Forbidden (user not allowed to delete this account)
      404:
        description: User not found
    """
  
  http_request = HttpRequest(
    params={"user_id": user_id},
    token_infos = g.token_informations,
  )
  http_response = user_delete_composer().handle(http_request)
  return jsonify(http_response.body), http_response.status_code

