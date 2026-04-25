from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity, get_jwt
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# -------------------------------------------------------
# Secret key for JWT token generation and validation
# -------------------------------------------------------
app.config["JWT_SECRET_KEY"] = "super-secret-key-12345"

# -------------------------------------------------------
# Initialize Basic Auth and JWT Manager
# -------------------------------------------------------
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# -------------------------------------------------------
# Users dictionary with hashed passwords and roles
# Passwords are never stored as plain text - always hashed
# -------------------------------------------------------
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}


# -------------------------------------------------------
# BASIC AUTH: Password verification function
# Flask-HTTPAuth calls this automatically to check credentials
# -------------------------------------------------------
@auth.verify_password
def verify_password(username, password):
    # Check if username exists and password matches the hash
    if username in users and check_password_hash(users[username]["password"], password):
        return username
    return None


# -------------------------------------------------------
# ENDPOINT 1: Basic Auth protected route - GET /basic-protected
# @auth.login_required means: only allow if Basic Auth passes
# -------------------------------------------------------
@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


# -------------------------------------------------------
# ENDPOINT 2: Login route - POST /login
# User sends username + password, receives a JWT token
# -------------------------------------------------------
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON"}), 401

    username = data.get("username")
    password = data.get("password")

    # Check if user exists and password is correct
    if username not in users or not check_password_hash(users[username]["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    # Create JWT token - embed the role inside the token payload
    additional_claims = {"role": users[username]["role"]}
    access_token = create_access_token(identity=username, additional_claims=additional_claims)

    return jsonify({"access_token": access_token})


# -------------------------------------------------------
# ENDPOINT 3: JWT protected route - GET /jwt-protected
# @jwt_required() means: only allow if a valid JWT token is provided
# -------------------------------------------------------
@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


# -------------------------------------------------------
# ENDPOINT 4: Admin only route - GET /admin-only
# Requires JWT token AND the user must have "admin" role
# -------------------------------------------------------
@app.route("/admin-only")
@jwt_required()
def admin_only():
    # get_jwt() retrieves the full token payload (including our custom claims)
    claims = get_jwt()
    role = claims.get("role")

    if role != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


# -------------------------------------------------------
# JWT error handlers - must return 401 for all token errors
# -------------------------------------------------------
@jwt.unauthorized_loader
def unauthorized_response(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def invalid_token_response(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def expired_token_response(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401


# -------------------------------------------------------
# Start the server
# -------------------------------------------------------
if __name__ == "__main__":
    app.run()
