"""
Demo - Keyword Arguments, Default Arguments
"""
from typing import Optional


def configure_server(ip: str, 
                     port: int,
                     timeout: Optional[int] = None,
                     encryption: Optional[bool] = False) -> None:
    print(f"Server IP: {ip}")
    print(f"Port: {port}")
    print(f"Timeout: {timeout} seconds")
    print(f"Encryption: {'enabled' if encryption else 'disabled'}")


# Example of calling with keyword arguments
configure_server(ip='192.168.1.1', port=8080)

