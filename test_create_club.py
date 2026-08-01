import pytest
import requests
import random
from jsonschema import validate

from schemas import club_schema
from schemas.create_club_schema import success_create_club_schema, duplicate_create_club_schema, \
    no_auth_create_club_schema, invalid_token_create_club_schema, empty_book_title_schema, empty_book_author_schema, \
    empty_book_description_schema, empty_book_telegram_schema, missing_book_title_schema, missing_book_author_schema, \
    missing_book_description_schema, missing_book_telegram_schema, missing_book_publication_year_schema, \
    invalid_data_type_book_publication_year_schema, empty_book_publication_year_schema, invalid_json_schema, \
    unsupported_media_type_schema, very_long_book_title_schema, very_long_book_author_schema, \
    invalid_telegram_link_schema

API_URL = "https://book-club.qa.guru/api/v1"
USERNAME = "bugaev"
PASSWORD = "qwerty"
USER_ID = 306


def test_success_create_club(auth):
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

    print("\nStatus code: ", club_response.status_code)
    print("Headers: ", club_response.headers)
    print("Body: ", club_response.text)

    assert club_response.status_code == 201

    club_response_body = club_response.json()
    validate(club_response_body, schema=success_create_club_schema)

    assert club_response_body["bookTitle"] == book_title
    assert club_response_body["bookAuthors"] == book_authors
    assert club_response_body["publicationYear"] == 1866
    assert club_response_body["description"] == "Some description"
    assert club_response_body["telegramChatLink"] == "https://t.me/qa-guru"
    assert club_response_body["owner"] == USER_ID
    assert USER_ID in club_response_body["members"]
    assert club_response_body["modified"] is None


def test_create_duplicate_club(auth):
    club_body = {
        "bookTitle": "Of Mice and Men",
        "bookAuthors": "Mrs. Oma White",
        "publicationYear": 1806,
        "description": "Chuck Norris doesn't use pointers, he just points, and memory obeys.",
        "telegramChatLink": "https://t.me/Ulysses"
    }
    club_response = requests.post(API_URL + "/clubs/", headers=auth, json=club_body)

    print("\nStatus code: ", club_response.status_code)
    print("Headers: ", club_response.headers)
    print("Body: ", club_response.text)

    assert club_response.status_code == 400

    club_response_body = club_response.json()
    validate(club_response_body, schema=duplicate_create_club_schema)

    assert ["Book Club with this Book Title already exists."] == club_response_body["bookTitle"]


def test_create_club_without_access_token():
    book_title = f"Crime and Punishment {random.randint(1000, 9999)}"
    book_authors = f"Fyodor Mikhailovich Dostoevsky {random.randint(1, 10)}"
    club_body = {
        "bookTitle": book_title,
        "bookAuthors": book_authors,
        "publicationYear": 1866,
        "description": "Some description",
        "telegramChatLink": "https://t.me/qa-guru"
    }
    club_response = requests.post(API_URL + "/clubs/", json=club_body)

    print("\nStatus code: ", club_response.status_code)
    print("Headers: ", club_response.headers)
    print("Body: ", club_response.text)

    assert club_response.status_code == 401

    club_response_body = club_response.json()
    validate(club_response_body, schema=no_auth_create_club_schema)

    assert club_response_body["detail"] == "Authentication credentials were not provided."


def test_create_club_with_invalid_access_token():
    invalid_access_token = "Bearer invalid.token.12345"
    headers = {"Authorization": invalid_access_token}
    book_title = f"Crime and Punishment {random.randint(1000, 9999)}"
    book_authors = f"Fyodor Mikhailovich Dostoevsky {random.randint(1, 10)}"
    club_body = {
        "bookTitle": book_title,
        "bookAuthors": book_authors,
        "publicationYear": 1866,
        "description": "Some description",
        "telegramChatLink": "https://t.me/qa-guru"
    }
    club_response = requests.post(API_URL + "/clubs/", headers=headers, json=club_body)

    print("\nStatus code: ", club_response.status_code)
    print("Headers: ", club_response.headers)
    print("Body: ", club_response.text)

    assert club_response.status_code == 401

    club_response_body = club_response.json()
    validate(club_response_body, schema=invalid_token_create_club_schema)

    assert club_response_body["detail"] == "Given token not valid for any token type"
    assert club_response_body["code"] == "token_not_valid"
    assert club_response_body["messages"][0]["message"] == "Token is invalid"


