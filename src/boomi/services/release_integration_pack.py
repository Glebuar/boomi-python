
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import ReleaseIntegrationPack


class ReleaseIntegrationPackService(BaseService):

    @cast_models
    def create_release_integration_pack(
        self, request_body: ReleaseIntegrationPack = None
    ) -> Union[ReleaseIntegrationPack, str]:
        """Creates an immediate or scheduled release for a publisher integration pack.

        To schedule the publisher integration pack for release, you must specify the release schedule (immediate or scheduled).
        The `releaseOnDate` field is required if you schedule the release for a future date.

        :param request_body: The request body., defaults to None
        :type request_body: ReleaseIntegrationPack, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ReleaseIntegrationPack, str]
        """

        Validator(ReleaseIntegrationPack).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ReleaseIntegrationPack",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return ReleaseIntegrationPack._unmap(response)
        if content == "application/xml":
            return ReleaseIntegrationPack._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def update_release_integration_pack(
        self, id_: str, request_body: ReleaseIntegrationPack = None
    ) -> Union[ReleaseIntegrationPack, str]:
        """Modifies the scheduled release of a publisher integration pack.

         > **Note:** The Update operation is only performed when there is an existing scheduled release request for the integration pack.

        :param request_body: The request body., defaults to None
        :type request_body: ReleaseIntegrationPack, optional
        :param id_: id_
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ReleaseIntegrationPack, str]
        """

        Validator(ReleaseIntegrationPack).is_optional().validate(request_body)
        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ReleaseIntegrationPack/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return ReleaseIntegrationPack._unmap(response)
        if content == "application/xml":
            return ReleaseIntegrationPack._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)
