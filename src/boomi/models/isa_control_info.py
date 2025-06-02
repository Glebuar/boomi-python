
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class AuthorizationInformationQualifier(Enum):
    """An enumeration representing different categories.

    :cvar X12AUTHQUAL00: "X12AUTHQUAL_00"
    :vartype X12AUTHQUAL00: str
    :cvar X12AUTHQUAL01: "X12AUTHQUAL_01"
    :vartype X12AUTHQUAL01: str
    :cvar X12AUTHQUAL02: "X12AUTHQUAL_02"
    :vartype X12AUTHQUAL02: str
    :cvar X12AUTHQUAL03: "X12AUTHQUAL_03"
    :vartype X12AUTHQUAL03: str
    :cvar X12AUTHQUAL04: "X12AUTHQUAL_04"
    :vartype X12AUTHQUAL04: str
    :cvar X12AUTHQUAL05: "X12AUTHQUAL_05"
    :vartype X12AUTHQUAL05: str
    """

    X12AUTHQUAL00 = "X12AUTHQUAL_00"
    X12AUTHQUAL01 = "X12AUTHQUAL_01"
    X12AUTHQUAL02 = "X12AUTHQUAL_02"
    X12AUTHQUAL03 = "X12AUTHQUAL_03"
    X12AUTHQUAL04 = "X12AUTHQUAL_04"
    X12AUTHQUAL05 = "X12AUTHQUAL_05"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                AuthorizationInformationQualifier._member_map_.values(),
            )
        )


