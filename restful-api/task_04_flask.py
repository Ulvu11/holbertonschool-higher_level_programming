from flask import Flask, jsonify, request

# Create the Flask application
# __name__ tells Flask the name of this file
app = Flask(__name__)

# -------------------------------------------------------
# Dictionary to store users in memory
# username is the key, user details are the value
# -------------------------------------------------------
users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}
}


# -------------------------------------------------------
# ENDPOINT 1: Home page - GET /
# -------------------------------------------------------
@app.route("/")
def home():
    # Return a simple welcome message
    return "Welcome to the Flask API!"


# -------------------------------------------------------
# ENDPOINT 2: All users - GET /data
# -------------------------------------------------------
@app.route("/data")
def get_data():
    # Return the users dictionary in JSON format
    return jsonify(users)


# -------------------------------------------------------
# ENDPOINT 3: Status check - GET /status
# -------------------------------------------------------
@app.route("/status")
def status():
    return "OK"


# -------------------------------------------------------
# ENDPOINT 4: Single user - GET /users/<username>
# <username> is dynamic - whatever the user types
# gets passed as a variable to the function
# Example: /users/jane -> username = "jane"
# -------------------------------------------------------
@app.route("/users/<username>")
def get_user(username):
    if username in users:
        # User found - return their data
        return jsonify(users[username])
    else:
        # User not found - return 404 error
        return jsonify({"error": "User not found"}), 404


# -------------------------------------------------------
# ENDPOINT 5: Add new user - POST /add_user
# POST is used for sending data (not GET)
# -------------------------------------------------------
@app.route("/add_user", methods=["POST"])
def add_user():
    # request.get_json() retrieves the incoming JSON data
    data = request.get_json()

    # If the sent data is not valid JSON
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    # If the "username" field is missing
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # If this username already exists
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Add the new user to the users dictionary
    users[username] = {
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    # Return a success response
    return jsonify({"message": "User added", "user": users[username]}), 201


# -------------------------------------------------------
# Start the server
# -------------------------------------------------------
if __name__ == "__main__":
    app.run()
