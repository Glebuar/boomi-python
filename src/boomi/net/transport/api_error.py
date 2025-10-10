
from ...models.utils.base_model import BaseModel
from .response import Response
from typing import Optional


class ApiError(BaseModel, Exception):
    """
    Class representing an API Error.

    :ivar Optional[int] status: The status code of the HTTP error.
    :ivar Optional[Response] response: The response associated with the error.
    :ivar Optional[str] error_detail: Parsed error message from response body (if available).
    """

    def __init__(
        self,
        message: Optional[str] = None,
        status: Optional[int] = None,
        response: Optional[Response] = None,
    ):
        """
        Initialize a new instance of API Error.

        :param Optional[str] message: The error message.
        :param Optional[int] status: The status code of the HTTP error.
        :param Optional[Response] response: The response associated with the error.
        """
        self.message = message
        self.status = status
        self.response = response
        self.error_detail = self._extract_error_detail()

    def _extract_error_detail(self) -> Optional[str]:
        """
        Extract detailed error message from XML response body if available.

        Returns:
            The error message from <error><message>...</message></error> or None
        """
        if not self.response or not hasattr(self.response, 'body'):
            return None

        body = self.response.body
        if not body or not isinstance(body, str):
            return None

        # Only try to parse XML error responses
        if not body.strip().startswith('<?xml') and not body.strip().startswith('<error'):
            return None

        try:
            from .utils import parse_xml_to_dict
            parsed = parse_xml_to_dict(body)

            # Check for standard Boomi error format: <error><message>...</message></error>
            if isinstance(parsed, dict) and 'error' in parsed:
                error_data = parsed['error']
                if isinstance(error_data, dict) and 'message' in error_data:
                    return error_data['message']

        except Exception:
            # If parsing fails, just return None
            pass

        return None