class InterchangeIdQualifier(Enum):
    """An enumeration representing different categories.

    :cvar X12IDQUAL01: "X12IDQUAL_01"
    :vartype X12IDQUAL01: str
    :cvar X12IDQUAL02: "X12IDQUAL_02"
    :vartype X12IDQUAL02: str
    :cvar X12IDQUAL03: "X12IDQUAL_03"
    :vartype X12IDQUAL03: str
    :cvar X12IDQUAL04: "X12IDQUAL_04"
    :vartype X12IDQUAL04: str
    :cvar X12IDQUAL07: "X12IDQUAL_07"
    :vartype X12IDQUAL07: str
    :cvar X12IDQUAL08: "X12IDQUAL_08"
    :vartype X12IDQUAL08: str
    :cvar X12IDQUAL09: "X12IDQUAL_09"
    :vartype X12IDQUAL09: str
    :cvar X12IDQUAL10: "X12IDQUAL_10"
    :vartype X12IDQUAL10: str
    :cvar X12IDQUAL11: "X12IDQUAL_11"
    :vartype X12IDQUAL11: str
    :cvar X12IDQUAL12: "X12IDQUAL_12"
    :vartype X12IDQUAL12: str
    :cvar X12IDQUAL13: "X12IDQUAL_13"
    :vartype X12IDQUAL13: str
    :cvar X12IDQUAL14: "X12IDQUAL_14"
    :vartype X12IDQUAL14: str
    :cvar X12IDQUAL15: "X12IDQUAL_15"
    :vartype X12IDQUAL15: str
    :cvar X12IDQUAL16: "X12IDQUAL_16"
    :vartype X12IDQUAL16: str
    :cvar X12IDQUAL17: "X12IDQUAL_17"
    :vartype X12IDQUAL17: str
    :cvar X12IDQUAL18: "X12IDQUAL_18"
    :vartype X12IDQUAL18: str
    :cvar X12IDQUAL19: "X12IDQUAL_19"
    :vartype X12IDQUAL19: str
    :cvar X12IDQUAL20: "X12IDQUAL_20"
    :vartype X12IDQUAL20: str
    :cvar X12IDQUAL21: "X12IDQUAL_21"
    :vartype X12IDQUAL21: str
    :cvar X12IDQUAL22: "X12IDQUAL_22"
    :vartype X12IDQUAL22: str
    :cvar X12IDQUAL23: "X12IDQUAL_23"
    :vartype X12IDQUAL23: str
    :cvar X12IDQUAL24: "X12IDQUAL_24"
    :vartype X12IDQUAL24: str
    :cvar X12IDQUAL25: "X12IDQUAL_25"
    :vartype X12IDQUAL25: str
    :cvar X12IDQUAL26: "X12IDQUAL_26"
    :vartype X12IDQUAL26: str
    :cvar X12IDQUAL27: "X12IDQUAL_27"
    :vartype X12IDQUAL27: str
    :cvar X12IDQUAL28: "X12IDQUAL_28"
    :vartype X12IDQUAL28: str
    :cvar X12IDQUAL29: "X12IDQUAL_29"
    :vartype X12IDQUAL29: str
    :cvar X12IDQUAL30: "X12IDQUAL_30"
    :vartype X12IDQUAL30: str
    :cvar X12IDQUAL31: "X12IDQUAL_31"
    :vartype X12IDQUAL31: str
    :cvar X12IDQUAL32: "X12IDQUAL_32"
    :vartype X12IDQUAL32: str
    :cvar X12IDQUAL33: "X12IDQUAL_33"
    :vartype X12IDQUAL33: str
    :cvar X12IDQUAL34: "X12IDQUAL_34"
    :vartype X12IDQUAL34: str
    :cvar X12IDQUALNR: "X12IDQUAL_NR"
    :vartype X12IDQUALNR: str
    :cvar X12IDQUALZZ: "X12IDQUAL_ZZ"
    :vartype X12IDQUALZZ: str
    """

    X12IDQUAL01 = "X12IDQUAL_01"
    X12IDQUAL02 = "X12IDQUAL_02"
    X12IDQUAL03 = "X12IDQUAL_03"
    X12IDQUAL04 = "X12IDQUAL_04"
    X12IDQUAL07 = "X12IDQUAL_07"
    X12IDQUAL08 = "X12IDQUAL_08"
    X12IDQUAL09 = "X12IDQUAL_09"
    X12IDQUAL10 = "X12IDQUAL_10"
    X12IDQUAL11 = "X12IDQUAL_11"
    X12IDQUAL12 = "X12IDQUAL_12"
    X12IDQUAL13 = "X12IDQUAL_13"
    X12IDQUAL14 = "X12IDQUAL_14"
    X12IDQUAL15 = "X12IDQUAL_15"
    X12IDQUAL16 = "X12IDQUAL_16"
    X12IDQUAL17 = "X12IDQUAL_17"
    X12IDQUAL18 = "X12IDQUAL_18"
    X12IDQUAL19 = "X12IDQUAL_19"
    X12IDQUAL20 = "X12IDQUAL_20"
    X12IDQUAL21 = "X12IDQUAL_21"
    X12IDQUAL22 = "X12IDQUAL_22"
    X12IDQUAL23 = "X12IDQUAL_23"
    X12IDQUAL24 = "X12IDQUAL_24"
    X12IDQUAL25 = "X12IDQUAL_25"
    X12IDQUAL26 = "X12IDQUAL_26"
    X12IDQUAL27 = "X12IDQUAL_27"
    X12IDQUAL28 = "X12IDQUAL_28"
    X12IDQUAL29 = "X12IDQUAL_29"
    X12IDQUAL30 = "X12IDQUAL_30"
    X12IDQUAL31 = "X12IDQUAL_31"
    X12IDQUAL32 = "X12IDQUAL_32"
    X12IDQUAL33 = "X12IDQUAL_33"
    X12IDQUAL34 = "X12IDQUAL_34"
    X12IDQUALNR = "X12IDQUAL_NR"
    X12IDQUALZZ = "X12IDQUAL_ZZ"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, InterchangeIdQualifier._member_map_.values())
        )


class SecurityInformationQualifier(Enum):
    """An enumeration representing different categories.

    :cvar X12SECQUAL00: "X12SECQUAL_00"
    :vartype X12SECQUAL00: str
    :cvar X12SECQUAL01: "X12SECQUAL_01"
    :vartype X12SECQUAL01: str
    """

    X12SECQUAL00 = "X12SECQUAL_00"
    X12SECQUAL01 = "X12SECQUAL_01"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, SecurityInformationQualifier._member_map_.values())
        )


class Testindicator(Enum):
    """An enumeration representing different categories.

    :cvar P: "P"
    :vartype P: str
    :cvar T: "T"
    :vartype T: str
    """

    P = "P"
    T = "T"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, Testindicator._member_map_.values()))


