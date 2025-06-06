
import requests

from requests.exceptions import Timeout
from typing import Generator, Optional, Tuple
from .base_handler import BaseHandler
from ...transport.request import Request
from ...transport.response import Response
from ...transport.api_error import ApiError


class HttpHandler(BaseHandler):
    """
    Handler for making HTTP requests.
    This handler sends the request to the specified URL and returns the response.

    :ivar int _timeout_in_seconds: The timeout for the HTTP request in seconds.
    """

    def __init__(self, timeout=60000):
        """
        Initialize a new instance of HttpHandler.
        """
        super().__init__()
        self._timeout_in_seconds = timeout / 1000

    def handle(
        self, request: Request
    ) -> Tuple[Optional[Response], Optional[Exception]]:
        """
        Send the request to the specified URL and return the response.

        :param Request request: The request to send.
        :return: The response and any error that occurred.
        :rtype: Tuple[Optional[Response], Optional[Exception]]
        """
        try:
            request_args = self._get_request_data(request)

            result = requests.request(
                request.method,
                request.url,
                headers=request.headers,
                timeout=self._timeout_in_seconds,
                **request_args,
            )
            response = Response(result)

            if response.status >= 400:
                if response.status in request.errors and isinstance(
                    response.body, dict
                ):
                    error_model_class = request.errors[response.status]
                    error = error_model_class(**response.body)
                    if "message" not in response.body:
                        error.message = (
                            f"{response.status} error in request to: {request.url}"
                        )
                    error.status = response.status
                    error.response = response

                    return None, error

                return None, ApiError(
                    message=f"{response.status} error in request to: {request.url}",
                    status=response.status,
                    response=response,
                )

            return response, None
        except Timeout:
            return None, ApiError("Request timed out", status=408)

    def stream(
        self, request: Request
    ) -> Generator[Tuple[Optional[Response], Optional[Exception]], None, None]:
        try:
            request_args = self._get_request_data(request)

            result = requests.request(
                request.method,
                request.url,
                headers=request.headers,
                timeout=self._timeout_in_seconds,
                stream=True,
                **request_args,
            )

            if result.status_code >= 400:
                response = Response(result)
                yield (
                    None,
                    ApiError(
                        message=f"{response.status} error in request to: {request.url}",
                        status=response.status,
                        response=response,
                    ),
                )

            else:
                for chunk in result.iter_content(chunk_size=8192):
                    for response in Response.from_chunk(result, chunk):
                        yield response, None

        except Timeout:
            yield None, ApiError("Request timed out", status=408)

    def _get_request_data(self, request: Request) -> dict:
        """
        Get the request arguments based on the request headers and data.

        :param Request request: The request object.
        :return: The request arguments.
        :rtype: dict
        """
        headers = request.headers or {}
        data = request.body or {}
        content_type = headers.get("Content-Type", "application/json")

        if request.method == "GET" and not data:
            return {}

        if content_type.startswith("application/") and "json" in content_type:
            return {"json": data}

        if "multipart/form-data" in content_type:
            headers.pop("Content-Type", None)
            files, form_data = {}, {}
            for key, value in data.items():
                if isinstance(value, bytes):
                    files[key] = (key, value, "application/octet-stream")
                else:
                    form_data[key] = value
            return {"files": files, "data": form_data}

        return {"data": data}
