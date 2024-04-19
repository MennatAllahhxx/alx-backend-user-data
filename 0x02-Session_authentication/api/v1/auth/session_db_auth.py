#!/usr/bin/env python3
""" Module of Session Database Authorization
"""
import uuid
from typing import Dict
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """SessionDBAuth class"""

    def create_session(self, user_id: str = None) -> str:
        """AI is creating summary for create_session

        Args:
            user_id (str, optional): id of the user. Defaults to None.

        Returns:
            str: session id
        """
        session_id = super().create_session(user_id)
        UserSession(**{
            "user_id": user_id,
            "session_id": session_id
        }).save()
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

    def destroy_session(self, request=None):
        """AI is creating summary for destroy_session

        Args:
            request ([type], optional): [description]. Defaults to None.
        """
