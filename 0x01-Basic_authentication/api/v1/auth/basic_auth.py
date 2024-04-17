#!/usr/bin/env python3
""" Module of Basic Authorization
"""
from api.v1.auth.auth import Auth


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
