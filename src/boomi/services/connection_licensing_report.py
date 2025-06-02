
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..net.transport.utils import parse_xml_to_dict
from ..models import ConnectionLicensingDownload, ConnectionLicensingReport


class ConnectionLicensingReportService(BaseService):

    @cast_models
    def create_connection_licensing_report(
        self, request_body: ConnectionLicensingReport = None
    ) -> Union[ConnectionLicensingDownload, str]:
        """Returns the Connection Licensing URL in the response to view or download the deployed connection details. To download connection licensing data for a given connector class:

         a. Send a POST and request body to `https://api.boomi.com/api/rest/v1/<accountId>/ConnectionLicensingReport`

         where accountId is the ID of the authenticating account for the request.

         Populate the request body with or without the available filters for the report that you want to download.

         b. Next, send a GET request using the URL returned in the POST response. The GET does not require a request body, and returns the deployed connection details.

         >**Note:** Do not pass any filters in the CREATE payload. This will not help get the Test & Production connections deployed details for all the connector classes. To get the Test and Production deployed connection details you have to pass ONLY the structure in the CREATE request, without any filters.

         - To apply multiple filters, add the Operator to the payload. Refer to the provided code samples for guidance.

         - The argument values for the *property* filters in the CREATE payload should be:

          - componentId - Must be a valid componentId value. If an invalid value is passed, the report or the GET response will be blank or will have zero records.

          - environmentId - Must be valid environmentId value. If an invalid value is passed, the report or the GET response will be blank or will have zero records.

          - containerId - Must be a valid atomId or moleculeId. If an invalid value is passed, the report or the GET response will be blank or will have zero records.

          - connectorClass - Must be valid connectorClass. Values must be either Standard, Small Business, Trading Partner, or Enterprise.

        :param request_body: The request body., defaults to None
        :type request_body: ConnectionLicensingReport, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ConnectionLicensingDownload, str]
        """

        Validator(ConnectionLicensingReport).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ConnectionLicensingReport",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return ConnectionLicensingDownload._unmap(response)
        if content == "application/xml":
            return ConnectionLicensingDownload._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)
