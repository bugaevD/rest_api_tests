import pytest
import requests

API_URL = "https://book-club.qa.guru/api/v1"
USERNAME = "bugaev"
PASSWORD = "qwerty"


@pytest.fixture
def auth():
    auth_body = {"username": USERNAME, "password": PASSWORD}
    auth_response = requests.post(API_URL + "/auth/token/", json=auth_body)
    access_token = auth_response.json()["access"]

    return {"Authorization": "Bearer " + access_token}
