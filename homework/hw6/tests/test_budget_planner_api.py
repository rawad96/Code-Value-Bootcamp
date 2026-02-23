import requests
import responses

BASE_URL = "http://localhost:8000"


@responses.activate
def test_add_income_calls_api_and_returns_success():
    responses.add(
        responses.POST,
        f"{BASE_URL}/add_income",
        json={"message": "Income added successfully."},
        status=200,
    )
    response = requests.post(
        f"{BASE_URL}/add_income",
        json={"description": "Salary", "amount": 5000.0},
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Income added successfully."}
