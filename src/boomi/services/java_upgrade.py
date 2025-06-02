
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import JavaUpgrade


class JavaUpgradeService(BaseService):

    @cast_models
    def create_java_upgrade(
        self, request_body: JavaUpgrade = None
    ) -> Union[JavaUpgrade, str]:
        """Download and run the Java upgrader script for a specified Runtime, Runtime cluster, Runtime cloud, Authentication Broker, or API Gateway.  Upgrades your selected container to Boomis latest supported version of Java.

         - After providing the endpoint and a request body that includes the containerID, the CREATE operation immediately upgrades the given container to Boomi's latest supported version of Java. After performing a CREATE operation, you can determine a successful upgrade when the **Update to use Java 11.<minor_version>** link no longer appears on the following pages:
          -  For Runtimes, Runtime clusters, and Runtime clouds — the **Runtime Information** panel (**Manage** > **Runtime Management** of the user interface).
          -  For Brokers (applicable for versions newer than 1.8.0_281-b09)— the **Broker Information** panel (**Configure Server** > **Authentication** of the user interface).
          -  For API Gateways — the **Gateway Information** panel (**Configure Server** > **Gateways** of the user interface).
         - You must have the **Runtime Management** privilege to perform the CREATE operation. If you have the **Runtime Management Read Access** privilege, you cannot use this operation to upgrade your container.
         - The container must be online to use the Upgrade Java operation.
        - The container must be eligible for upgrade.

         >**Important:** Only the node that runs upgrades (typically the head node) restarts automatically to run the updated Java version. Therefore, you must restart all other cluster nodes to install the upgrade.

        :param request_body: The request body., defaults to None
        :type request_body: JavaUpgrade, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[JavaUpgrade, str]
        """

        Validator(JavaUpgrade).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/JavaUpgrade",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return JavaUpgrade._unmap(response)
        if content == "application/xml":
            return JavaUpgrade._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)
