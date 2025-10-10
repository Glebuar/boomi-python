
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..net.transport.utils import parse_xml_to_dict
from ..models import (
    AccountCloudAttachmentQuota,
    AccountCloudAttachmentQuotaBulkRequest,
    AccountCloudAttachmentQuotaBulkResponse,
)


class AccountCloudAttachmentQuotaService(BaseService):

    @cast_models
    def create_account_cloud_attachment_quota(
        self, request_body: AccountCloudAttachmentQuota = None
    ) -> Union[AccountCloudAttachmentQuota, str]:
        """- Use the CREATE operation to create a new Cloud quota and determine the maximum number of Runtime attachments that you can create on the account.
         - You can use the CREATE or UPDATE operations interchangeably to edit a Cloud quota value. Both operations can act as an update after creating the quota.
         - CREATE and UPDATE use the same REST endpoint, as seen in the next section of sample code REST calls. When calling the endpoint for an account that has a quota set, the endpoint acts as an update and modifies the existing value, as explained in the previous item. When calling the endpoint for an account that does not already have a quota set, the endpoint creates a new quota.
         - You cannot set the Cloud quota less than the number of attachments that currently exist on the account, unless you are setting the value to -1 for unlimited. Attempting to do so returns an error.
         - The CREATE operation returns an id value that you can use in a GET operation to retrieve the existing quota for a specific account's Cloud ID.

        :param request_body: The request body., defaults to None
        :type request_body: AccountCloudAttachmentQuota, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[AccountCloudAttachmentQuota, str]
        """

        Validator(AccountCloudAttachmentQuota).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/AccountCloudAttachmentQuota",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return AccountCloudAttachmentQuota._unmap(response)
        if content == "application/xml":
            return AccountCloudAttachmentQuota._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def get_account_cloud_attachment_quota(
        self, id_: str
    ) -> Union[AccountCloudAttachmentQuota, str]:
        """Retrieves the Cloud quota value currently existing for a Cloud ID on a specific account. The GET operation requires an additional ID (id), and differs from the `cloudId` and `accountId`.

        :param id_: A unique ID generated for a newly created or recently updated Cloud quota (using the Account Cloud Attachment quota object). You can use this ID to get a Cloud quota for an account's specific Cloud ID.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[AccountCloudAttachmentQuota, str]
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/AccountCloudAttachmentQuota/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return AccountCloudAttachmentQuota._unmap(response)
        if content == "application/xml":
            return AccountCloudAttachmentQuota._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def update_account_cloud_attachment_quota(
        self, id_: str, request_body: AccountCloudAttachmentQuota = None
    ) -> Union[AccountCloudAttachmentQuota, str]:
        """Edit the number of Runtime attachments that you can create on the given account. Specify the IDs of both the account and the Runtime cloud that you want to update. You cannot set the Cloud quota less than the number of attachments that currently exist on the account, unless you are setting the value to -1 for unlimited. Attempting to do so returns an error.

        :param request_body: The request body., defaults to None
        :type request_body: AccountCloudAttachmentQuota, optional
        :param id_: A unique ID generated for a newly created or recently updated Cloud quota (using the Account Cloud Attachment quota object). You can use this ID to get a Cloud quota for an account's specific Cloud ID.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[AccountCloudAttachmentQuota, str]
        """

        Validator(AccountCloudAttachmentQuota).is_optional().validate(request_body)
        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/AccountCloudAttachmentQuota/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return AccountCloudAttachmentQuota._unmap(response)
        if content == "application/xml":
            return AccountCloudAttachmentQuota._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def delete_account_cloud_attachment_quota(self, id_: str) -> None:
        """Deletes a Cloud quota for a given account.

        :param id_: A unique ID generated for a newly created or recently updated Cloud quota (using the Account Cloud Attachment quota object). You can use this ID to get a Cloud quota for an account's specific Cloud ID.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/AccountCloudAttachmentQuota/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)

    @cast_models
    def bulk_account_cloud_attachment_quota(
        self, request_body: AccountCloudAttachmentQuotaBulkRequest = None
    ) -> Union[AccountCloudAttachmentQuotaBulkResponse, str]:
        """To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

        :param request_body: The request body., defaults to None
        :type request_body: AccountCloudAttachmentQuotaBulkRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[AccountCloudAttachmentQuotaBulkResponse, str]
        """

        Validator(AccountCloudAttachmentQuotaBulkRequest).is_optional().validate(
            request_body
        )

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/AccountCloudAttachmentQuota/bulk",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return AccountCloudAttachmentQuotaBulkResponse._unmap(response)
        if content == "application/xml":
            return AccountCloudAttachmentQuotaBulkResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)
