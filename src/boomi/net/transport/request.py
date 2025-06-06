
from typing import Any, Set
from .utils import extract_original_data


class Request:
    """
    A simple HTTP request builder class using the requests library.

    Example Usage:
    ```python
    # Create a Request object
    request = Request()

    # Set request parameters
    request.set_url('https://yourendpoint.com/') \
           .set_method('GET') \
           .set_headers({'Content-Type': 'application/json'}) \
           .set_body(None)  # For GET requests, the body should be None

    # Send the HTTP request
    response = request.send()
    ```

    :ivar str url: The URL of the API endpoint.
    :ivar str method: The HTTP method for the request.
    :ivar dict headers: Dictionary of headers to include in the request.
    :ivar Any body: Request body.
    :ivar Set[str] scopes: List of scopes to include in the request.
    :ivar dict errors: Dictionary of HTTP status codes to error models.
    """

    def __init__(self):
        self.url = None
        self.method = None
        self.headers = None
        self.body = None
        self.scopes = None
        self.errors = None

    def set_url(self, url: str) -> "Request":
        """
        Set the URL of the API endpoint.

        :param str url: The URL of the API endpoint.
        :return: The updated Request object.
        :rtype: Request
        """
        self.url = url
        return self

    def set_headers(self, headers: dict) -> "Request":
        """
        Set the headers for the HTTP request.

        :param dict headers: Dictionary of headers to include in the request.
        :return: The updated Request object.
        :rtype: Request
        """
        self.headers = headers
        return self

    def set_method(self, method: str) -> "Request":
        """
        Set the HTTP method for the request.

        :param str method: The HTTP method (e.g., 'GET', 'POST', 'PUT', 'DELETE', etc.).
        :return: The updated Request object.
        :rtype: Request
        """
        self.method = method
        return self

    def set_body(self, body: Any, content_type: str = "application/json") -> "Request":
        """
        Set the request body (e.g., JSON payload).

        :param Any body: Request body.
        :param str content_type: The content type of the request body. Default is "application/json".
        :return: The updated Request object.
        :rtype: Request
        """
        self.body = extract_original_data(body)
        self.headers["Content-Type"] = content_type
        return self

    def set_scopes(self, scopes: Set[str]) -> "Request":
        """
        Set the scopes for the request.

        :param list scopes: List of scopes to include in the request.
        :return: The updated Request object.
        :rtype: Request
        """
        self.scopes = scopes
        return self

    def set_errors(self, errors: dict) -> "Request":
        """
        Set the errors for the request.

        :param dict errors: Dictionary of HTTP status codes to error models.
        :return: The updated Request object.
        :rtype: Request
        """
        self.errors = errors
        return self

    def __str__(self) -> str:
        """
        Return a string representation of the Request object.

        :return: A string representation of the Request object.
        :rtype: str
        """
        return f"Request(url={self.url}, method={self.method}, headers={self.headers}, body={self.body})"
