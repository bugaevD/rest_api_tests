import requests
from jsonschema import validate

from schemas.register_user_schema import success_register

API_URL = "https://book-club.qa.guru/api/v1"
USERNAME = "bugaev"
PASSWORD = "qwerty"

def test_register_user():
    request_body = {"username": USERNAME, "password": PASSWORD}
    response = requests.post(API_URL + "/users/register/", json=request_body)

    print("\nStatus code: ", response.status_code)
    print("Body: ", response.text)

    assert response.status_code == 201

    body = response.json()
    validate(body, schema=success_register)

