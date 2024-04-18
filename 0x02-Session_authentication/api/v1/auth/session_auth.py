#!/usr/bin/env python3
""" Module of Session Authorization
"""
import uuid
from typing import Dict
from api.v1.auth.auth import Auth
from models.user import User


class SessionAuth(Auth):
    """SessionAuth class"""

    user_id_by_session_id: Dict[str, str] = {}

    def create_session(self, user_id: str = None) -> str:
        """AI is creating summary for create_session

        Args:
            user_id (str, optional): id of the user. Defaults to None.

        Returns:
            str: session id
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """AI is creating summary for user_id_for_session_id

        Args:
            session_id (str, optional): id of the session. Defaults to None.

        Returns:
            str: user id of that session
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """AI is creating summary for current_user

        Args:
            request ([type], optional): request to handle. Defaults to None.
        """
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        return User.get(user_id)
