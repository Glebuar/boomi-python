
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({"status_code": "statusCode"})
class LogDownload(BaseModel):
    """LogDownload

    :param status_code: The status code as one of the following:   - 202 — status message: Beginning download.  - 504 — status message: Runtime is unavailable., defaults to None
    :type status_code: str, optional
    :param message: The status message., defaults to None
    :type message: str, optional
    :param url: (statusCode 202 only) The URL for the download., defaults to None
    :type url: str, optional
    """

    def __init__(
        self,
        status_code: str = SENTINEL,
        message: str = SENTINEL,
        url: str = SENTINEL,
        **kwargs
    ):
        """LogDownload

        :param status_code: The status code as one of the following:   - 202 — status message: Beginning download.  - 504 — status message: Runtime is unavailable., defaults to None
        :type status_code: str, optional
        :param message: The status message., defaults to None
        :type message: str, optional
        :param url: (statusCode 202 only) The URL for the download., defaults to None
        :type url: str, optional
        """
        if status_code is not SENTINEL:
            self.status_code = status_code
        if message is not SENTINEL:
            self.message = message
        if url is not SENTINEL:
            self.url = url
        self._kwargs = kwargs
