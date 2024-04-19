#!/usr/bin/env python3
""" Module of Session Authentication views
"""
import os
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """ POST /auth_session/login
    Return:
      - User object JSON represented
    """
    email = request.form.get('email')
    pswd = request.form.get('password')
    if email is None or email == "":
        return jsonify({"error": "email missing"}), 400

    if pswd is None or pswd == "":
        return jsonify({"error": "password missing"}), 400

    user = User.search({'email': email})

    if not user:
        return jsonify({"error": "no user found for this email"}), 404

    if not user[0].is_valid_password(pswd):
        return jsonify({"error": "wrong password"}), 404

    from api.v1.app import auth

    session_id = auth.create_session(user[0].id)
    data = jsonify(user[0].to_json())
    session_cookie = os.getenv('SESSION_NAME')

    data.set_cookie(session_cookie, session_id)

    return data
