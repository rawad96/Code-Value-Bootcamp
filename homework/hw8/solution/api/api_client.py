import requests

API_URL = "http://localhost:8000"


def get(path: str):
    response = requests.get(f"{API_URL}{path}")
    response.raise_for_status()
    return response.json()


def post(path: str, data: dict):
    response = requests.post(f"{API_URL}{path}", json=data)
    response.raise_for_status()
    return response.json()


def delete(path: str):
    response = requests.delete(f"{API_URL}{path}")
    response.raise_for_status()
    return response.json()


def put(path: str, data: dict):
    response = requests.put(f"{API_URL}{path}", json=data)
    response.raise_for_status()
    return response.json()
