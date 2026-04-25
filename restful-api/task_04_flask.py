from flask import Flask, jsonify, request

# Create the Flask application
app = Flask(__name__)

# -------------------------------------------------------
# Empty dictionary to store users in memory
# username is the key, user details are the value
# -------------------------------------------------------
users = {}


# -------------------------------------------------------
# ENDPOINT 1: Home page - GET /
# -------------------------------------------------------
@app.route("/")
def home():
    return "Welcome to the Flask API!"


# -------------------------------------------------------
# ENDPOINT 2: All users - GET /data
# Returns list of all usernames
# -------------------------------------------------------
@app.route("/data")
def get_data():
    # Return just the list of usernames (keys)
    return jsonify(list(users.keys()))


# -------------------------------------------------------
# ENDPOINT 3: Status check - GET /status
# -------------------------------------------------------
@app.route("/status")
def status():
    return "OK"


# -------------------------------------------------------
# ENDPOINT 4: Single user - GET /users/<username>
# Returns full user object including username field
# -------------------------------------------------------
@app.route("/users/<username>")
def get_user(username):
    if username in users:
        # Return user data including the username field
        user_data = {"username": username}
        user_data.update(users[username])
        return jsonify(user_data)
    else:
        # User not found - return 404 error
        return jsonify({"error": "User not found"}), 404


# -------------------------------------------------------
# ENDPOINT 5: Add new user - POST /add_user
# -------------------------------------------------------
@app.route("/add_user", methods=["POST"])
def add_user():
    # Retrieve the incoming JSON data
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

    # Build response with username included
    user_response = {"username": username}
    user_response.update(users[username])

    # Return a success response with 201 status
    return jsonify({"message": "User added", "user": user_response}), 201


# -------------------------------------------------------
# Start the server
# -------------------------------------------------------
if __name__ == "__main__":
    app.run()
