
from typing import Dict
from base64 import b64encode

from .base_header import BaseHeader


class BasicAuth(BaseHeader):
    """
    A class for handling Basic authentication in headers.

    :ivar str _username: The username for Basic authentication.
    :ivar str _password: The password for Basic authentication.
    """

    _username = ""
    _password = ""

    def __init__(self, username: str, password: str):
        """
        Initialize the BasicAuth instance.

        :param username: The username for Basic authentication.
        :type username: str
        :param password: The password for Basic authentication.
        :type password: str
        """
        self._username = username
        self._password = password

    def set_value(self, value: dict[str, str]) -> None:
        """
        Set the username and password for Basic authentication.

        :param value: A dictionary with keys 'username' and 'password'.
        :type value: dict[str, str]
        """
        self._username = value.get("username")
        self._password = value.get("password")

    def get_headers(self) -> Dict[str, str]:
        """
        Get the headers with the Authorization field set to the Basic authentication token.

        :return: A dictionary with the Authorization field set to the Basic authentication token.
        :rtype: Dict[str, str]
        """
        token = (
            "Basic " + b64encode(f"{self._username}:{self._password}".encode()).decode()
        )
        return {"Authorization": token}
