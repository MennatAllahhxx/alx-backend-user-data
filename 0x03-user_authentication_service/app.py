#!/usr/bin/env python3
""" Module of App
"""
from flask import Flask, jsonify, request, abort, make_response
from auth import Auth

app = Flask(__name__)
auth = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ GET /
    Return:
      - jsonified message
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def register_user():
    """ POST /users
    Return:
      - register a user
    """
    try:
        email = request.form["email"]
        password = request.form["password"]
    except KeyError:
        abort(400)
    try:
        user = auth.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400
    return jsonify({"email": email, "message": "user created"})


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """ POST /sessions
    Return:
      - log in
    """
    try:
        email = request.form["email"]
        password = request.form["password"]
    except KeyError:
        abort(400)

    session_id = auth.create_session(email)
    if not session_id or not auth.valid_login(email, password):
        abort(401)
    response = make_response(
        jsonify({
            "email": email,
            "message": "logged in"
            }), 200
        )
    response.set_cookie("session_id", session_id)
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
