#!/usr/bin/env python3
"""
Auth Module
"""

from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import bcrypt
import uuid


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


def _generate_uuid() -> str:

    """AI is creating summary for _generate_uuid

    Returns:
        str: uuid
    """
    return str(uuid.uuid4())


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

    def valid_login(self, email: str, password: str) -> bool:
        """AI is creating summary for valid_login

        Args:
            email (str): user email
            password (str): user password

        Returns:
            bool: true if valid password
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        return bcrypt.checkpw(password.encode('utf-8'), user.hashed_password)

    def create_session(self, email: str) -> str:
        """AI is creating summary for create_session

        Args:
            email (str): user email

        Returns:
            str: session id
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id: str) -> User:
        """AI is creating summary for get_user_from_session_id

        Args:
            session_id (str): session id

        Returns:
            User: corresponding user
        """
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None
        return user

    def destroy_session(self, user_id: int) -> None:
        """AI is creating summary for destroy_session

        Args:
            user_id (int): user id
        """
        try:
            self._db.update_user(user_id, session_id=None)
        except ValueError:
            pass
        return None
