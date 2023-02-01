import pytest
from flask.testing import FlaskClient

from app import app, create_app


@pytest.fixture()
def app2():
    """Create new application for testing."""
    app2 = create_app()
    app2.config.update(
        {
            "TESTING": True,
        }
    )
    yield app2


@pytest.fixture()
def client() -> FlaskClient:
    """Create test_client for current flask application."""
    return app.test_client()
