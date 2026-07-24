import requests
from jsonschema import validate

from schemas.status_response_schema import status_response

def test_ready_is_true():
    response = requests.get("https://selenoid.qa.guru/ui/wd/hub/status")

    print("\nStatus code: ", response.status_code)
    print("Headers: ", response.headers)
    print("Body: ", response.text)

    assert response.status_code == 200
