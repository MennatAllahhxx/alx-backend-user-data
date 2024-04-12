#!/usr/bin/env python3
"""
encrypt_password module
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """hash_password fun"""
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)
    return hash


def is_valid(hashed_password: bytes, password: str) -> bool:
    """is_valid fun"""
    user_bytes = password.encode('utf-8')
    result = bcrypt.checkpw(user_bytes, hashed_password)
    return result
