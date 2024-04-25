#!/usr/bin/env python3
"""
Auth Module
"""

import bcrypt


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
