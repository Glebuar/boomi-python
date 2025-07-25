
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..net.transport.utils import parse_xml_to_dict
from ..models import (
    EnvironmentAtomAttachment,
    EnvironmentAtomAttachmentQueryConfig,
    EnvironmentAtomAttachmentQueryResponse,
)


class EnvironmentAtomAttachmentService(BaseService):

    @cast_models
    def create_environment_atom_attachment(
        self, request_body: EnvironmentAtomAttachment = None
    ) -> Union[EnvironmentAtomAttachment, str]:
        """Attaches a Runtime having the specified ID to the environment having the specified ID. Attaching an already attached Runtime moves the Runtime to the environment specified in the request.

         >**Note:** For accounts with Basic environment support, you can attach a single Runtime to each environment. For accounts with Unlimited environment support, you can attach have an unlimited number of Runtimes attached in each environment.

        :param request_body: The request body., defaults to None
        :type request_body: EnvironmentAtomAttachment, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[EnvironmentAtomAttachment, str]
        """

        Validator(EnvironmentAtomAttachment).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/EnvironmentAtomAttachment",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return EnvironmentAtomAttachment._unmap(response)
        if content == "application/xml":
            return EnvironmentAtomAttachment._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_environment_atom_attachment(
        self, request_body: EnvironmentAtomAttachmentQueryConfig = None
    ) -> Union[EnvironmentAtomAttachmentQueryResponse, str]:
        """For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body., defaults to None
        :type request_body: EnvironmentAtomAttachmentQueryConfig, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[EnvironmentAtomAttachmentQueryResponse, str]
        """

        Validator(EnvironmentAtomAttachmentQueryConfig).is_optional().validate(
            request_body
        )

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/EnvironmentAtomAttachment/query",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return EnvironmentAtomAttachmentQueryResponse._unmap(response)
        if content == "application/xml":
            return EnvironmentAtomAttachmentQueryResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_more_environment_atom_attachment(
        self, request_body: str
    ) -> Union[EnvironmentAtomAttachmentQueryResponse, str]:
        """To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body.
        :type request_body: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[EnvironmentAtomAttachmentQueryResponse, str]
        """

        Validator(str).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/EnvironmentAtomAttachment/queryMore",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body, "text/plain")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return EnvironmentAtomAttachmentQueryResponse._unmap(response)
        if content == "application/xml":
            return EnvironmentAtomAttachmentQueryResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def delete_environment_atom_attachment(self, id_: str) -> None:
        """Detaches a Runtime from an environment where the attachment is specified by the conceptual Environment Atom Attachment object ID. This ID is returned by the CREATE operation that originated the attachment and can also be obtained from a QUERY operation. If you successfully detach the Runtime from the environment, the response is  `<true/>`.

        :param id_: The object’s conceptual ID, which is synthesized from the Runtime and environment IDs.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/EnvironmentAtomAttachment/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)
