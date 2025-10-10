
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..net.transport.utils import parse_xml_to_dict
from ..models import (
    Branch,
    BranchBulkRequest,
    BranchBulkResponse,
    BranchQueryConfig,
    BranchQueryResponse,
)


class BranchService(BaseService):

    @cast_models
    def create_branch(self, request_body: Branch = None) -> Union[Branch, str]:
        """- To create a branch, you need the branch ID for the branch from which you want to create a new branch. New branches return ready as false until the creating stage has cleared.
         - You can also create a branch from a packaged component. To do so, use the ID of the packaged component as the packageId.
         - To create a branch from a deployment, use the ID of the deployment for the packageId.

        :param request_body: The request body., defaults to None
        :type request_body: Branch, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[Branch, str]
        """

        Validator(Branch).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/Branch",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return Branch._unmap(response)
        if content == "application/xml":
            return Branch._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def get_branch(self, id_: str) -> Union[Branch, str]:
        """When you have the branch ID, you can query for additional information about the branch. Send an HTTP GET where {accountId} is the ID of the authenticating account and {branchId} is the ID of the branch you want to query.

        :param id_: The ID of the branch.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[Branch, str]
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/Branch/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return Branch._unmap(response)
        if content == "application/xml":
            return Branch._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def update_branch(
        self, id_: str, request_body: Branch = None
    ) -> Union[Branch, str]:
        """To update a branch, you need the branch ID. Currently, you can only update the name of the branch.

        :param request_body: The request body., defaults to None
        :type request_body: Branch, optional
        :param id_: The ID of the branch.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[Branch, str]
        """

        Validator(Branch).is_optional().validate(request_body)
        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/Branch/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return Branch._unmap(response)
        if content == "application/xml":
            return Branch._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def delete_branch(self, id_: str) -> None:
        """Deletes a branch

        :param id_: The ID of the branch.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/Branch/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)

    @cast_models
    def bulk_branch(
        self, request_body: BranchBulkRequest = None
    ) -> Union[BranchBulkResponse, str]:
        """To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

        :param request_body: The request body., defaults to None
        :type request_body: BranchBulkRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[BranchBulkResponse, str]
        """

        Validator(BranchBulkRequest).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/Branch/bulk",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return BranchBulkResponse._unmap(response)
        if content == "application/xml":
            return BranchBulkResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_branch(
        self, request_body: BranchQueryConfig = None
    ) -> Union[BranchQueryResponse, str]:
        """You must first retrieve the ID of your main branch, using the name of your current branch. If you haven't created any branches, your current branch will be `main`.

         When you query a branch, it might be in one of the following states:
         - `CREATING`: The branch is being created
         - `NORMAL`: The branch is ready to use
         - `DELETING`: The branch is being deleted.

         For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body., defaults to None
        :type request_body: BranchQueryConfig, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[BranchQueryResponse, str]
        """

        Validator(BranchQueryConfig).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/Branch/query",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return BranchQueryResponse._unmap(response)
        if content == "application/xml":
            return BranchQueryResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_more_branch(self, request_body: str) -> Union[BranchQueryResponse, str]:
        """To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body.
        :type request_body: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[BranchQueryResponse, str]
        """

        Validator(str).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/Branch/queryMore",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body, "text/plain")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return BranchQueryResponse._unmap(response)
        if content == "application/xml":
            return BranchQueryResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)
