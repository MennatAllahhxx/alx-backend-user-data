#!/usr/bin/env python3
""" Module of Authorization
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """AI is creating summary for require_auth

        Args:
            path (str): [description]
            excluded_paths (List[str]): [description]

        Returns:
            bool: [description]
        """
        return False

    def authorization_header(self, request=None) -> str:
        """AI is creating summary for authorization_header

        Args:
            request ([type], optional): [description]. Defaults to None.

        Returns:
            str: [description]
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """AI is creating summary for current_user
        """
        return None
