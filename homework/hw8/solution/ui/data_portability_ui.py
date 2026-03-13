import requests

API_URL = "http://localhost:8000"

CHUNK_SIZE = 8192


def export_data() -> None:
    """Exports all data to zip file."""
    try:
        response = requests.get(f"{API_URL}/data/export", stream=True)
        response.raise_for_status()
        filename = "backup.zip"
        with open(filename, "wb") as file:
            for chunk in response.iter_content(CHUNK_SIZE=CHUNK_SIZE):
                file.write(chunk)
        print(f"[SUCCESS] Data exported to {filename}")
    except requests.RequestException as error:
        print(f"[ERROR] Failed to export data: {error}")


def import_data() -> None:
    """Imports data from zip file."""
    path = input("Enter path to ZIP file: ").strip()
    try:
        with open(path, "rb") as file:
            files = {"file": (path, file, "application/zip")}
            response = requests.post(f"{API_URL}/data/import", files=files)
            response.raise_for_status()
        print("[SUCCESS] Data imported successfully!")
    except FileNotFoundError:
        print(f"[ERROR] File not found: {path}")
    except requests.RequestException as error:
        print(f"[ERROR] Failed to import data: {error}")
