#!/usr/bin/env python3
""" Module of Basic Authorization
"""
from api.v1.auth.auth import Auth
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
