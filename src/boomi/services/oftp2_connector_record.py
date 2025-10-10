
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import Oftp2ConnectorRecordQueryConfig, Oftp2ConnectorRecordQueryResponse


class Oftp2ConnectorRecordService(BaseService):

    @cast_models
    def query_oftp2_connector_record(
        self, request_body: Oftp2ConnectorRecordQueryConfig = None
    ) -> Union[Oftp2ConnectorRecordQueryResponse, str]:
        """For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

        To filter by a custom field, use the format `customFields/fieldName` as the filter property, where `fieldName` is the element name of the custom field in the OFTP2 Connector Record structure. To get a list of the available custom fields, see [Custom Tracked Field](/api/platformapi#tag/CustomTrackedField) object.



         The STARTS_WITH operator accepts only values that do not include spaces.

         Sorting of the QUERY results are by the dateProcessed field value, from the oldest to the newest.

        :param request_body: The request body., defaults to None
        :type request_body: Oftp2ConnectorRecordQueryConfig, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[Oftp2ConnectorRecordQueryResponse, str]
        """

        Validator(Oftp2ConnectorRecordQueryConfig).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/OFTP2ConnectorRecord/query",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return Oftp2ConnectorRecordQueryResponse._unmap(response)
        if content == "application/xml":
            return Oftp2ConnectorRecordQueryResponse._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_more_oftp2_connector_record(
        self, request_body: str
    ) -> Union[Oftp2ConnectorRecordQueryResponse, str]:
        """To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body.
        :type request_body: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[Oftp2ConnectorRecordQueryResponse, str]
        """

        Validator(str).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/OFTP2ConnectorRecord/queryMore",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body, "text/plain")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return Oftp2ConnectorRecordQueryResponse._unmap(response)
        if content == "application/xml":
            return Oftp2ConnectorRecordQueryResponse._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)
