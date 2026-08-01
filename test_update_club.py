import pytest
import requests
import random
from jsonschema import validate

from schemas.update_club_schema import success_put_update_club_schema, success_patch_update_club_schema, \
    update_club_without_auth_schema, update_non_existent_club_schema, \
    patch_update_empty_body_schema, update_other_member_club_schema, \
    put_update_missing_required_fields_schema

API_URL = "https://book-club.qa.guru/api/v1"


def test_success_update_club(auth):
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

    updated_book_title = f"Updated Book {random.randint(1000, 9999)}"
    updated_club_body = {
        "bookTitle": updated_book_title,
        "bookAuthors": "Updated Author",
        "publicationYear": 2024,
        "description": "Updated description",
        "telegramChatLink": "https://t.me/updated"
    }
    put_response = requests.put(API_URL + "/clubs/" + club_id + "/", headers=auth, json=updated_club_body)

    print("\nStatus code: ", put_response.status_code)
    print("Headers: ", put_response.headers)
    print("Body: ", put_response.text)

    body = put_response.json()
    validate(body, schema=success_put_update_club_schema)

    assert put_response.status_code == 200
    assert body["bookTitle"] == updated_club_body["bookTitle"]
    assert body["bookAuthors"] == updated_club_body["bookAuthors"]
    assert body["publicationYear"] == updated_club_body["publicationYear"]
    assert body["description"] == updated_club_body["description"]
    assert body["telegramChatLink"] == updated_club_body["telegramChatLink"]
    assert body["modified"] is not None


def test_success_update_club_patch(auth):
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

    updated_book_title = f"Updated Book {random.randint(1000, 9999)}"
    updated_club_body = {
        "bookTitle": updated_book_title,
    }

    put_response = requests.patch(API_URL + "/clubs/" + club_id + "/", headers=auth, json=updated_club_body)

    print("\nStatus code: ", put_response.status_code)
    print("Headers: ", put_response.headers)
    print("Body: ", put_response.text)

    body = put_response.json()
    validate(body, schema=success_patch_update_club_schema)

    assert put_response.status_code == 200
    assert body["bookTitle"] == updated_club_body["bookTitle"]
    assert body["bookAuthors"] == club_body["bookAuthors"]
    assert body["publicationYear"] == club_body["publicationYear"]
    assert body["description"] == club_body["description"]
    assert body["telegramChatLink"] == club_body["telegramChatLink"]
    assert body["modified"] is not None


def test_update_club_without_auth(auth):
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

    updated_book_title = f"Updated Book {random.randint(1000, 9999)}"
    updated_club_body = {
        "bookTitle": updated_book_title,
        "bookAuthors": "Updated Author",
        "publicationYear": 2024,
        "description": "Updated description",
        "telegramChatLink": "https://t.me/updated"
    }
    put_response = requests.put(API_URL + "/clubs/" + club_id + "/", json=updated_club_body)

    print("\nStatus code: ", put_response.status_code)
    print("Headers: ", put_response.headers)
    print("Body: ", put_response.text)

    body = put_response.json()
    validate(body, schema=update_club_without_auth_schema)

    assert put_response.status_code == 401
    assert body["detail"] == "Authentication credentials were not provided."


def test_update_nonexistent_club(auth):
    updated_book_title = f"Updated Book {random.randint(1000, 9999)}"
    updated_club_body = {
        "bookTitle": updated_book_title,
        "bookAuthors": "Updated Author",
        "publicationYear": 2024,
        "description": "Updated description",
        "telegramChatLink": "https://t.me/updated"
    }
    put_response = requests.put(API_URL + "/clubs/9999/", headers=auth, json=updated_club_body)

    print("\nStatus code: ", put_response.status_code)
    print("Headers: ", put_response.headers)
    print("Body: ", put_response.text)

    body = put_response.json()
    validate(body, schema=update_non_existent_club_schema)

    assert put_response.status_code == 404


def test_put_missing_required_fields(auth):
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

    updated_club_body = {}

    put_response = requests.put(API_URL + "/clubs/" + club_id + "/", headers=auth, json=updated_club_body)

    print("\nStatus code: ", put_response.status_code)
    print("Headers: ", put_response.headers)
    print("Body: ", put_response.text)

    body = put_response.json()
    validate(body, schema=put_update_missing_required_fields_schema)

    assert put_response.status_code == 400
    assert body["bookTitle"] == ["This field is required."]
    assert body["bookAuthors"] == ["This field is required."]
    assert body["publicationYear"] == ["This field is required."]
    assert body["description"] == ["This field is required."]
    assert body["telegramChatLink"] == ["This field is required."]


def test_update_other_members_club(auth):
    updated_book_title = f"Updated Book {random.randint(1000, 9999)}"
    updated_club_body = {
        "bookTitle": updated_book_title,
        "bookAuthors": "Updated Author",
        "publicationYear": 2024,
        "description": "Updated description",
        "telegramChatLink": "https://t.me/updated"
    }
    put_response = requests.put(API_URL + "/clubs/1/", headers=auth, json=updated_club_body)

    print("\nStatus code: ", put_response.status_code)
    print("Headers: ", put_response.headers)
    print("Body: ", put_response.text)

    body = put_response.json()
    validate(body, schema=update_other_member_club_schema)

    assert put_response.status_code == 403


def test_patch_with_empty_body(auth):
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

    updated_club_body = {}

    put_response = requests.patch(API_URL + "/clubs/" + club_id + "/", headers=auth, json=updated_club_body)

    print("\nStatus code: ", put_response.status_code)
    print("Headers: ", put_response.headers)
    print("Body: ", put_response.text)

    body = put_response.json()
    validate(body, schema=patch_update_empty_body_schema)

    assert put_response.status_code == 200
    assert body["bookTitle"] == club_body["bookTitle"]
    assert body["bookAuthors"] == club_body["bookAuthors"]
    assert body["publicationYear"] == club_body["publicationYear"]
    assert body["description"] == club_body["description"]
    assert body["telegramChatLink"] == club_body["telegramChatLink"]
    assert body["modified"] is not None