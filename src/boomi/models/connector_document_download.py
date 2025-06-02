
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({"status_code": "statusCode"})
class ConnectorDocumentDownload(BaseModel):
    """ConnectorDocumentDownload

    :param url: The endpoint URL to retrieve the connector document. This URL is returned in the initial CREATE response., defaults to None
    :type url: str, optional
    :param message: message, defaults to None
    :type message: str, optional
    :param status_code: status_code, defaults to None
    :type status_code: str, optional
    """

    def __init__(
        self,
        url: str = SENTINEL,
        message: str = SENTINEL,
        status_code: str = SENTINEL,
        **kwargs
    ):
        """ConnectorDocumentDownload

        :param url: The endpoint URL to retrieve the connector document. This URL is returned in the initial CREATE response., defaults to None
        :type url: str, optional
        :param message: message, defaults to None
        :type message: str, optional
        :param status_code: status_code, defaults to None
        :type status_code: str, optional
        """
        if url is not SENTINEL:
            self.url = url
        if message is not SENTINEL:
            self.message = message
        if status_code is not SENTINEL:
            self.status_code = status_code
        self._kwargs = kwargs
