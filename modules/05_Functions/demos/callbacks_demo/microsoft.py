"""
Demo - This code simulates Microsoft API
"""

import uuid
from collections.abc import Callable


class InvalidTokenError(Exception):
    """Exception raised when the provided token is invalid."""
    pass


def _is_token_valid(token: str) -> bool:
    """Check if the current token is valid."""
    # Simulated token validation
    return token != "invalid_token"


def _get_data() -> dict:
    """Simulate fetching data."""
    return {"data": "example"}


def _generate_refresh_token() -> str:
    """Simulate the generation of a new refresh token."""
    return str(uuid.uuid4())


def request_data(api_url: str,
                 current_token: str,
                 on_token_refresh_callback: Callable[[str], None]) -> dict:
    """Request data from the API and handle token refresh."""
    if not _is_token_valid(current_token):
        raise InvalidTokenError("The current token is invalid.")

    data = _get_data()  # Get the requested data
    refreshed_token = _generate_refresh_token()
    on_token_refresh_callback(refreshed_token)  # Trigger the callback for token refresh
    return data
