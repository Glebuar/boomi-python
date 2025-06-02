
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..net.transport.utils import parse_xml_to_dict
from ..models import (
    ComponentDiffRequest,
    ComponentDiffRequestBulkRequest,
    ComponentDiffRequestBulkResponse,
    ComponentDiffResponseCreate,
)


class ComponentDiffRequestService(BaseService):

    @cast_models
    def create_component_diff_request(
        self, request_body: ComponentDiffRequest = None
    ) -> Union[ComponentDiffResponseCreate, str]:
        """Contains a diff visualization option to help understand the differences between component versions. For more information, refer to the Postman article [Visualize request responses using Postman Visualizer](https://learning.postman.com/docs/sending-requests/response-data/visualizer/).

        :param request_body: The request body., defaults to None
        :type request_body: ComponentDiffRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ComponentDiffResponseCreate, str]
        """

        Validator(ComponentDiffRequest).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ComponentDiffRequest",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return ComponentDiffResponseCreate._unmap(response)
        if content == "application/xml":
            return ComponentDiffResponseCreate._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def get_component_diff_request(
        self, component_id: str
    ) -> Union[ComponentDiffRequest, str]:
        """If you use Postman to make API calls, the GET response contains a diff visualization option to help understand the differences between component versions. For more information, refer to the Postman article [Visualize request responses using Postman Visualizer](https://learning.postman.com/docs/sending-requests/response-data/visualizer/). The Postman visualization feature currently supports only JSON responses.

        :param component_id: The ID of the component for which you want to compare versions.
        :type component_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ComponentDiffRequest, str]
        """

        Validator(str).validate(component_id)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ComponentDiffRequest/{{componentId}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("componentId", component_id)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return ComponentDiffRequest._unmap(response)
        if content == "application/xml":
            return ComponentDiffRequest._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def bulk_component_diff_request(
        self, request_body: ComponentDiffRequestBulkRequest = None
    ) -> Union[ComponentDiffRequestBulkResponse, str]:
        """To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

        :param request_body: The request body., defaults to None
        :type request_body: ComponentDiffRequestBulkRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ComponentDiffRequestBulkResponse, str]
        """

        Validator(ComponentDiffRequestBulkRequest).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ComponentDiffRequest/bulk",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return ComponentDiffRequestBulkResponse._unmap(response)
        if content == "application/xml":
            return ComponentDiffRequestBulkResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)
