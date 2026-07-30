import requests
from jsonschema import validate

from schemas.club_schema import club_response
from schemas.get_clubs_response_schema import status_response
from schemas.invalid_search_schema import invalid_search
from schemas.search_schema import search_title_schema


def test_count_of_clubs_with_schema():
    response = requests.get("https://book-club.qa.guru/api/v1/clubs/")

    print("\nStatus code: ", response.status_code)
    print("Body: ", response.text)

    assert response.status_code == 200

    body = response.json()
    validate(body, schema=status_response)

    assert body["count"] == 92


def test_club_1_book_title():
    response = requests.get("https://book-club.qa.guru/api/v1/clubs/1")
    print("\nStatus code: ", response.status_code)
    print("Body: ", response.text)

    assert response.status_code == 200

    body = response.json()
    validate(body, schema=club_response)

    assert body["bookTitle"] == "Of Mice and Men"


def test_number_of_clubs_per_page_with_page_size_10():
    params = {"page": 1, "page_size": 10}
    response = requests.get("https://book-club.qa.guru/api/v1/clubs/", params)

    print("\nStatus code: ", response.status_code)
    print("Body: ", response.text)

    assert response.status_code == 200

    body = response.json()
    validate(body, schema=status_response)

    total_of_clubs_per_page = 0

    for club in body["results"]:
        total_of_clubs_per_page += 1
    print("Total number of clubs: ", total_of_clubs_per_page)

    assert total_of_clubs_per_page == 10


def test_search_by_book_title():
    params = {"search": "The Other Side of Silence"}
    response = requests.get("https://book-club.qa.guru/api/v1/clubs/", params)

    print("\nStatus code: ", response.status_code)
    print("Body: ", response.text)

    assert response.status_code == 200

    body = response.json()
    validate(body, schema=search_title_schema)

    assert body["results"][0]["bookTitle"] == "The Other Side of Silence"


def test_non_existent_book_title():
    params = {"search": "Non existent book"}
    response = requests.get("https://book-club.qa.guru/api/v1/clubs/", params)

    print("\nStatus code: ", response.status_code)
    print("Body: ", response.text)

    assert response.status_code == 200

    body = response.json()
    validate(body, schema=invalid_search)

    assert body["count"] == 0
