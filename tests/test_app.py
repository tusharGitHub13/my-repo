import pytest

from app import app as flask_app


@pytest.fixture
def client():
    flask_app.config["TESTING"] = True
    with flask_app.test_client() as client:
        yield client


def test_app_is_flask_instance():
    assert hasattr(flask_app, "wsgi_app")


def test_root_returns_hello(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.get_data(as_text=True) == "Hello from my containerized WSL app!"
