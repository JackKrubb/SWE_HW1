from flask_mysqldb import MySQL

from app import mysql


def get_mysql() -> MySQL:
    """Get MySQL from app file.

    Args:

    Returns:
      current mysql
    """
    return mysql
