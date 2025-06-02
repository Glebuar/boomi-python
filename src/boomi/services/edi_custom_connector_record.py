
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..net.transport.utils import parse_xml_to_dict
from ..models import (
    EdiCustomConnectorRecordQueryConfig,
    EdiCustomConnectorRecordQueryResponse,
)


class EdiCustomConnectorRecordService(BaseService):

    @cast_models
    def query_edi_custom_connector_record(
        self, request_body: EdiCustomConnectorRecordQueryConfig = None
    ) -> Union[EdiCustomConnectorRecordQueryResponse, str]:
        """- To filter by a customField, use the format customFields. Use fieldName as the filter property where fieldName is the element name of the custom field in the EDI Custom Connector Record structure. To get a list of the available custom fields, refer to [Custom Tracked Field object](#tag/CustomTrackedField).
         - The STARTS_WITH operator accepts values that do not include spaces.
         - Sorting of the Query results are by the `dateProcessed` field value, from the oldest to the newest.

         For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body., defaults to None
        :type request_body: EdiCustomConnectorRecordQueryConfig, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[EdiCustomConnectorRecordQueryResponse, str]
        """

        Validator(EdiCustomConnectorRecordQueryConfig).is_optional().validate(
            request_body
        )

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/EdiCustomConnectorRecord/query",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return EdiCustomConnectorRecordQueryResponse._unmap(response)
        if content == "application/xml":
            return EdiCustomConnectorRecordQueryResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_more_edi_custom_connector_record(
        self, request_body: str
    ) -> Union[EdiCustomConnectorRecordQueryResponse, str]:
        """To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body.
        :type request_body: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[EdiCustomConnectorRecordQueryResponse, str]
        """

        Validator(str).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/EdiCustomConnectorRecord/queryMore",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body, "text/plain")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return EdiCustomConnectorRecordQueryResponse._unmap(response)
        if content == "application/xml":
            return EdiCustomConnectorRecordQueryResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)
