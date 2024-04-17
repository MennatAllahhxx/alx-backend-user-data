#!/usr/bin/env python3
""" Module of Basic Authorization
"""
from api.v1.auth.auth import Auth
from typing import TypeVar, List
from models.user import User
import base64


class BasicAuth(Auth):
    """BasicAuth class"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """AI is creating summary for extract_base64_authorization_header

        Args:
            authorization_header (str): auth token (basic + token)

        Returns:
            str: token
        """
        if authorization_header is None or\
           not isinstance(authorization_header, str) or \
           authorization_header[0:6] != "Basic ":
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """AI is creating summary for decode_base64_authorization_header

        Args:
            base64_authorization_header (str): encoded base64 token

        Returns:
            str: decoded value as UTF8 string
        """
        if base64_authorization_header is None or \
           not isinstance(base64_authorization_header, str):
            return None

        try:
            return base64.\
                   b64decode(base64_authorization_header).\
                   decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> (str, str):
        """AI is creating summary for extract_user_credentials

        Args:
            str ([type]): [description]
        """

        if decoded_base64_authorization_header is None or\
           not isinstance(decoded_base64_authorization_header, str)\
           or ':' not in decoded_base64_authorization_header:
            return (None, None)
        info = decoded_base64_authorization_header.split(":")
        return (info[0], info[1])

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """AI is creating summary for user_object_from_credentials

        Args:
            self ([type]): [description]
        """
        if user_email is None or\
           not isinstance(user_email, str) or\
           user_pwd is None or\
           not isinstance(user_pwd, str):
            return None

        user = User.search({"email": user_email})
        if not user:
            return None
        if user[0].is_valid_password(user_pwd):
            return user[0]
        else:
            return None
