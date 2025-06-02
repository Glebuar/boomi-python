
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..net.transport.utils import parse_xml_to_dict
from ..models import (
    TradingPartnerComponent,
    TradingPartnerComponentBulkRequest,
    TradingPartnerComponentBulkResponse,
    TradingPartnerComponentQueryConfig,
    TradingPartnerComponentQueryResponse,
)


class TradingPartnerComponentService(BaseService):

    @cast_models
    def create_trading_partner_component(
        self, request_body: TradingPartnerComponent = None
    ) -> Union[TradingPartnerComponent, str]:
        """- This operation creates a Trading Partner Component object with a specified component name.
         - The request body requires the standard, classification, and componentName fields. If you omit the folderName field, you must use the folderId field — and vice versa. If you omit the componentID field and the IDs of any certificates you want to create, their values are assigned when you create the components. If you leave off the folderID field when creating a component, it assigns a value.
         - Includes the organizationId field only if the trading partner is to reference an Organization component, in which case the field value is the ID of the Organization component. A request specifying the organizationId field populates the ContactInformation fields with the data from the referenced Organization component.

        :param request_body: The request body., defaults to None
        :type request_body: TradingPartnerComponent, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[TradingPartnerComponent, str]
        """

        Validator(TradingPartnerComponent).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/TradingPartnerComponent",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return TradingPartnerComponent._unmap(response)
        if content == "application/xml":
            return TradingPartnerComponent._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def get_trading_partner_component(
        self, id_: str
    ) -> Union[TradingPartnerComponent, str]:
        """The ordinary GET operation returns a single Trading Partner Component object based on the supplied ID. A GET operation specifying the ID of a deleted Trading Partner component retrieves the component. In the component, the deleted field’s value is true.

        :param id_: id_
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[TradingPartnerComponent, str]
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/TradingPartnerComponent/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return TradingPartnerComponent._unmap(response)
        if content == "application/xml":
            return TradingPartnerComponent._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def update_trading_partner_component(
        self, id_: str, request_body: TradingPartnerComponent = None
    ) -> Union[TradingPartnerComponent, str]:
        """This operation overwrites the Trading Partner Component object with the specified component ID except as described:
         - If the fields are empty, an UPDATE operation specifying the organizationId field populates the ContactInformation fields with the data from the referenced Organization component. However, if those fields have values, they are not overwritten.
         An UPDATE operation specifying the ID of a deleted Trading Partner component restores the component to a non-deleted state, assuming the request is otherwise valid.

        :param request_body: The request body., defaults to None
        :type request_body: TradingPartnerComponent, optional
        :param id_: id_
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[TradingPartnerComponent, str]
        """

        Validator(TradingPartnerComponent).is_optional().validate(request_body)
        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/TradingPartnerComponent/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return TradingPartnerComponent._unmap(response)
        if content == "application/xml":
            return TradingPartnerComponent._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def delete_trading_partner_component(self, id_: str) -> None:
        """The DELETE operation deletes the Trading Partner Component object with a specific component ID.
         A DELETE operation specifying the ID of a deleted Trading Partner component returns a false response.

        :param id_: id_
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/TradingPartnerComponent/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)

    @cast_models
    def bulk_trading_partner_component(
        self, request_body: TradingPartnerComponentBulkRequest = None
    ) -> Union[TradingPartnerComponentBulkResponse, str]:
        """The bulk GET operation returns multiple Trading Partner Component objects based on the supplied IDs, to a maximum of 100.

        :param request_body: The request body., defaults to None
        :type request_body: TradingPartnerComponentBulkRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[TradingPartnerComponentBulkResponse, str]
        """

        Validator(TradingPartnerComponentBulkRequest).is_optional().validate(
            request_body
        )

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/TradingPartnerComponent/bulk",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return TradingPartnerComponentBulkResponse._unmap(response)
        if content == "application/xml":
            return TradingPartnerComponentBulkResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_trading_partner_component(
        self, request_body: TradingPartnerComponentQueryConfig = None
    ) -> Union[TradingPartnerComponentQueryResponse, str]:
        """The QUERY operation returns each Trading Partner component that meets the specified filtering criteria.

         - The name field in a QUERY filter represents the object’s componentName field.
         - Only the LIKE operator is allowed with a name filter. Likewise, you can only use the EQUALS operator with a classification, standard, identifier filter, or a communication method filter (as2, disk, ftp, http, mllp, sftp). Filtering on a communication method field requests Trading Partner components by defining the communication method.
         - If the QUERY request includes multiple filters, you can connect the filters with a logical AND operator. The QUERY request does not support the logical OR operator.
         - The QUERY results omit the folderName field.

         For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body., defaults to None
        :type request_body: TradingPartnerComponentQueryConfig, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[TradingPartnerComponentQueryResponse, str]
        """

        Validator(TradingPartnerComponentQueryConfig).is_optional().validate(
            request_body
        )

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/TradingPartnerComponent/query",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return TradingPartnerComponentQueryResponse._unmap(response)
        if content == "application/xml":
            return TradingPartnerComponentQueryResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_more_trading_partner_component(
        self, request_body: str
    ) -> Union[TradingPartnerComponentQueryResponse, str]:
        """To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body.
        :type request_body: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[TradingPartnerComponentQueryResponse, str]
        """

        Validator(str).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/TradingPartnerComponent/queryMore",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body, "text/plain")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return TradingPartnerComponentQueryResponse._unmap(response)
        if content == "application/xml":
            return TradingPartnerComponentQueryResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)
