from microsoft import request_data, InvalidTokenError
from my_logger import MyLogger


my_logger = MyLogger()


def _save_refreshed_token_to_disk(token: str) -> None:
    """Simulates saving the refreshed token to disk."""
    # Implementation to save the token
    my_logger.log(f"Token saved to disk: {token}")


def on_token_refresh(token: str) -> None:
    """Handles the token refresh callback."""
    _save_refreshed_token_to_disk(token)
    my_logger.log(f"Token was refreshed successfully: {token}")


def call_microsoft(current_token: str):
    try:
        data = request_data("https://api.microsoft.com/data",
                            current_token,
                            on_token_refresh)
        my_logger.log(str(data))
        return data
    except InvalidTokenError as e:
        my_logger.log(str(e))
