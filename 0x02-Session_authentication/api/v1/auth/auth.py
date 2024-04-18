#!/usr/bin/env python3
""" Module of Authorization
"""
import os
from typing import List, TypeVar


class Auth:
    """Auth class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """AI is creating summary for require_auth

        Args:
            path (str): path to be checked
            excluded_paths (List[str]): paths that dont require auth

        Returns:
            bool: False if path is in excluded_paths
        """
        if path is None or\
           excluded_paths is None or\
           excluded_paths == []:
            return True
        path = os.path.join(path, '')
        for pathh in excluded_paths:
            if pathh.endswith('*') and\
               path.startswith(pathh[:-1]) or\
               pathh == path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """AI is creating summary for authorization_header

        Args:
            request ([type], optional): request. Defaults to None.

        Returns:
            str: the value of the header request Authorization
        """
        if request is None:
            return None
        if "Authorization" in request.headers:
            return request.headers["Authorization"]
        else:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """AI is creating summary for current_user

        Returns:
            [type]: [description]
        """
        return None

    def session_cookie(self, request=None):
        """AI is creating summary for session_cookie

        Args:
            request ([type], optional): request to handle. Defaults to None.
        """
        if request is None:
            return None
        _my_session_id = os.getenv('SESSION_NAME')
        return request.cookies.get(_my_session_id)
