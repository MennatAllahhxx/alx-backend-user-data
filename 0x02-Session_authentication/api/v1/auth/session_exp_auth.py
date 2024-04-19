#!/usr/bin/env python3
""" Module of Session Expiration Authorization
"""
from api.v1.auth.session_auth import SessionAuth
from typing import TypeVar, List
from models.user import User
import datetime
import base64
import os


class SessionExpAuth(SessionAuth):
    """SessionExpAuth class"""

    def __init__(self) -> None:
        """AI is creating summary for __init__
        """
        self.session_duration = int(os.getenv('SESSION_DURATION', 0))

    def create_session(self, user_id=None):
        """AI is creating summary for create_session

        Args:
            user_id ([type], optional): user id. Defaults to None.

        Returns:
            str: session id
        """
        session_id = super().create_session(user_id)
        if not session_id:
            return None
        session_dictionary = {'user_id': user_id,
                              'created_at': datetime.datetime.now()}
        self.user_id_by_session_id[session_id] = session_dictionary
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """AI is creating summary for user_id_for_session_id

        Args:
            session_id ([type], optional): session id. Defaults to None.

        Returns:
            str: user id
        """
        if session_id is None:
            return None
        session_dictionary = self.user_id_by_session_id.get(session_id)
        if not session_dictionary:
            return None
        user_id = session_dictionary.get('user_id')
        if self.session_duration <= 0:
            return user_id
        created_at = session_dictionary.get('created_at')
        if not created_at:
            return None
        duration = created_at +\
            datetime.timedelta(seconds=self.session_duration)
        if duration < datetime.datetime.now():
            return None
        return user_id
