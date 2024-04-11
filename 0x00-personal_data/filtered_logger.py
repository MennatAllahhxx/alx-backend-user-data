#!/usr/bin/env python3
"""
filtered_logger module
"""

from typing import List
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """filter_datum fun"""
    for field in fields:
        message = re.sub(f'({re.escape(field)})(.*?){re.escape(separator)}',
                         rf'\1={redaction}{separator}',
                         message, flags=re.DOTALL)
    return message
