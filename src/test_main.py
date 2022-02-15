"""Minimal tests for main.py
"""
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_main():
    """This tests if the root endpoint return 200 OK and the right message to the
user

    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello, World!"}


def test_numbers_ok():
    """This tests the response status code and details for a correct input to the
    /one-to-ten endpoint.

    """
    response = client.get("/one-to-ten/1")
    assert response.status_code == 200
    assert response.json() == {"number": {
        "binary": "0b1", "hexadecimal": "0x1", "octal": "0o1"}}


def test_numbers_bad_input():
    """This tests the response status code and details for an incorrect input to
    the /one-to-ten endpoint (non numeric input).

    """
    response = client.get("/one-to-ten/one")
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid input!"}


def test_numbers_bad_number():
    """This tests the response status code and details for an incorrect input to
    the /one-to-ten endpoint (non numeric input).

    """
    response = client.get("/one-to-ten/11")
    assert response.status_code == 422
    assert response.json() == {"detail": "Only numbers 1-10 are accepted!"}
