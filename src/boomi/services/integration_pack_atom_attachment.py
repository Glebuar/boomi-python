
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import (
    IntegrationPackAtomAttachment,
    IntegrationPackAtomAttachmentQueryConfig,
    IntegrationPackAtomAttachmentQueryResponse,
)


class IntegrationPackAtomAttachmentService(BaseService):

    @cast_models
    def create_integration_pack_atom_attachment(
        self, request_body: IntegrationPackAtomAttachment = None
    ) -> Union[IntegrationPackAtomAttachment, str]:
        """Attaches an integration pack instance having the specified ID to the Runtime having the specified ID.

        :param request_body: The request body., defaults to None
        :type request_body: IntegrationPackAtomAttachment, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[IntegrationPackAtomAttachment, str]
        """

        Validator(IntegrationPackAtomAttachment).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/IntegrationPackAtomAttachment",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return IntegrationPackAtomAttachment._unmap(response)
        if content == "application/xml":
            return IntegrationPackAtomAttachment._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_integration_pack_atom_attachment(
        self, request_body: IntegrationPackAtomAttachmentQueryConfig = None
    ) -> Union[IntegrationPackAtomAttachmentQueryResponse, str]:
        """For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body., defaults to None
        :type request_body: IntegrationPackAtomAttachmentQueryConfig, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[IntegrationPackAtomAttachmentQueryResponse, str]
        """

        Validator(IntegrationPackAtomAttachmentQueryConfig).is_optional().validate(
            request_body
        )

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/IntegrationPackAtomAttachment/query",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return IntegrationPackAtomAttachmentQueryResponse._unmap(response)
        if content == "application/xml":
            return IntegrationPackAtomAttachmentQueryResponse._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_more_integration_pack_atom_attachment(
        self, request_body: str
    ) -> Union[IntegrationPackAtomAttachmentQueryResponse, str]:
        """To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body.
        :type request_body: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[IntegrationPackAtomAttachmentQueryResponse, str]
        """

        Validator(str).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/IntegrationPackAtomAttachment/queryMore",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body, "text/plain")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return IntegrationPackAtomAttachmentQueryResponse._unmap(response)
        if content == "application/xml":
            return IntegrationPackAtomAttachmentQueryResponse._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def delete_integration_pack_atom_attachment(self, id_: str) -> None:
        """Detaches an integration pack instance from a Runtime, where the attachment is specified by the conceptual Integration Pack Atom Attachment object ID. This ID can be obtained from a QUERY operation.

        :param id_: The object’s conceptual ID, which is synthesized from the Runtime and integration pack instance IDs.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/IntegrationPackAtomAttachment/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)
