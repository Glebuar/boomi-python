
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..net.transport.utils import parse_xml_to_dict
from ..models import (
    AsyncOperationTokenResult,
    AtomSecurityPolicies,
    AtomSecurityPoliciesAsyncResponse,
)


class AtomSecurityPoliciesService(BaseService):

    @cast_models
    def update_atom_security_policies(
        self, id_: str, request_body: AtomSecurityPolicies = None
    ) -> Union[AtomSecurityPolicies, str]:
        """Updates the security policy for the specified Runtime cloud or Runtime cluster. You can add, update, or delete permissions by using the UPDATE operation. You can add custom Java runtime permissions you specify in an UPDATE operation to the appropriate High-security policy file. In addition, all High-security policy files contain custom permissions that you specify in the <common> section.
         As confirmation of the changes made, the UPDATE operation returns a copy of the request.

        :param request_body: The request body., defaults to None
        :type request_body: AtomSecurityPolicies, optional
        :param id_: The runtime (container) id for the applicable runtime (accepts only Runtime cloud cluster and regular Runtime cluster types, no basic runtimes or cloud attachments).
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[AtomSecurityPolicies, str]
        """

        Validator(AtomSecurityPolicies).is_optional().validate(request_body)
        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/AtomSecurityPolicies/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return AtomSecurityPolicies._unmap(response)
        if content == "application/xml":
            return AtomSecurityPolicies._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def async_get_atom_security_policies(
        self, id_: str
    ) -> Union[AsyncOperationTokenResult, str]:
        """The initial GET operation returns a security policy token for the specified Runtime cloud or Runtime cluster. Subsequent GET operations return status code 202 (while the request is in progress) or the custom contents of a security policy based on the token that was returned.

         The GET operation returns only custom runtime permissions that you added to the security policy, not the entire policy file. If you did not update the security policy for a given Runtime cloud or Runtime cluster, the response to a GET operation is empty.

        :param id_: The runtime (container) id for the applicable runtime (accepts only Runtime cloud cluster and regular runtime cluster types, no basic runtimes or cloud attachments).
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[AsyncOperationTokenResult, str]
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/async/AtomSecurityPolicies/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return AsyncOperationTokenResult._unmap(response)
        if content == "application/xml":
            return AsyncOperationTokenResult._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def async_token_atom_security_policies(
        self, token: str
    ) -> Union[AtomSecurityPoliciesAsyncResponse, str]:
        """Using the token from the initial GET response, send an HTTP GET where accountId is the account with which you are authenticating.

         Custom Java runtime permissions listed in the `<common>` section apply to all High security policy files (procrunner-HIGH.policy, procbrowser-HIGH.policy, and procworker-HIGH.policy). Custom permissions listed in a specific section, such as `<runner>`, apply only to the associated security policy file.

        :param token: Takes in the token from a previous call to return a result.
        :type token: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[AtomSecurityPoliciesAsyncResponse, str]
        """

        Validator(str).validate(token)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/async/AtomSecurityPolicies/response/{{token}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("token", token)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return AtomSecurityPoliciesAsyncResponse._unmap(response)
        if content == "application/xml":
            return AtomSecurityPoliciesAsyncResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)
