#!/usr/bin/env python3
""" Module of Authorization
"""
import os
from typing import List, TypeVar
from flask import request


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
        if os.path.join(path, '') in excluded_paths:
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
        if "Authorization" not in request.headers:
            return None
        else:
            return request.headers["Authorization"]

    def current_user(self, request=None) -> TypeVar('User'):
        """AI is creating summary for current_user

        Returns:
            [type]: [description]
        """
        return None
