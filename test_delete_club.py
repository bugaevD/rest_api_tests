import pytest
import requests
import random
from jsonschema import validate

from schemas.delete_club_schema import delete_other_user_club_schema, \
    delete_already_deleted_club_schema, delete_invalid_id_schema, delete_nonexistent_club_schema

API_URL = "https://book-club.qa.guru/api/v1"


def test_success_delete_club(auth):
    book_title = f"Crime and Punishment {random.randint(1000, 9999)}"
    book_authors = f"Fyodor Mikhailovich Dostoevsky {random.randint(1, 10)}"
    club_body = {
        "bookTitle": book_title,
        "bookAuthors": book_authors,
        "publicationYear": 1866,
        "description": "Some description",
        "telegramChatLink": "https://t.me/qa-guru"
    }
    club_response = requests.post(API_URL + "/clubs/", headers=auth, json=club_body)
    club_id = str(club_response.json()["id"])

    delete_response = requests.delete(API_URL + "/clubs/" + club_id, headers=auth)

    assert delete_response.status_code == 204


def test_delete_club_without_auth(auth):
    book_title = f"Crime and Punishment {random.randint(1000, 9999)}"
    book_authors = f"Fyodor Mikhailovich Dostoevsky {random.randint(1, 10)}"
    club_body = {
        "bookTitle": book_title,
        "bookAuthors": book_authors,
        "publicationYear": 1866,
        "description": "Some description",
        "telegramChatLink": "https://t.me/qa-guru"
    }
    club_response = requests.post(API_URL + "/clubs/", headers=auth, json=club_body)
    club_id = str(club_response.json()["id"])

    delete_response = requests.delete(API_URL + "/clubs/" + club_id)

    print("\nStatus code: ", delete_response.status_code)
    print("Headers: ", delete_response.headers)
    print("Body: ", delete_response.text)

    assert delete_response.status_code == 401

    club_response_body = delete_response.json()
    validate(club_response_body, schema=delete_other_user_club_schema)

    assert club_response_body["detail"] == "Authentication credentials were not provided."


def test_delete_other_user_club(auth):
    delete_response = requests.delete(API_URL + "/clubs/" + "1", headers=auth)

    print("\nStatus code: ", delete_response.status_code)
    print("Headers: ", delete_response.headers)
    print("Body: ", delete_response.text)

    assert delete_response.status_code == 403

    club_response_body = delete_response.json()
    validate(club_response_body, schema=delete_other_user_club_schema)

    assert club_response_body["detail"] == "You do not have permission to perform this action."


def test_delete_nonexistent_club(auth):
    delete_response = requests.delete(API_URL + "/clubs/" + "9999", headers=auth)

    print("\nStatus code: ", delete_response.status_code)
    print("Headers: ", delete_response.headers)
    print("Body: ", delete_response.text)

    assert delete_response.status_code == 404

    club_response_body = delete_response.json()
    validate(club_response_body, schema=delete_nonexistent_club_schema)

    assert club_response_body["detail"] == "No Club matches the given query."


def test_delete_already_deleted_club(auth):
    book_title = f"Crime and Punishment {random.randint(1000, 9999)}"
    book_authors = f"Fyodor Mikhailovich Dostoevsky {random.randint(1, 10)}"
    club_body = {
        "bookTitle": book_title,
        "bookAuthors": book_authors,
        "publicationYear": 1866,
        "description": "Some description",
        "telegramChatLink": "https://t.me/qa-guru"
    }
    club_response = requests.post(API_URL + "/clubs/", headers=auth, json=club_body)
    club_id = str(club_response.json()["id"])

    requests.delete(API_URL + "/clubs/" + club_id, headers=auth)
    delete_response = requests.delete(API_URL + "/clubs/" + club_id, headers=auth)

    print("\nStatus code: ", delete_response.status_code)
    print("Headers: ", delete_response.headers)
    print("Body: ", delete_response.text)

    assert delete_response.status_code == 404

    club_response_body = delete_response.json()
    validate(club_response_body, schema=delete_already_deleted_club_schema)

    assert club_response_body["detail"] == "No Club matches the given query."


@pytest.mark.parametrize("invalid_id,error_message", [
    ("abc", "Not found."),
    ("12.5", "Not found."),
    (" ", "Not found."),
    ("0", "No Club matches the given query."),
    ("-1", "No Club matches the given query."),
])
def test_delete_club_invalid_id(auth, invalid_id, error_message):
    delete_response = requests.delete(API_URL + "/clubs/" + invalid_id, headers=auth)

    print("\nStatus code: ", delete_response.status_code)
    print("Headers: ", delete_response.headers)
    print("Body: ", delete_response.text)

    assert delete_response.status_code == 404

    club_response_body = delete_response.json()
    validate(club_response_body, schema=delete_invalid_id_schema)

    assert club_response_body["detail"] == error_message
