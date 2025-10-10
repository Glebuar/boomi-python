
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import (
    PackagedComponentManifest,
    PackagedComponentManifestBulkRequest,
    PackagedComponentManifestBulkResponse,
)


class PackagedComponentManifestService(BaseService):

    @cast_models
    def get_packaged_component_manifest(
        self, package_id: str
    ) -> Union[PackagedComponentManifest, str]:
        """Retrieve a list of the included components and their summary metadata for a single version of a packaged component.

        :param package_id: The ID of the packaged component.
        :type package_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[PackagedComponentManifest, str]
        """

        Validator(str).validate(package_id)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/PackagedComponentManifest/{{packageId}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("packageId", package_id)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return PackagedComponentManifest._unmap(response)
        if content == "application/xml":
            return PackagedComponentManifest._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def bulk_packaged_component_manifest(
        self, request_body: PackagedComponentManifestBulkRequest = None
    ) -> Union[PackagedComponentManifestBulkResponse, str]:
        """To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

        :param request_body: The request body., defaults to None
        :type request_body: PackagedComponentManifestBulkRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[PackagedComponentManifestBulkResponse, str]
        """

        Validator(PackagedComponentManifestBulkRequest).is_optional().validate(
            request_body
        )

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/PackagedComponentManifest/bulk",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return PackagedComponentManifestBulkResponse._unmap(response)
        if content == "application/xml":
            return PackagedComponentManifestBulkResponse._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)
