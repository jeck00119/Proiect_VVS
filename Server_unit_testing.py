# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
import pytest
import webserver


@pytest.fixture
def client():
    app = webserver.app
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_root(client):
    rv = client.get("/")

    assert 200 == rv.status_code


def test_site1(client):
    rv = client.get("/site1")
    assert 200 == rv.status_code


def test_site2(client):
    rv = client.get("/site2")
    assert 200 == rv.status_code


def test_404_not_found(client):
    rv = client.get('/nothinghere')
    assert 404 == rv.status_code


def test_maintenance(client):
    rv = client.get("/maintenance")
    assert 503 == rv.status_code
    rv = client.get("/")
    assert '503 SERVICE UNAVAILABLE' == rv.status
