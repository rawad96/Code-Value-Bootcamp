import requests

API_URL = "http://localhost:8000"

CHUNK_SIZE = 8192


def export_data() -> None:
    """Exports all data to zip file."""
    try:
        response = requests.get(f"{API_URL}/data/export", stream=True)
    except requests.RequestException as error:
        print(f"[ERROR] Failed to export data: {error}")
        return
    else:
        response.raise_for_status()
    filename = "backup.zip"
    with open(filename, "wb") as file:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            file.write(chunk)

    print(f"[SUCCESS] Data exported to {filename}")


def import_data() -> None:
    """Imports data from zip file."""
    path = input("Enter path to ZIP file: ").strip()

    with open(path, "rb") as file:
        files = {"file": (path, file, "application/zip")}
        try:
            response = requests.post(f"{API_URL}/data/import", files=files)
        except requests.RequestException as error:
            print(f"[ERROR] Failed to import data: {error}")
            return

    response.raise_for_status()
    print("[SUCCESS] Data imported successfully!")
