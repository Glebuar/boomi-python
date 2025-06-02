
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import (
    EnvironmentMapExtensionUserDefinedFunction,
    EnvironmentMapExtensionUserDefinedFunctionBulkRequest,
    EnvironmentMapExtensionUserDefinedFunctionBulkResponse,
)


class EnvironmentMapExtensionUserDefinedFunctionService(BaseService):

    @cast_models
    def create_environment_map_extension_user_defined_function(
        self, request_body: EnvironmentMapExtensionUserDefinedFunction = None
    ) -> Union[EnvironmentMapExtensionUserDefinedFunction, str]:
        """The CREATE operation creates a new extensible user-defined function. User-defined functions created using the Environment Map Extension User Defined Function object exists only at the environment extension level and are tied to a single map extension only.

         When creating a new user-defined function, you define individual function steps that make up the greater user-defined function. Then, in the `<Mappings>` section of the request, you determine how to map or link each step to and from the function's input and output.

         >**Caution:** Creating new functions requires all existing input and output values in the request regardless if they are mapped or populated with a default value. Otherwise, it overrides and removes those variables from the function.

        :param request_body: The request body., defaults to None
        :type request_body: EnvironmentMapExtensionUserDefinedFunction, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[EnvironmentMapExtensionUserDefinedFunction, str]
        """

        Validator(EnvironmentMapExtensionUserDefinedFunction).is_optional().validate(
            request_body
        )

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/EnvironmentMapExtensionUserDefinedFunction",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return EnvironmentMapExtensionUserDefinedFunction._unmap(response)
        if content == "application/xml":
            return EnvironmentMapExtensionUserDefinedFunction._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def get_environment_map_extension_user_defined_function(
        self, id_: str
    ) -> Union[EnvironmentMapExtensionUserDefinedFunction, str]:
        """Retrieves an extensible user-defined function associated with a given environment map extension function ID.

        :param id_: Represents the unique, system-generated ID of the extended user-defined function.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[EnvironmentMapExtensionUserDefinedFunction, str]
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/EnvironmentMapExtensionUserDefinedFunction/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return EnvironmentMapExtensionUserDefinedFunction._unmap(response)
        if content == "application/xml":
            return EnvironmentMapExtensionUserDefinedFunction._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def update_environment_map_extension_user_defined_function(
        self, id_: str, request_body: EnvironmentMapExtensionUserDefinedFunction = None
    ) -> Union[EnvironmentMapExtensionUserDefinedFunction, str]:
        """Updates the extended configuration for a single user-defined function.

         >**Caution:** Updating functions require all existing input and output values in the request regardless if they are mapped or populated with a default value. Otherwise, it overrides and removes those variables from the function.

        :param request_body: The request body., defaults to None
        :type request_body: EnvironmentMapExtensionUserDefinedFunction, optional
        :param id_: Represents the unique, system-generated ID of the extended user-defined function.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[EnvironmentMapExtensionUserDefinedFunction, str]
        """

        Validator(EnvironmentMapExtensionUserDefinedFunction).is_optional().validate(
            request_body
        )
        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/EnvironmentMapExtensionUserDefinedFunction/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return EnvironmentMapExtensionUserDefinedFunction._unmap(response)
        if content == "application/xml":
            return EnvironmentMapExtensionUserDefinedFunction._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def delete_environment_map_extension_user_defined_function(self, id_: str) -> None:
        """Deletes the specified user-defined function. Deleted user-defined functions return a status of true and are no longer available for use in an API call or on the user interface.

         ### Restoring a deleted user-defined function

         Reinstate a deleted user-defined function by providing the function's id in a CREATE operation. You cannot make changes to a function during restoration (in other words, you cannot edit its values in a RESTORE request). By restoring a deleted function, it becomes available for use in an API call and in the user interface. After a successful RESTORE operation, the function returns a deleted status of false.

        :param id_: Represents the unique, system-generated ID of the extended user-defined function.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/EnvironmentMapExtensionUserDefinedFunction/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)

    @cast_models
    def bulk_environment_map_extension_user_defined_function(
        self, request_body: EnvironmentMapExtensionUserDefinedFunctionBulkRequest = None
    ) -> Union[EnvironmentMapExtensionUserDefinedFunctionBulkResponse, str]:
        """To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

        :param request_body: The request body., defaults to None
        :type request_body: EnvironmentMapExtensionUserDefinedFunctionBulkRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[EnvironmentMapExtensionUserDefinedFunctionBulkResponse, str]
        """

        Validator(
            EnvironmentMapExtensionUserDefinedFunctionBulkRequest
        ).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/EnvironmentMapExtensionUserDefinedFunction/bulk",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return EnvironmentMapExtensionUserDefinedFunctionBulkResponse._unmap(
                response
            )
        if content == "application/xml":
            return EnvironmentMapExtensionUserDefinedFunctionBulkResponse._unmap(
                response
            )
        raise ApiError("Error on deserializing the response.", status, response)
