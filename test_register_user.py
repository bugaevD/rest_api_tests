import pytest
import requests
from jsonschema import validate
from faker import Faker

from schemas.register_user_schema import success_register, blank_password_schema, blank_both_fields_schema, \
    very_long_username_schema, very_long_password_schema, very_long_both_fields_schema, invalid_username_schema, \
    already_registered_schema, very_short_username_schema, very_short_password_schema, very_short_both_fields_schema, \
    missing_username_schema, missing_password_schema, missing_both_fields_schema, \
    unsupported_content_type_registred_schema, invalid_json_schema, invalid_body_type_schema, none_body_type_schema
from schemas.register_user_schema import blank_username_schema

fake = Faker()
API_URL = "https://book-club.qa.guru/api/v1"
USERNAME = "bugaev"
PASSWORD = "qwerty"


def test_register_user():
    request_body = {"username": fake.user_name(), "password": fake.password()}
    response = requests.post(API_URL + "/users/register/", json=request_body)

    print("\nStatus code: ", response.status_code)
    print("Body: ", response.text)

    assert response.status_code == 201

    body = response.json()
    validate(body, schema=success_register)

    assert USERNAME == body["username"]


def test_register_with_existing_username():
    request_body = {"username": USERNAME, "password": PASSWORD}
    response = requests.post(API_URL + "/users/register/", json=request_body)

    print("\nStatus code: ", response.status_code)
    print("Body: ", response.text)

    assert response.status_code == 400

    body = response.json()
    validate(body, schema=already_registered_schema)

    assert body["username"] == ['A user with that username already exists.']


@pytest.mark.parametrize("username,password,status_code,schema,body_key", [
    (fake.user_name(), "", 400, blank_password_schema, ["password"]),
    ("", fake.password(), 400, blank_username_schema, ["username"]),
    ("", "", 400, blank_both_fields_schema, ["username", "password"]),
    ("   ", "   ", 400, blank_both_fields_schema, ["username", "password"]),
    ("   ", fake.password(), 400, blank_username_schema, ["username"]),
    (fake.user_name(), "   ", 400, blank_password_schema, ["password"]),
])
def test_blank_fields_register_user(username, password, status_code, schema, body_key):
    request_body = {"username": username, "password": password}
    response = requests.post(API_URL + "/users/register/", json=request_body)

    print("\nStatus code: ", response.status_code)
    print("Body: ", response.text)

    assert response.status_code == status_code

    body = response.json()
    validate(body, schema=schema)
    for key in body_key:
        assert body[key] == ["This field may not be blank."]


def test_very_long_username():
    request_body = {"username": "A" * 151, "password": fake.password()}
    response = requests.post(API_URL + "/users/register/", json=request_body)

    print("\nStatus code: ", response.status_code)
    print("Body: ", response.text)

    assert response.status_code == 400

    body = response.json()
    validate(body, schema=very_long_username_schema)

    assert body["username"] == ['Ensure this field has no more than 150 characters.']


def test_very_long_password():
    request_body = {"username": fake.user_name(), "password": "A" * 129}
    response = requests.post(API_URL + "/users/register/", json=request_body)

    print("\nStatus code: ", response.status_code)
    print("Body: ", response.text)

    assert response.status_code == 400

    body = response.json()
    validate(body, schema=very_long_password_schema)

    assert body["password"] == ['Ensure this field has no more than 128 characters.']


def test_very_long_both_fields():
    request_body = {"username": "B" * 151, "password": "A" * 129}
    response = requests.post(API_URL + "/users/register/", json=request_body)

    print("\nStatus code: ", response.status_code)
    print("Body: ", response.text)

    assert response.status_code == 400

    body = response.json()
    validate(body, schema=very_long_both_fields_schema)

    assert body["username"] == ['Ensure this field has no more than 150 characters.']
    assert body["password"] == ['Ensure this field has no more than 128 characters.']


@pytest.mark.parametrize("username,password,status_code,schema,body_key", [
    ("38U54BUBq3Vfr.z3Rp7ULxmYoD****", "string", 400, invalid_username_schema, "username"),
    ("kjh lasdhk", "string", 400, invalid_username_schema, "username"),
])
def test_invalid_username(username, password, status_code, schema, body_key):
    request_body = {"username": username, "password": password}
    response = requests.post(API_URL + "/users/register/", json=request_body)

    print("\nStatus code: ", response.status_code)
    print("Body: ", response.text)

    assert response.status_code == status_code

    body = response.json()
    validate(body, schema=schema)

    assert body[body_key] == ['Enter a valid username. This value may contain only letters, numbers, and @/./+/-/_ characters.']

@pytest.mark.parametrize("username,password,status_code,schema,body_key", [
    ("A", fake.password(), 400, very_short_username_schema, "username"),
    (fake.user_name(), "1", 400, very_short_password_schema, "password"),
    ("A", "1", 400, very_short_both_fields_schema, ["username", "password"]),
])
@pytest.mark.xfail(reason="Api allows register with 1 character credentials")
def test_min_length_validation_register(username, password, status_code, schema, body_key):
    request_body = {"username": username, "password": password}
    response = requests.post(API_URL + "/users/register/", json=request_body)

    print("\nStatus code: ", response.status_code)
    print("Body: ", response.text)

    assert response.status_code == status_code

    body = response.json()
    validate(body, schema=schema)
    for key in body_key:
        assert body[key] == ["This field should be at least 3 characters"]

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

    assert body[body_key] == ['This field is required.'] 

@pytest.mark.parametrize("request_body,status_code,headers", [
    ({"username": fake.user_name(), "password": fake.password()}, 415, {"content-type": "image/png"}),
    ({"username": fake.user_name(), "password": fake.password()}, 415, {"content-type": "application/xml"}),
(   {"username": fake.user_name(), "password": fake.password()}, 415, {"content-type": "text/html"}),
])
def test_wrong_content_type_auth(request_body, status_code, headers):
    response = requests.post(API_URL + "/auth/token/", headers=headers ,json=request_body)

    print("\nStatus code: ", response.status_code)
    print("Body: ", response.text)

    assert response.status_code == status_code

    body = response.json()
    validate(body, schema=unsupported_content_type_registred_schema)

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