@JsonMap(
    {
        "authorization_information": "authorizationInformation",
        "authorization_information_qualifier": "authorizationInformationQualifier",
        "component_element_separator": "componentElementSeparator",
        "interchange_id": "interchangeId",
        "interchange_id_qualifier": "interchangeIdQualifier",
        "security_information": "securityInformation",
        "security_information_qualifier": "securityInformationQualifier",
        "standard_identification": "standardIdentification",
    }
)
class IsaControlInfo(BaseModel):
    """IsaControlInfo

    :param ackrequested: ackrequested, defaults to None
    :type ackrequested: bool, optional
    :param authorization_information: authorization_information, defaults to None
    :type authorization_information: str, optional
    :param authorization_information_qualifier: authorization_information_qualifier, defaults to None
    :type authorization_information_qualifier: AuthorizationInformationQualifier, optional
    :param component_element_separator: component_element_separator, defaults to None
    :type component_element_separator: str, optional
    :param interchange_id: interchange_id, defaults to None
    :type interchange_id: str, optional
    :param interchange_id_qualifier: interchange_id_qualifier, defaults to None
    :type interchange_id_qualifier: InterchangeIdQualifier, optional
    :param security_information: security_information, defaults to None
    :type security_information: str, optional
    :param security_information_qualifier: security_information_qualifier, defaults to None
    :type security_information_qualifier: SecurityInformationQualifier, optional
    :param standard_identification: standard_identification, defaults to None
    :type standard_identification: str, optional
    :param testindicator: testindicator, defaults to None
    :type testindicator: Testindicator, optional
    :param version: version, defaults to None
    :type version: str, optional
    """

    def __init__(
        self,
        ackrequested: bool = SENTINEL,
        authorization_information: str = SENTINEL,
        authorization_information_qualifier: AuthorizationInformationQualifier = SENTINEL,
        component_element_separator: str = SENTINEL,
        interchange_id: str = SENTINEL,
        interchange_id_qualifier: InterchangeIdQualifier = SENTINEL,
        security_information: str = SENTINEL,
        security_information_qualifier: SecurityInformationQualifier = SENTINEL,
        standard_identification: str = SENTINEL,
        testindicator: Testindicator = SENTINEL,
        version: str = SENTINEL,
        **kwargs
    ):
        """IsaControlInfo

        :param ackrequested: ackrequested, defaults to None
        :type ackrequested: bool, optional
        :param authorization_information: authorization_information, defaults to None
        :type authorization_information: str, optional
        :param authorization_information_qualifier: authorization_information_qualifier, defaults to None
        :type authorization_information_qualifier: AuthorizationInformationQualifier, optional
        :param component_element_separator: component_element_separator, defaults to None
        :type component_element_separator: str, optional
        :param interchange_id: interchange_id, defaults to None
        :type interchange_id: str, optional
        :param interchange_id_qualifier: interchange_id_qualifier, defaults to None
        :type interchange_id_qualifier: InterchangeIdQualifier, optional
        :param security_information: security_information, defaults to None
        :type security_information: str, optional
        :param security_information_qualifier: security_information_qualifier, defaults to None
        :type security_information_qualifier: SecurityInformationQualifier, optional
        :param standard_identification: standard_identification, defaults to None
        :type standard_identification: str, optional
        :param testindicator: testindicator, defaults to None
        :type testindicator: Testindicator, optional
        :param version: version, defaults to None
        :type version: str, optional
        """
        if ackrequested is not SENTINEL:
            self.ackrequested = ackrequested
        if authorization_information is not SENTINEL:
            self.authorization_information = authorization_information
        if authorization_information_qualifier is not SENTINEL:
            self.authorization_information_qualifier = self._enum_matching(
                authorization_information_qualifier,
                AuthorizationInformationQualifier.list(),
                "authorization_information_qualifier",
            )
        if component_element_separator is not SENTINEL:
            self.component_element_separator = component_element_separator
        if interchange_id is not SENTINEL:
            self.interchange_id = interchange_id
        if interchange_id_qualifier is not SENTINEL:
            self.interchange_id_qualifier = self._enum_matching(
                interchange_id_qualifier,
                InterchangeIdQualifier.list(),
                "interchange_id_qualifier",
            )
        if security_information is not SENTINEL:
            self.security_information = security_information
        if security_information_qualifier is not SENTINEL:
            self.security_information_qualifier = self._enum_matching(
                security_information_qualifier,
                SecurityInformationQualifier.list(),
                "security_information_qualifier",
            )
        if standard_identification is not SENTINEL:
            self.standard_identification = standard_identification
        if testindicator is not SENTINEL:
            self.testindicator = self._enum_matching(
                testindicator, Testindicator.list(), "testindicator"
            )
        if version is not SENTINEL:
            self.version = version
        self._kwargs = kwargs