@pytest.mark.parametrize("key,schema,error_message", [
    ("bookTitle", empty_book_title_schema, ["This field may not be blank."]),
    ("bookAuthors", empty_book_author_schema, ["This field may not be blank."]),
    ("publicationYear", empty_book_publication_year_schema, ["A valid integer is required."]),
    ("description", empty_book_description_schema, ["This field may not be blank."]),
    ("telegramChatLink", empty_book_telegram_schema, ["This field may not be blank."]),
])
def test_create_club_empty_required_field(key, schema, error_message, auth):
    book_title = f"Crime and Punishment {random.randint(1000, 9999)}"
    book_authors = f"Fyodor Mikhailovich Dostoevsky {random.randint(1, 10)}"
    club_body = {
        "bookTitle": book_title,
        "bookAuthors": book_authors,
        "publicationYear": 1866,
        "description": "Chuck Norris doesn't use pointers, he just points, and memory obeys.",
        "telegramChatLink": "https://t.me/Ulysses"
    }
    club_body[key] = ""
    club_response = requests.post(API_URL + "/clubs/", headers=auth, json=club_body)

    print("\nStatus code: ", club_response.status_code)
    print("Headers: ", club_response.headers)
    print("Body: ", club_response.text)

    assert club_response.status_code == 400

    club_response_body = club_response.json()
    validate(club_response_body, schema=schema)

    assert club_response_body[key] == error_message


@pytest.mark.parametrize("key,schema", [
    ("bookTitle", missing_book_title_schema),
    ("bookAuthors", missing_book_author_schema),
    ("publicationYear", missing_book_publication_year_schema),
    ("description", missing_book_description_schema),
    ("telegramChatLink", missing_book_telegram_schema),
])
def test_create_club_missing_required_field(key, schema, auth):
    book_title = f"Crime and Punishment {random.randint(1000, 9999)}"
    book_authors = f"Fyodor Mikhailovich Dostoevsky {random.randint(1, 10)}"
    club_body = {
        "bookTitle": book_title,
        "bookAuthors": book_authors,
        "publicationYear": 1806,
        "description": "Chuck Norris doesn't use pointers, he just points, and memory obeys.",
        "telegramChatLink": "https://t.me/Ulysses"
    }
    del club_body[key]
    club_response = requests.post(API_URL + "/clubs/", headers=auth, json=club_body)

    print("\nStatus code: ", club_response.status_code)
    print("Headers: ", club_response.headers)
    print("Body: ", club_response.text)

    assert club_response.status_code == 400

    club_response_body = club_response.json()
    validate(club_response_body, schema=schema)

    assert club_response_body[key] == ["This field is required."]


@pytest.mark.xfail
@pytest.mark.parametrize("publication_year,schema,error_message", [
    ("string", invalid_data_type_book_publication_year_schema, ["A valid integer is required."]),
    ("12.5", invalid_data_type_book_publication_year_schema, ["A valid integer is required."]),
    (None, invalid_data_type_book_publication_year_schema, ["This field may not be null."]),
])
def test_create_club_publication_year_validation(publication_year, schema, error_message, auth):
    book_title = f"Crime and Punishment {random.randint(1000, 9999)}"
    book_authors = f"Fyodor Mikhailovich Dostoevsky {random.randint(1, 10)}"
    club_body = {
        "bookTitle": book_title,
        "bookAuthors": book_authors,
        "publicationYear": publication_year,
        "description": "Chuck Norris doesn't use pointers, he just points, and memory obeys.",
        "telegramChatLink": "https://t.me/Ulysses"
    }
    club_response = requests.post(API_URL + "/clubs/", headers=auth, json=club_body)

    print("\nStatus code: ", club_response.status_code)
    print("Headers: ", club_response.headers)
    print("Body: ", club_response.text)

    assert club_response.status_code == 400

    club_response_body = club_response.json()
    validate(club_response_body, schema=schema)

    assert club_response_body["publicationYear"] == error_message
