#!/usr/bin/env python3
"""
filtered_logger module
"""

from typing import List
import re
import os
import logging
import mysql.connector

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(fields: List[str], redaction: str,
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


def get_db() -> mysql.connector.connection.MySQLConnection:
    """get_db fun"""
    host = os.getenv('PERSONAL_DATA_DB_HOST') or 'localhost'
    user = os.getenv('PERSONAL_DATA_DB_USERNAME') or 'root'
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD') or ''
    database = os.getenv('PERSONAL_DATA_DB_NAME')
    mydb = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    return mydb


def main():
    """main fun"""
    mydb = get_db()
    cursor = mydb.cursor()
    cursor.execute('SELECT * FROM users;')
    users = cursor.fetchall()
    logger = get_logger()
    for user in users:
        message = f'{PII_FIELDS[0]}={user[0]}; ' + \
                  f'{PII_FIELDS[1]}={user[1]}; ' + \
                  f'{PII_FIELDS[2]}={user[2]}: ' + \
                  f'{PII_FIELDS[3]}={user[3]}; ' + \
                  f'{PII_FIELDS[4]}={user[4]}'
        logger.info(message)
    cursor.close()
    mydb.close()


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """format fun"""
        message = super().format(record)
        return filter_datum(self.fields, self.REDACTION,
                            message, self.SEPARATOR)
