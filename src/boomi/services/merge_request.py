
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import (
    MergeRequest,
    MergeRequestBulkRequest,
    MergeRequestBulkResponse,
    MergeRequestQueryConfig,
    MergeRequestQueryResponse,
)


class MergeRequestService(BaseService):

    @cast_models
    def create_merge_request(
        self, request_body: MergeRequest = None
    ) -> Union[MergeRequest, str]:
        """You can use the Merge Request object to merge a development branch into the main branch.

         - To create a merge request, you need the branch IDs for the source and destination branches. The source branch is the branch you want to merge into the destination branch.

        - There are two merge request strategies you can choose from: OVERRIDE or CONFLICT_RESOLVE. An override merge automatically resolves any merge conflicts by prioritizing the branch specified in the `priorityBranch` field. If you choose the CONFLICT_RESOLVE strategy, you have the opportunity to review any conflicts and choose which version you want to keep.

        :param request_body: The request body., defaults to None
        :type request_body: MergeRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[MergeRequest, str]
        """

        Validator(MergeRequest).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/MergeRequest",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return MergeRequest._unmap(response)
        if content == "application/xml":
            return MergeRequest._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def get_merge_request(self, id_: str) -> Union[MergeRequest, str]:
        """Retrieve more information about the recently performed merge.

         - The `resolution` parameter is generated from the original merge request and specifies either the source branch for the final content for the merge or the destination. It can have the following values:

          -  OVERRIDE: The source branch has taken priority
          -  KEEP_DESTINATION: The destination branch has taken priority
         - The `changeType` parameter is generated from a branch diff that is performed on merge and can be one of the following values:
          -  ADDED: A component was added to the source branch
          -  MODIFIED: A component was modified in the source branch
          -  DELETED: A component was deleted in the source branch

         After performing a merge request between two branches, you can use the merge request’s ID to retrieve more information about the recently performed merge. The following example shows a merge between two branches where something was deleted in the source branch:

         Send an HTTP GET to `https://api.boomi.com/api/rest/v1/{accountId}/MergeRequest/{mergeRequestId}` where `{accountId}` is the ID of the authenticating account and `{mergeRequestId}` is the ID of the merge request.

         You can also use the GET operation to view a user's current working branch:

         Send an HTTP GET to `https://api.boomi.com/api/rest/v1/{accountId}/UserAccountProperty/defaultWorkingBranch` where the `{accountId}` is the ID of the account for which you want to view the working branch.

        :param id_: ID of the merge request.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[MergeRequest, str]
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/MergeRequest/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return MergeRequest._unmap(response)
        if content == "application/xml":
            return MergeRequest._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def update_merge_request(
        self, id_: str, request_body: MergeRequest = None
    ) -> Union[MergeRequest, str]:
        """update_merge_request

        :param request_body: The request body., defaults to None
        :type request_body: MergeRequest, optional
        :param id_: ID of the merge request.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[MergeRequest, str]
        """

        Validator(MergeRequest).is_optional().validate(request_body)
        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/MergeRequest/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return MergeRequest._unmap(response)
        if content == "application/xml":
            return MergeRequest._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def delete_merge_request(self, id_: str) -> None:
        """- There are three actions you can choose from when executing a merge request:
         -  MERGE: Use to start or restart a merge request; the `stage` must be REVIEWING or FAILED_TO_MERGE
         -  REVERT: Use to revert a merge request; the `stage` must be MERGED or DELETED and `previousStage` is MERGED
         -  RETRY_DRAFTING: Use when the merge request `stage` is FAILED_TO_DRAFT or FAILED_TO_REDRAFT
         - If the merge is successful, the `stage` and/or `previousStage` might be in one of the following stages:
         -  DRAFTING: The merge request is in the queue.
        -  DRAFTED: The merge request is drafted for review.
        -  REVIEWING: The merge request is being reviewed.
        -  MERGING: The merge request is being processed.
        -  MERGED: The merge request has successfully completed.
        -  FAILED_TO_MERGE: The merge request failed to merge.
        -  NOT_EXIST: No previous merge request has been submitted. This stage is typically returned in the `previousStage` parameter.

        :param id_: id_
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/MergeRequest/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)

    @cast_models
    def bulk_merge_request(
        self, request_body: MergeRequestBulkRequest = None
    ) -> Union[MergeRequestBulkResponse, str]:
        """To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

        :param request_body: The request body., defaults to None
        :type request_body: MergeRequestBulkRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[MergeRequestBulkResponse, str]
        """

        Validator(MergeRequestBulkRequest).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/MergeRequest/bulk",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return MergeRequestBulkResponse._unmap(response)
        if content == "application/xml":
            return MergeRequestBulkResponse._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def execute_merge_request(
        self, id_: str, request_body: MergeRequest = None
    ) -> Union[MergeRequest, str]:
        """- These are the actions you can choose from when executing a merge request:
          -  MERGE: Use to start or restart a merge request; the stage must be REVIEWING or FAILED_TO_MERGE
          -  REVERT: Use to revert a merge request; the stage must be MERGED or DELETED and previousStage is MERGED
          -  RETRY_DRAFTING: Use when the merge request stage is FAILED_TO_DRAFT or FAILED_TO_REDRAFT
        - If the merge is successful, the `stage` and/or `previousStage` might be in one of the following stages:
          -  DRAFTING - The merge request is in the queue.
          -  DRAFTED - The merge request is drafted for review.
          -  REVIEWING - The merge request is being reviewed.
          * MERGING - The merge request is being processed.
          * MERGED - The merge request has successfully completed.
          * FAILED_TO_MERGE - The merge request failed to merge.

        :param request_body: The request body., defaults to None
        :type request_body: MergeRequest, optional
        :param id_: id_
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[MergeRequest, str]
        """

        Validator(MergeRequest).is_optional().validate(request_body)
        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/MergeRequest/execute/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return MergeRequest._unmap(response)
        if content == "application/xml":
            return MergeRequest._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_merge_request(
        self, request_body: MergeRequestQueryConfig = None
    ) -> Union[MergeRequestQueryResponse, str]:
        """- You can query a branch to retrieve a list of all active merge request IDs.
          - You must include the destination or source branch as a parameter. Only EQUALS is allowed for these parameters.
         - Optional parameters include:
          -   `createdDate`
          -   `createdBy`
          -   `stage`
          -   `modifiedDate`
          -   `modifiedBy`
        -  You can use the `queryMore` request to return more than 100 results.

        For more information about query filters, refer to [Query filters](/api/platformapi#section/Introduction/Query-filters).

        :param request_body: The request body., defaults to None
        :type request_body: MergeRequestQueryConfig, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[MergeRequestQueryResponse, str]
        """

        Validator(MergeRequestQueryConfig).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/MergeRequest/query",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return MergeRequestQueryResponse._unmap(response)
        if content == "application/xml":
            return MergeRequestQueryResponse._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_more_merge_request(
        self, request_body: str
    ) -> Union[MergeRequestQueryResponse, str]:
        """To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body.
        :type request_body: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[MergeRequestQueryResponse, str]
        """

        Validator(str).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/MergeRequest/queryMore",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body, "text/plain")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return MergeRequestQueryResponse._unmap(response)
        if content == "application/xml":
            return MergeRequestQueryResponse._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)
