
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..net.transport.utils import parse_xml_to_dict
from ..models import (
    Folder,
    FolderBulkRequest,
    FolderBulkResponse,
    FolderQueryConfig,
    FolderQueryResponse,
)


class FolderService(BaseService):

    @cast_models
    def create_folder(self, request_body: Folder = None) -> Union[Folder, str]:
        """- When using the CREATE operation, you can create a new folder within the parent folder.

        - When creating a new folder, a name is required but PermittedRoles are optional. Unless it includes a list of UserRoles, in which case the GUID is required for the UserRole.

        - `parentId` must be a valid, non-deleted folder. If omitted or blank, it defaults to the root folder.

        - To Restore a folder you need to use the CREATE operation call, using a valid GUID for a deleted item. This will also restore any deleted components within that folder.

        :param request_body: The request body., defaults to None
        :type request_body: Folder, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[Folder, str]
        """

        Validator(Folder).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/Folder",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return Folder._unmap(response)
        if content == "application/xml":
            return Folder._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def get_folder(self, id_: str) -> Union[Folder, str]:
        """Retrieves the folder with the particular ID.

        :param id_: Required. Read only. The Boomi-generated, unique identifier of the folder.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[Folder, str]
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/Folder/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return Folder._unmap(response)
        if content == "application/xml":
            return Folder._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def update_folder(
        self, id_: str, request_body: Folder = None
    ) -> Union[Folder, str]:
        """You can update by changing the name of the folder and following the same considerations for the CREATE parameters.

        :param request_body: The request body., defaults to None
        :type request_body: Folder, optional
        :param id_: Required. Read only. The Boomi-generated, unique identifier of the folder.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[Folder, str]
        """

        Validator(Folder).is_optional().validate(request_body)
        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/Folder/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return Folder._unmap(response)
        if content == "application/xml":
            return Folder._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def delete_folder(self, id_: str) -> None:
        """- Deleting a folder will delete the folder and its contents including all components and sub-folders.
         - The root folder cannot be deleted.
         - Folders containing actively deployed processes or other deployable components cannot be deleted.
         >**Note:** You can restore a deleted folder by requesting a CREATE operation and specifying the ID of the deleted folder.

        :param id_: Required. Read only. The Boomi-generated, unique identifier of the folder.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/Folder/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)

    @cast_models
    def bulk_folder(
        self, request_body: FolderBulkRequest = None
    ) -> Union[FolderBulkResponse, str]:
        """To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

        :param request_body: The request body., defaults to None
        :type request_body: FolderBulkRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[FolderBulkResponse, str]
        """

        Validator(FolderBulkRequest).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/Folder/bulk",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return FolderBulkResponse._unmap(response)
        if content == "application/xml":
            return FolderBulkResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_folder(
        self, request_body: FolderQueryConfig = None
    ) -> Union[FolderQueryResponse, str]:
        """For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

        - You can perform the QUERY operation for the Folder object by id, name, fullPath and deleted.

        - The QUERY MORE operation is also available for the Folder object.

        - You can perform an empty QUERY to return all folders.

        - If no filter is specified, both non-deleted and deleted records are returned.

        :param request_body: The request body., defaults to None
        :type request_body: FolderQueryConfig, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[FolderQueryResponse, str]
        """

        Validator(FolderQueryConfig).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/Folder/query",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return FolderQueryResponse._unmap(response)
        if content == "application/xml":
            return FolderQueryResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_more_folder(self, request_body: str) -> Union[FolderQueryResponse, str]:
        """To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body.
        :type request_body: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[FolderQueryResponse, str]
        """

        Validator(str).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/Folder/queryMore",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body, "text/plain")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return FolderQueryResponse._unmap(response)
        if content == "application/xml":
            return FolderQueryResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)
