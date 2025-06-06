
from typing import Any, List
from urllib.parse import quote

from .request import Request
from .utils import extract_original_data
from ...models.utils.sentinel import was_value_set
from ...net.headers.base_header import BaseHeader
from ...net.transport.api_error import ApiError


class Serializer:
    """
    A class for handling serialization of URL components such as headers, cookies, path parameters, and query parameters.

    :ivar str url: The base URL to be serialized.
    :ivar dict[str, str] headers: A dictionary containing headers for the request.
    :ivar list[str] cookies: A list containing cookie strings for the request.
    :ivar dict[str, str] path: A dictionary containing path parameters for the request.
    :ivar list[str] query: A list containing query parameters for the request.
    :ivar dict[int, ApiError] errors: A dictionary of HTTP status codes to error models.
    """

    def __init__(self, url: str, default_headers: List[BaseHeader] = []):
        """
        Initializes a Serializer instance with the base URL.

        :param str url: The base URL to be serialized.
        :param list[BaseHeader] default_headers: A list of default headers to be added to the request. Defaults to an empty list.
        """
        self.url: str = url
        self.headers: dict[str, str] = {}
        self.cookies: list[str] = []
        self.path: dict[str, str] = {}
        self.query: list[str] = []
        self.errors: dict[int, ApiError] = {}

        for header in default_headers:
            for key, value in header.get_headers().items():
                self.add_header(key, value)

    def add_header(
        self, key: str, data: Any, explode: bool = False, nullable: bool = False
    ) -> "Serializer":
        """
        Adds a header to the request.

        :param str key: The header key.
        :param Any data: The data to be serialized as the header value.
        :param bool explode: Flag indicating whether to explode the data.
        :return: The Serializer instance for method chaining.
        :rtype: Serializer
        """
        if not nullable and data is None:
            return self

        if not was_value_set(data):
            return self

        data = extract_original_data(data)

        self.headers[key] = self._serialize_value(
            data, explode=explode, quote_str_values=False
        )
        return self

    def add_cookie(
        self, key: str, data: Any, explode: bool = False, nullable: bool = False
    ) -> "Serializer":
        """
        Adds a cookie to the request.

        :param str key: The cookie key.
        :param Any data: The data to be serialized as the cookie value.
        :param bool explode: Flag indicating whether to explode the data.
        :return: The Serializer instance for method chaining.
        :rtype: Serializer
        """
        if not nullable and data is None:
            return self

        if not was_value_set(data):
            return self

        data = extract_original_data(data)

        self.cookies.append(
            f"{key}={self._serialize_value(data, explode=explode, quote_str_values=False)}"
        )
        return self

    def add_path(
        self,
        key: str,
        data: Any,
        explode: bool = False,
        style: str = "simple",
        nullable: bool = False,
    ) -> "Serializer":
        """
        Adds a path parameter to the request.

        :param str key: The path parameter key.
        :param Any data: The data to be serialized as the path parameter value.
        :param bool explode: Flag indicating whether to explode the data.
        :param str style: The style of serialization for the path parameter.
        :return: The Serializer instance for method chaining.
        :rtype: Serializer
        """
        if not nullable and data is None:
            return self

        if not was_value_set(data):
            return self

        data = extract_original_data(data)

        if style == "simple":
            self.path[key] = self._serialize_value(data=data, explode=explode)
        elif style == "label":
            separator = "." if explode else ","
            self.path[key] = "." + self._serialize_value(
                data=data, explode=explode, separator=separator
            )
        elif style == "matrix":
            separator = ","

            if isinstance(data, list) and explode:
                separator = f";{key}="
            elif explode:
                separator = ";"

            prefix = ";" if isinstance(data, dict) and explode else f";{key}="
            self.path[key] = prefix + self._serialize_value(
                data, explode=explode, separator=separator
            )
        else:
            raise ValueError(f"Unsupported path style: {style}")

        return self

    def add_query(
        self,
        key: str,
        data: Any,
        explode: bool = True,
        style: str = "form",
        nullable: bool = False,
    ) -> "Serializer":
        """
        Adds a query parameter to the request.

        :param str key: The query parameter key.
        :param Any data: The data to be serialized as the query parameter value.
        :param bool explode: Flag indicating whether to explode the data.
        :param str style: The style of serialization for the query parameter.
        :return: The Serializer instance for method chaining.
        :rtype: Serializer
        """
        if not nullable and data is None:
            return self

        if not was_value_set(data):
            return self

        data = extract_original_data(data)

        if style == "form":
            separator = (
                f"&{key}="
                if explode and isinstance(data, list)
                else ("&" if explode else ",")
            )
            prefix = "" if (explode and isinstance(data, dict)) else f"{key}="
            query_param = f"{prefix}{self._serialize_value(data=data, explode=explode, separator=separator)}"
        elif style == "spaceDelimited":
            separator = f"&{key}=" if explode else f"%20"
            query_param = f"{key}={self._serialize_value(data=data, explode=explode, separator=separator)}"
        elif style == "pipeDelimited":
            separator = f"&{key}=" if explode else "|"
            query_param = f"{key}={self._serialize_value(data=data, explode=explode, separator=separator)}"
        elif style == "deepObject":
            query_param = "".join(
                f"{key}[{k}]={quote(self._serialize_value(v))}&"
                for k, v in data.items()
            ).rstrip("&")

        self.query.append(query_param)
        return self

    def add_error(self, status: int, error: ApiError) -> "Serializer":
        """
        Adds an error to the request.

        :param int status: The HTTP status code associated with the error.
        :param ApiError error: The ApiError class representing the error.
        :return: The Serializer instance for method chaining.
        :rtype: Serializer
        """
        if not was_value_set(error):
            return self

        self.errors[status] = error
        return self

    def serialize(self) -> Request:
        """
        Serializes the components and returns a Request object.

        :return: The Request object containing the serialized components.
        :rtype: Request
        """
        final_url = self._define_url()

        if len(self.cookies) > 0:
            self.headers["Cookie"] = ";".join(self.cookies)

        return (
            Request()
            .set_url(final_url)
            .set_headers(self.headers)
            .set_errors(self.errors)
        )

    def _define_url(self) -> str:
        """
        Constructs the final URL by replacing path parameters and appending query parameters.

        :return: The final URL.
        :rtype: str
        """
        final_url = self.url

        for key, value in self.path.items():
            final_url = final_url.replace(f"{{{key}}}", value)

        if len(self.query) > 0:
            final_url += "?" + "&".join(self.query)

        return final_url

    def _serialize_value(
        self,
        data: Any,
        separator: str = ",",
        explode: bool = False,
        quote_str_values: bool = True,
    ) -> str:
        """
        Serializes a value based on the specified separator and explode flag.

        :param Any data: The data to be serialized.
        :param str separator: The separator used for serialization.
        :param bool explode: Flag indicating whether to explode the data.
        :return: The serialized value.
        :rtype: str
        """
        if data is None:
            return "null"

        if isinstance(data, list):
            return separator.join(
                self._serialize_value(item, separator, explode) for item in data
            )

        if isinstance(data, dict):
            if explode:
                return separator.join(
                    [
                        f"{k}={self._serialize_value(v, separator, explode)}"
                        for k, v in data.items()
                    ]
                )
            else:
                return separator.join(
                    [
                        self._serialize_value(item, separator, explode)
                        for sublist in data.items()
                        for item in sublist
                    ]
                )

        if isinstance(data, str) and quote_str_values:
            return quote(data)
        if isinstance(data, bool):
            return str(data).lower()
        if isinstance(data, (int, float)):
            return str(data)

        return data
