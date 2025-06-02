
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import (
    ProcessAtomAttachment,
    ProcessAtomAttachmentQueryConfig,
    ProcessAtomAttachmentQueryResponse,
)


class ProcessAtomAttachmentService(BaseService):

    @cast_models
    def create_process_atom_attachment(
        self, request_body: ProcessAtomAttachment = None
    ) -> Union[ProcessAtomAttachment, str]:
        """Attaches a process having the specified ID to the Runtime having the specified ID.

        :param request_body: The request body., defaults to None
        :type request_body: ProcessAtomAttachment, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ProcessAtomAttachment, str]
        """

        Validator(ProcessAtomAttachment).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ProcessAtomAttachment",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return ProcessAtomAttachment._unmap(response)
        if content == "application/xml":
            return ProcessAtomAttachment._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_process_atom_attachment(
        self, request_body: ProcessAtomAttachmentQueryConfig = None
    ) -> Union[ProcessAtomAttachmentQueryResponse, str]:
        """For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body., defaults to None
        :type request_body: ProcessAtomAttachmentQueryConfig, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ProcessAtomAttachmentQueryResponse, str]
        """

        Validator(ProcessAtomAttachmentQueryConfig).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ProcessAtomAttachment/query",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return ProcessAtomAttachmentQueryResponse._unmap(response)
        if content == "application/xml":
            return ProcessAtomAttachmentQueryResponse._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_more_process_atom_attachment(
        self, request_body: str
    ) -> Union[ProcessAtomAttachmentQueryResponse, str]:
        """To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body.
        :type request_body: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ProcessAtomAttachmentQueryResponse, str]
        """

        Validator(str).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ProcessAtomAttachment/queryMore",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body, "text/plain")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return ProcessAtomAttachmentQueryResponse._unmap(response)
        if content == "application/xml":
            return ProcessAtomAttachmentQueryResponse._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def delete_process_atom_attachment(self, id_: str) -> None:
        """Detaches a process from a Runtime where the attachment is specified by the conceptual Process Atom Attachment object ID.

        :param id_: id_
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ProcessAtomAttachment/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)
