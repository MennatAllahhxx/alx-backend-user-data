#!/usr/bin/env python3
""" Module of App
"""
from flask import Flask, jsonify, request, abort, make_response, redirect
from auth import Auth

app = Flask(__name__)
auth = Auth()


@app.route('/')
def index():
    """ GET /
    Return:
      - jsonified message
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def register():
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


@app.route('/sessions', methods=['POST'])
def login():
    """ POST /sessions
    Return:
      - log in
    """
    email = request.form["email"]
    password = request.form["password"]
    if auth.valid_login(email, password):
        session_id = auth.create_session(email)
        if session_id:
            response = make_response(
                jsonify({"email": email, "message": "logged in"}), 200
            )
            response.set_cookie("session_id", session_id)
            return response
    abort(401)


@app.route('/sessions', methods=['DELETE'])
def logout():
    """ DELETE /sessions
    Return:
      - log out
    """
    session_id = request.cookies.get("session_id")
    if session_id:
        user = auth.get_user_from_session_id(session_id)
        if user:
            auth.destroy_session(user.id)
            return redirect("/")
    abort(403)


@app.route('/profile', methods=["GET"])
def profile():
    """ GET /profile
    Return:
      - log out
    """
    session_id = request.cookies.get("session_id")
    if session_id:
        user = auth.get_user_from_session_id(session_id)
        if user:
            return jsonify({"email": user.email}), 200
    abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
