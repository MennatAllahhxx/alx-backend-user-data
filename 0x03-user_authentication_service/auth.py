#!/usr/bin/env python3
"""
Auth Module
"""

from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import bcrypt


def _hash_password(password: str) -> bytes:
    """AI is creating summary for _hash_password

    Args:
        password (str): original password

    Returns:
        bytes: hashed password
    """
    byte = password.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(byte, salt)


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """AI is creating summary for register_user

        Args:
            email (str): [description]
            password (str): [description]

        Returns:
            User: [description]
        """
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            password = _hash_password(password)
            return self._db.add_user(email, password)
