
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import JavaRollback


class JavaRollbackService(BaseService):

    @cast_models
    def execute_java_rollback(
        self, id_: str, request_body: JavaRollback = None
    ) -> Union[JavaRollback, str]:
        """Returns a Runtime, Runtime cluster, Runtime cloud, Authentication Broker, or Gateway to use the previous version of Java with an EXECUTE operation.

         - After performing the EXECUTE operation, you can determine the success of returning to an earlier version when the **Update to use <new Java version>.<minor_version>** link displays on the following pages, indicating that a more recent version is available for upgrade:

          - For Runtimes, Runtime clusters, and Runtime clouds — the **Runtime Information** panel (**Manage** > **Runtime Management** of the user interface).

          - For Brokers — the **Broker Information** panel (**Configure Server** > **Authentication** of the user interface).

          - For API Gateways — the **Gateway Information** panel (**Configure Server** > **Gateways** of the user interface).

          To verify a successful rollback on a Runtime using the user interface, you can also navigate to **Runtime Management** > **Startup Properties** and reference the Java version number listed in the **Java Home** field.

        - The container must be online to use the Rollback Java operation.

         >**Important:** Only the node that runs upgrades (typically the head node) restarts automatically to run the updated Java version for Runtimes, Runtime clusters, and Runtime clouds. You must restart all other cluster nodes to successfully return to a previous version of Java.
         > To successfully return to a previous version of Java for API Management Gateways and Authentication Brokers, you must restart all Gateways and Brokers.

        :param request_body: The request body., defaults to None
        :type request_body: JavaRollback, optional
        :param id_: The unique ID assigned by the system to the container.

        1. Use the Runtime ID for Runtimes, Runtime clusters, and Runtime clouds found in the user interface by navigating to **Manage** > **Runtime Management** and viewing the Runtime Information panel for a selected container.

        2. Use the Gateway ID found in the user interface by navigating to **Configure Server** > **Gateways** > `<gatewayName>` > Gateway Information panel.

        3. Use the Broker ID found in the user interface by navigating to **Configure Server** > **Authentication** > `<brokerName>` > Broker Information panel.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[JavaRollback, str]
        """

        Validator(JavaRollback).is_optional().validate(request_body)
        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/JavaRollback/execute/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return JavaRollback._unmap(response)
        if content == "application/xml":
            return JavaRollback._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)
