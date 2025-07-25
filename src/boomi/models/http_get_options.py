
from __future__ import annotations
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .http_path_elements import HttpPathElements
from .http_reflect_headers import HttpReflectHeaders
from .http_request_headers import HttpRequestHeaders
from .http_response_header_mapping import HttpResponseHeaderMapping


class HttpGetOptionsMethodType(Enum):
    """An enumeration representing different categories.

    :cvar GET: "GET"
    :vartype GET: str
    :cvar POST: "POST"
    :vartype POST: str
    :cvar PUT: "PUT"
    :vartype PUT: str
    :cvar DELETE: "DELETE"
    :vartype DELETE: str
    """

    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, HttpGetOptionsMethodType._member_map_.values())
        )


class HttpGetOptionsRequestProfileType(Enum):
    """An enumeration representing different categories.

    :cvar NONE: "NONE"
    :vartype NONE: str
    :cvar XML: "XML"
    :vartype XML: str
    :cvar JSON: "JSON"
    :vartype JSON: str
    """

    NONE = "NONE"
    XML = "XML"
    JSON = "JSON"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                HttpGetOptionsRequestProfileType._member_map_.values(),
            )
        )


class HttpGetOptionsResponseProfileType(Enum):
    """An enumeration representing different categories.

    :cvar NONE: "NONE"
    :vartype NONE: str
    :cvar XML: "XML"
    :vartype XML: str
    :cvar JSON: "JSON"
    :vartype JSON: str
    """

    NONE = "NONE"
    XML = "XML"
    JSON = "JSON"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                HttpGetOptionsResponseProfileType._member_map_.values(),
            )
        )


@JsonMap(
    {
        "data_content_type": "dataContentType",
        "follow_redirects": "followRedirects",
        "method_type": "methodType",
        "path_elements": "pathElements",
        "reflect_headers": "reflectHeaders",
        "request_headers": "requestHeaders",
        "request_profile": "requestProfile",
        "request_profile_type": "requestProfileType",
        "response_header_mapping": "responseHeaderMapping",
        "response_profile": "responseProfile",
        "response_profile_type": "responseProfileType",
        "return_errors": "returnErrors",
        "use_default_options": "useDefaultOptions",
    }
)
class HttpGetOptions(BaseModel):
    """HttpGetOptions

    :param data_content_type: data_content_type, defaults to None
    :type data_content_type: str, optional
    :param follow_redirects: follow_redirects, defaults to None
    :type follow_redirects: bool, optional
    :param method_type: method_type, defaults to None
    :type method_type: HttpGetOptionsMethodType, optional
    :param path_elements: path_elements
    :type path_elements: HttpPathElements
    :param reflect_headers: reflect_headers, defaults to None
    :type reflect_headers: HttpReflectHeaders, optional
    :param request_headers: request_headers
    :type request_headers: HttpRequestHeaders
    :param request_profile: request_profile, defaults to None
    :type request_profile: str, optional
    :param request_profile_type: request_profile_type, defaults to None
    :type request_profile_type: HttpGetOptionsRequestProfileType, optional
    :param response_header_mapping: response_header_mapping
    :type response_header_mapping: HttpResponseHeaderMapping
    :param response_profile: response_profile, defaults to None
    :type response_profile: str, optional
    :param response_profile_type: response_profile_type, defaults to None
    :type response_profile_type: HttpGetOptionsResponseProfileType, optional
    :param return_errors: return_errors, defaults to None
    :type return_errors: bool, optional
    :param use_default_options: use_default_options, defaults to None
    :type use_default_options: bool, optional
    """

    def __init__(
        self,
        path_elements: HttpPathElements,
        request_headers: HttpRequestHeaders,
        response_header_mapping: HttpResponseHeaderMapping,
        data_content_type: str = SENTINEL,
        follow_redirects: bool = SENTINEL,
        method_type: HttpGetOptionsMethodType = SENTINEL,
        reflect_headers: HttpReflectHeaders = SENTINEL,
        request_profile: str = SENTINEL,
        request_profile_type: HttpGetOptionsRequestProfileType = SENTINEL,
        response_profile: str = SENTINEL,
        response_profile_type: HttpGetOptionsResponseProfileType = SENTINEL,
        return_errors: bool = SENTINEL,
        use_default_options: bool = SENTINEL,
        **kwargs,
    ):
        """HttpGetOptions

        :param data_content_type: data_content_type, defaults to None
        :type data_content_type: str, optional
        :param follow_redirects: follow_redirects, defaults to None
        :type follow_redirects: bool, optional
        :param method_type: method_type, defaults to None
        :type method_type: HttpGetOptionsMethodType, optional
        :param path_elements: path_elements
        :type path_elements: HttpPathElements
        :param reflect_headers: reflect_headers, defaults to None
        :type reflect_headers: HttpReflectHeaders, optional
        :param request_headers: request_headers
        :type request_headers: HttpRequestHeaders
        :param request_profile: request_profile, defaults to None
        :type request_profile: str, optional
        :param request_profile_type: request_profile_type, defaults to None
        :type request_profile_type: HttpGetOptionsRequestProfileType, optional
        :param response_header_mapping: response_header_mapping
        :type response_header_mapping: HttpResponseHeaderMapping
        :param response_profile: response_profile, defaults to None
        :type response_profile: str, optional
        :param response_profile_type: response_profile_type, defaults to None
        :type response_profile_type: HttpGetOptionsResponseProfileType, optional
        :param return_errors: return_errors, defaults to None
        :type return_errors: bool, optional
        :param use_default_options: use_default_options, defaults to None
        :type use_default_options: bool, optional
        """
        if data_content_type is not SENTINEL:
            self.data_content_type = data_content_type
        if follow_redirects is not SENTINEL:
            self.follow_redirects = follow_redirects
        if method_type is not SENTINEL:
            self.method_type = self._enum_matching(
                method_type, HttpGetOptionsMethodType.list(), "method_type"
            )
        self.path_elements = self._define_object(path_elements, HttpPathElements)
        if reflect_headers is not SENTINEL:
            self.reflect_headers = self._define_object(
                reflect_headers, HttpReflectHeaders
            )
        self.request_headers = self._define_object(request_headers, HttpRequestHeaders)
        if request_profile is not SENTINEL:
            self.request_profile = request_profile
        if request_profile_type is not SENTINEL:
            self.request_profile_type = self._enum_matching(
                request_profile_type,
                HttpGetOptionsRequestProfileType.list(),
                "request_profile_type",
            )
        self.response_header_mapping = self._define_object(
            response_header_mapping, HttpResponseHeaderMapping
        )
        if response_profile is not SENTINEL:
            self.response_profile = response_profile
        if response_profile_type is not SENTINEL:
            self.response_profile_type = self._enum_matching(
                response_profile_type,
                HttpGetOptionsResponseProfileType.list(),
                "response_profile_type",
            )
        if return_errors is not SENTINEL:
            self.return_errors = return_errors
        if use_default_options is not SENTINEL:
            self.use_default_options = use_default_options
        self._kwargs = kwargs
