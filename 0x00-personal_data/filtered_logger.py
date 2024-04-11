#!/usr/bin/env python3
"""
filtered_logger module
"""

from typing import List
import re
import logging

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(fields: tuple, redaction: str,
                 message: str, separator: str) -> str:
    """filter_datum fun"""
    for field in fields:
        message = re.sub(f'({re.escape(field)})(.*?){re.escape(separator)}',
                         rf'\1={redaction}{separator}',
                         message, flags=re.DOTALL)
    return message


def get_logger() -> logging.Logger:
    """get_logger fun"""
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    hdlr = logging.StreamHandler()
    fmt = RedactingFormatter(fields=PII_FIELDS)
    hdlr.setFormatter(fmt)
    logger.addHandler(hdlr)
    return logger


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: tuple):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """format fun"""
        message = super().format(record)
        return filter_datum(self.fields, self.REDACTION,
                            message, self.SEPARATOR)
