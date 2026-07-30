import pytest
import requests
from jsonschema import validate

from schemas.auth_schema import success_auth_schema, get_user_schema, unsuccessful_auth_schema, \
    blank_both_fields_schema, blank_password_schema, blank_username_schema, missing_password_schema, \
    missing_username_schema, missing_both_fields_schema, unsupported_content_type_auth_schema, invalid_json_schema, \
    invalid_body_type_schema, none_body_type_schema

API_URL = "https://book-club.qa.guru/api/v1"
USERNAME = "bugaev"
PASSWORD = "qwerty"


def test_success_auth():
    request_body = {"username": USERNAME, "password": PASSWORD}
    response = requests.post(API_URL + "/auth/token/", json=request_body)

    print("\nStatus code: ", response.status_code)
    print("Body: ", response.text)

    assert response.status_code == 200

    body = response.json()
    validate(body, schema=success_auth_schema)

    access_token = body["access"]
    refresh_token = body["refresh"]

    assert access_token in body["access"]
    assert refresh_token in body["refresh"]
    assert len(access_token.split(".")) == 3
    assert len(refresh_token.split(".")) == 3
    assert access_token != refresh_token

    return access_token


def test_get_user():
    headers = {"Authorization": "Bearer " + test_success_auth()}
    response = requests.get(API_URL + "/users/me/", headers=headers)

    print("\nStatus code: ", response.status_code)
    print("Body: ", response.text)

    assert response.status_code == 200

    body = response.json()
    validate(body, schema=get_user_schema)

    assert body["id"] == 306
    assert body["username"] == USERNAME


@pytest.mark.parametrize("username,password,status_code,schema", [
    (USERNAME, "WrongPassword", 401, unsuccessful_auth_schema),
    ("WrongUsername", PASSWORD, 401, unsuccessful_auth_schema),
    ("' OR '1'='1", PASSWORD, 401, unsuccessful_auth_schema),
    (USERNAME, "' OR '1'='1", 401, unsuccessful_auth_schema),
    ("<script>alert(1)</script>", PASSWORD, 401, unsuccessful_auth_schema)
])
def test_wrong_credentials_auth(username, password, status_code, schema):
    request_body = {"username": username, "password": password}
    response = requests.post(API_URL + "/auth/token/", json=request_body)

    print("\nStatus code: ", response.status_code)
    print("Body: ", response.text)

    assert response.status_code == status_code

    body = response.json()
    validate(body, schema=schema)

    assert "Invalid username or password." == body["detail"]


@pytest.mark.parametrize("username,password,status_code,schema,body_key", [
    ("", "", 400, blank_both_fields_schema, ["username", "password"]),
    (" ", " ", 400, blank_both_fields_schema, ["username", "password"]),
    (USERNAME, "", 400, blank_password_schema, ["password"]),
    ("", PASSWORD, 400, blank_username_schema, ["username"]),
    (USERNAME, "   ", 400, blank_password_schema, ["password"]),
    ("   ", PASSWORD, 400, blank_username_schema, ["username"]),
])
def test_blank_fields_auth(username, password, status_code, schema, body_key):
    request_body = {"username": username, "password": password}
    response = requests.post(API_URL + "/auth/token/", json=request_body)

    print("\nStatus code: ", response.status_code)
    print("Body: ", response.text)

    assert response.status_code == status_code

    body = response.json()
    validate(body, schema=schema)
    for key in body_key:
        assert ["This field may not be blank."] == body[key]

@pytest.mark.parametrize("request_body,status_code,schema, body_key",[
    ({"username": USERNAME}, 400, missing_password_schema, "password"),
    ({"password": PASSWORD}, 400, missing_username_schema, "username"),
    ({}, 400, missing_both_fields_schema, "username"),
])
def test_missing_required_field_auth(request_body, status_code, schema, body_key):
    response = requests.post(API_URL + "/auth/token/", json=request_body)

    print("\nStatus code: ", response.status_code)
    print("Body: ", response.text)

    assert response.status_code == status_code

    body = response.json()
    validate(body, schema=schema)

    assert ['This field is required.'] == body[body_key]

@pytest.mark.parametrize("request_body,status_code,headers,schema", [
    ({"username": USERNAME, "password": PASSWORD}, 415, {"content-type": "image/png"}, unsupported_content_type_auth_schema),
    ({"username": USERNAME, "password": PASSWORD}, 415, {"content-type": "application/xml"}, unsupported_content_type_auth_schema),
(   {"username": USERNAME, "password": PASSWORD}, 415, {"content-type": "text/html"}, unsupported_content_type_auth_schema),
])
def test_wrong_content_type_auth(request_body, status_code, headers, schema):
    response = requests.post(API_URL + "/auth/token/", headers=headers ,json=request_body)

    print("\nStatus code: ", response.status_code)
    print("Body: ", response.text)

    assert response.status_code == status_code

    body = response.json()
    validate(body, schema=schema)

    assert "Unsupported media type" in body["detail"]

def test_invalid_json_auth():
    request_body = "<xml><username>bugaev</username><password>qwerty</password></xml>"
    response = requests.post(API_URL + "/auth/token/", headers={"Content-Type": "application/json"}, data=request_body)

    print("\nStatus code: ", response.status_code)
    print("Body: ", response.text)

    assert response.status_code == 400

    body = response.json()
    validate(body, schema=invalid_json_schema)


@pytest.mark.parametrize("request_body,status_code,schema", [
    (None, 400, none_body_type_schema),
    (True, 400, invalid_body_type_schema),
    (123, 400, invalid_body_type_schema),
    ("text", 400, invalid_body_type_schema),
    ([], 400, invalid_body_type_schema),
])
def test_invalid_body_type_auth(request_body, status_code,schema):
    response = requests.post(API_URL + "/auth/token/", json=request_body)

    print("\nStatus code: ", response.status_code)
    print("Body: ", response.text)

    assert response.status_code == status_code

    body = response.json()
    validate(body, schema=schema)