import pymysql

pymysql.install_as_MySQLdb()
import pytest
from flask import Flask
from flask.testing import FlaskClient
from flask_mysqldb import MySQL

from app import create_app
from sql.sql_connection import Connection

mysql = MySQL()


def make_database():
    sql_connection = Connection(mysql)
    mysql_script_file = open("tests/swe_vending.sql", "r")
    lines = mysql_script_file.readlines()
    for line in lines:
        sql_connection.execute(line)


@pytest.fixture()
def app2():
    """Create new application for testing."""
    app2 = create_app()
    app2.config.update(
        {
            "TESTING": True,
        }
    )
    app2.config.update(
        {
            "WTF_CSRF_CHECK_DEFAULT": False,
        }
    )
    with app2.app_context():
        make_database()
    yield app2


@pytest.fixture()
def client(app2: Flask) -> FlaskClient:
    """Create test_client for current flask application."""
    return app2.test_client()
