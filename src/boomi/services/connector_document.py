
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..net.transport.utils import parse_xml_to_dict
from ..models import ConnectorDocument, ConnectorDocumentDownload


class ConnectorDocumentService(BaseService):

    @cast_models
    def create_connector_document(
        self, request_body: ConnectorDocument = None
    ) -> Union[ConnectorDocumentDownload, str]:
        """The Connector Document operation allows you to download the raw, document data for a specific Generic Connector Record. This action submits the download request and the call returns a URL used to download the actual document data.

        :param request_body: The request body., defaults to None
        :type request_body: ConnectorDocument, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ConnectorDocumentDownload, str]
        """

        Validator(ConnectorDocument).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ConnectorDocument",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return ConnectorDocumentDownload._unmap(response)
        if content == "application/xml":
            return ConnectorDocument._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)
