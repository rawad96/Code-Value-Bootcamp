import requests
from typing import Any

API_URL = "http://localhost:8000"


def get(path: str) -> Any:
    response = requests.get(f"{API_URL}{path}")
    response.raise_for_status()
    return response.json()


def post(path: str, data: dict) -> dict[str, Any]:
    response = requests.post(f"{API_URL}{path}", json=data)
    response.raise_for_status()
    return response.json()


def delete(path: str) -> dict[str, Any]:
    response = requests.delete(f"{API_URL}{path}")
    response.raise_for_status()
    return response.json()


def put(path: str, data: dict) -> Any:
    response = requests.put(f"{API_URL}{path}", json=data)
    response.raise_for_status()
    return response.json()
