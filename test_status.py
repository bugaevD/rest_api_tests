import requests
from jsonschema import validate

from schemas.status_response_schema import status_response


def test_total_amount():
    response = requests.get("https://selenoid.qa.guru/ui/status")

    print("\nStatus code: ", response.status_code)
    print("Headers: ", response.headers)
    print("Body: ", response.text)

    assert response.status_code == 200

    body = response.json()

    assert body["state"]["total"] == 25

def test_total_amount_with_schema():
    response = requests.get("https://selenoid.qa.guru/ui/status")

    print("\nStatus code: ", response.status_code)
    print("Headers: ", response.headers)
    print("Body: ", response.text)

    assert response.status_code == 200

    body = response.json()
    validate(body, schema=status_response)

    assert body["state"]["total"] == 25