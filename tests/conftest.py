import pytest
from flask import Flask
from flask.testing import FlaskClient

from app import create_app


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
    yield app2


@pytest.fixture()
def client(app2: Flask) -> FlaskClient:
    """Create test_client for current flask application."""
    return app2.test_client()
