
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..net.transport.utils import parse_xml_to_dict
from ..models import (
    Deployment,
    DeploymentBulkRequest,
    DeploymentBulkResponse,
    DeploymentQueryConfig,
    DeploymentQueryResponse,
    ProcessEnvironmentAttachmentQueryConfig,
    ProcessEnvironmentAttachmentQueryResponse,
)


class DeploymentService(BaseService):

    @cast_models
    def create_deployment(
        self, request_body: Deployment = None
    ) -> Union[Deployment, str]:
        """The Deployment object is a deprecated API and should no longer be used. Boomi recommends that you take advantage of the API functionality provided by the [Packaged Component](https://help.boomi.com/docs/Atomsphere/Integration/AtomSphere%20API/r-atm-Packaged_Component_object_66fa92c8-948f-46c6-a521-3927ab431c84) and [Deployed Package objects](https://help.boomi.com/docs/Atomsphere/Integration/AtomSphere%20API/r-atm-Deployed_Package_object_897b5068-6daa-44e4-bf04-7e25385157a8) instead.

        :param request_body: The request body., defaults to None
        :type request_body: Deployment, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[Deployment, str]
        """

        Validator(Deployment).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/Deployment",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return Deployment._unmap(response)
        if content == "application/xml":
            return Deployment._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def get_deployment(self, id_: str) -> Union[Deployment, str]:
        """The Deployment object is a deprecated API and should no longer be used. Boomi recommends that you take advantage of the API functionality provided by the [Packaged Component](https://help.boomi.com/docs/Atomsphere/Integration/AtomSphere%20API/r-atm-Packaged_Component_object_66fa92c8-948f-46c6-a521-3927ab431c84) and [Deployed Package objects](https://help.boomi.com/docs/Atomsphere/Integration/AtomSphere%20API/r-atm-Deployed_Package_object_897b5068-6daa-44e4-bf04-7e25385157a8) instead.

        :param id_: id_
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[Deployment, str]
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/Deployment/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return Deployment._unmap(response)
        if content == "application/xml":
            return Deployment._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def bulk_deployment(
        self, request_body: DeploymentBulkRequest = None
    ) -> Union[DeploymentBulkResponse, str]:
        """To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

        :param request_body: The request body., defaults to None
        :type request_body: DeploymentBulkRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[DeploymentBulkResponse, str]
        """

        Validator(DeploymentBulkRequest).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/Deployment/bulk",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return DeploymentBulkResponse._unmap(response)
        if content == "application/xml":
            return DeploymentBulkResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_deployment(
        self, request_body: DeploymentQueryConfig = None
    ) -> Union[DeploymentQueryResponse, str]:
        """For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body., defaults to None
        :type request_body: DeploymentQueryConfig, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[DeploymentQueryResponse, str]
        """

        Validator(DeploymentQueryConfig).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/Deployment/query",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return DeploymentQueryResponse._unmap(response)
        if content == "application/xml":
            return DeploymentQueryResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_more_deployment(
        self, request_body: str
    ) -> Union[DeploymentQueryResponse, str]:
        """To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body.
        :type request_body: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[DeploymentQueryResponse, str]
        """

        Validator(str).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/Deployment/queryMore",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body, "text/plain")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return DeploymentQueryResponse._unmap(response)
        if content == "application/xml":
            return DeploymentQueryResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_process_environment_attachment(
        self, request_body: ProcessEnvironmentAttachmentQueryConfig = None
    ) -> Union[ProcessEnvironmentAttachmentQueryResponse, str]:
        """For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body., defaults to None
        :type request_body: ProcessEnvironmentAttachmentQueryConfig, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ProcessEnvironmentAttachmentQueryResponse, str]
        """

        Validator(ProcessEnvironmentAttachmentQueryConfig).is_optional().validate(
            request_body
        )

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ProcessEnvironmentAttachment/query",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return ProcessEnvironmentAttachmentQueryResponse._unmap(response)
        if content == "application/xml":
            return ProcessEnvironmentAttachmentQueryResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_more_process_environment_attachment(
        self, request_body: str
    ) -> Union[ProcessEnvironmentAttachmentQueryResponse, str]:
        """To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body.
        :type request_body: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ProcessEnvironmentAttachmentQueryResponse, str]
        """

        Validator(str).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ProcessEnvironmentAttachment/queryMore",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body, "text/plain")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return ProcessEnvironmentAttachmentQueryResponse._unmap(response)
        if content == "application/xml":
            return ProcessEnvironmentAttachmentQueryResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def delete_process_environment_attachment(self, id_: str) -> None:
        """Detaches a process from an environment where the attachment is specified by the conceptual Process Environment Attachment object ID.

        :param id_: id_
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ProcessEnvironmentAttachment/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)
