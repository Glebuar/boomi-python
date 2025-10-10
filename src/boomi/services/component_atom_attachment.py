
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..net.transport.utils import parse_xml_to_dict
from ..models import (
    ComponentAtomAttachment,
    ComponentAtomAttachmentQueryConfig,
    ComponentAtomAttachmentQueryResponse,
)


class ComponentAtomAttachmentService(BaseService):

    @cast_models
    def create_component_atom_attachment(
        self, request_body: ComponentAtomAttachment = None
    ) -> Union[ComponentAtomAttachment, str]:
        """Attaches a component with a specific ID to the Runtime with a specific ID. You must have the Runtime Management privilege to perform the CREATE operation. If you have the Runtime Management Read Access privilege, you cannot attach components.

        :param request_body: The request body., defaults to None
        :type request_body: ComponentAtomAttachment, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ComponentAtomAttachment, str]
        """

        Validator(ComponentAtomAttachment).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ComponentAtomAttachment",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return ComponentAtomAttachment._unmap(response)
        if content == "application/xml":
            return ComponentAtomAttachment._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_component_atom_attachment(
        self, request_body: ComponentAtomAttachmentQueryConfig = None
    ) -> Union[ComponentAtomAttachmentQueryResponse, str]:
        """For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body., defaults to None
        :type request_body: ComponentAtomAttachmentQueryConfig, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ComponentAtomAttachmentQueryResponse, str]
        """

        Validator(ComponentAtomAttachmentQueryConfig).is_optional().validate(
            request_body
        )

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ComponentAtomAttachment/query",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return ComponentAtomAttachmentQueryResponse._unmap(response)
        if content == "application/xml":
            return ComponentAtomAttachmentQueryResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_more_component_atom_attachment(
        self, request_body: str
    ) -> Union[ComponentAtomAttachmentQueryResponse, str]:
        """To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body.
        :type request_body: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ComponentAtomAttachmentQueryResponse, str]
        """

        Validator(str).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ComponentAtomAttachment/queryMore",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body, "text/plain")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return ComponentAtomAttachmentQueryResponse._unmap(response)
        if content == "application/xml":
            return ComponentAtomAttachmentQueryResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def delete_component_atom_attachment(self, id_: str) -> None:
        """Detaches a component from a Runtime where the attachment is specified by the conceptual Component Atom Attachment object ID. This ID is returned by the CREATE operation that originated the attachment and can also be obtained from a QUERY operation. You must have the Runtime Management privilege to perform the DELETE operation.

        :param id_: id_
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ComponentAtomAttachment/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)