@pytest.mark.parametrize("telegram_link", [
    "random_url",
    "http://",
    "https://",
    "t.me/qa-guru"
])
def test_create_club_telegram_validation(telegram_link, auth):
    book_title = f"Crime and Punishment {random.randint(1000, 9999)}"
    book_authors = f"Fyodor Mikhailovich Dostoevsky {random.randint(1, 10)}"
    club_body = {
        "bookTitle": book_title,
        "bookAuthors": book_authors,
        "publicationYear": 1866,
        "description": "Chuck Norris doesn't use pointers, he just points, and memory obeys.",
        "telegramChatLink": telegram_link
    }
    club_response = requests.post(API_URL + "/clubs/", headers=auth, json=club_body)

    print("\nStatus code: ", club_response.status_code)
    print("Headers: ", club_response.headers)
    print("Body: ", club_response.text)

    assert club_response.status_code == 400

    club_response_body = club_response.json()
    validate(club_response_body, schema=invalid_telegram_link_schema)

    assert club_response_body["telegramChatLink"] == ["Enter a valid URL."]


def test_create_club_invalid_json(auth):
    headers = auth
    headers["Content-Type"] = "application/json"
    invalid_json = '{"bookTitle": "Test", "bookAuthors": "Author", publicationYear: 2024}'
    club_response = requests.post(API_URL + "/clubs/", headers=headers, data=invalid_json)

    print("\nStatus code: ", club_response.status_code)
    print("Headers: ", club_response.headers)
    print("Body: ", club_response.text)

    assert club_response.status_code == 400

    club_response_body = club_response.json()
    validate(club_response_body, schema=invalid_json_schema)

    assert "JSON parse error - unexpected character:" in club_response_body["detail"]


@pytest.mark.parametrize("content_type", [
    "image/png",
    "text/html",
    "application/xml"
])
def test_create_club_wrong_content_type(content_type, auth):
    headers = auth
    headers["Content-Type"] = content_type
    book_title = f"Crime and Punishment {random.randint(1000, 9999)}"
    book_authors = f"Fyodor Mikhailovich Dostoevsky {random.randint(1, 10)}"
    club_body = {
        "bookTitle": book_title,
        "bookAuthors": book_authors,
        "publicationYear": 1866,
        "description": "Chuck Norris doesn't use pointers, he just points, and memory obeys.",
        "telegramChatLink": "https://t.me/Ulysses"
    }
    club_response = requests.post(API_URL + "/clubs/", headers=headers, json=club_body)

    print("\nStatus code: ", club_response.status_code)
    print("Headers: ", club_response.headers)
    print("Body: ", club_response.text)

    assert club_response.status_code == 415

    club_response_body = club_response.json()
    validate(club_response_body, schema=unsupported_media_type_schema)

    assert "Unsupported media type" in club_response_body["detail"]


@pytest.mark.parametrize("key,length,schema", [
    ("bookTitle", 256, very_long_book_title_schema),
    ("bookAuthors", 256, very_long_book_author_schema),
])
def test_create_club_too_long_fields(key, length, schema, auth):
    book_title = f"Crime and Punishment {random.randint(1000, 9999)}"
    book_authors = f"Fyodor Mikhailovich Dostoevsky {random.randint(1, 10)}"
    club_body = {
        "bookTitle": book_title,
        "bookAuthors": book_authors,
        "publicationYear": 1866,
        "description": "Chuck Norris doesn't use pointers, he just points, and memory obeys.",
        "telegramChatLink": "https://t.me/Ulysses"
    }
    club_body[key] = "A" * length
    club_response = requests.post(API_URL + "/clubs/", headers=auth, json=club_body)

    print("\nStatus code: ", club_response.status_code)
    print("Headers: ", club_response.headers)
    print("Body: ", club_response.text)

    assert club_response.status_code == 400

    club_response_body = club_response.json()
    validate(club_response_body, schema=schema)

    assert club_response_body[key] == ["Ensure this field has no more than 255 characters."]
