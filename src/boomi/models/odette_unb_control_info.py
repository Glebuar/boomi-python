
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class OdetteUnbControlInfoInterchangeIdQual(Enum):
    """An enumeration representing different categories.

    :cvar ODETTEIDQUALNA: "ODETTEIDQUAL_NA"
    :vartype ODETTEIDQUALNA: str
    :cvar ODETTEIDQUAL1: "ODETTEIDQUAL_1"
    :vartype ODETTEIDQUAL1: str
    :cvar ODETTEIDQUAL4: "ODETTEIDQUAL_4"
    :vartype ODETTEIDQUAL4: str
    :cvar ODETTEIDQUAL5: "ODETTEIDQUAL_5"
    :vartype ODETTEIDQUAL5: str
    :cvar ODETTEIDQUAL8: "ODETTEIDQUAL_8"
    :vartype ODETTEIDQUAL8: str
    :cvar ODETTEIDQUAL9: "ODETTEIDQUAL_9"
    :vartype ODETTEIDQUAL9: str
    :cvar ODETTEIDQUAL12: "ODETTEIDQUAL_12"
    :vartype ODETTEIDQUAL12: str
    :cvar ODETTEIDQUAL14: "ODETTEIDQUAL_14"
    :vartype ODETTEIDQUAL14: str
    :cvar ODETTEIDQUAL18: "ODETTEIDQUAL_18"
    :vartype ODETTEIDQUAL18: str
    :cvar ODETTEIDQUAL22: "ODETTEIDQUAL_22"
    :vartype ODETTEIDQUAL22: str
    :cvar ODETTEIDQUAL30: "ODETTEIDQUAL_30"
    :vartype ODETTEIDQUAL30: str
    :cvar ODETTEIDQUAL31: "ODETTEIDQUAL_31"
    :vartype ODETTEIDQUAL31: str
    :cvar ODETTEIDQUAL33: "ODETTEIDQUAL_33"
    :vartype ODETTEIDQUAL33: str
    :cvar ODETTEIDQUAL34: "ODETTEIDQUAL_34"
    :vartype ODETTEIDQUAL34: str
    :cvar ODETTEIDQUAL51: "ODETTEIDQUAL_51"
    :vartype ODETTEIDQUAL51: str
    :cvar ODETTEIDQUAL52: "ODETTEIDQUAL_52"
    :vartype ODETTEIDQUAL52: str
    :cvar ODETTEIDQUAL53: "ODETTEIDQUAL_53"
    :vartype ODETTEIDQUAL53: str
    :cvar ODETTEIDQUAL54: "ODETTEIDQUAL_54"
    :vartype ODETTEIDQUAL54: str
    :cvar ODETTEIDQUAL55: "ODETTEIDQUAL_55"
    :vartype ODETTEIDQUAL55: str
    :cvar ODETTEIDQUAL57: "ODETTEIDQUAL_57"
    :vartype ODETTEIDQUAL57: str
    :cvar ODETTEIDQUAL58: "ODETTEIDQUAL_58"
    :vartype ODETTEIDQUAL58: str
    :cvar ODETTEIDQUAL59: "ODETTEIDQUAL_59"
    :vartype ODETTEIDQUAL59: str
    :cvar ODETTEIDQUAL61: "ODETTEIDQUAL_61"
    :vartype ODETTEIDQUAL61: str
    :cvar ODETTEIDQUAL63: "ODETTEIDQUAL_63"
    :vartype ODETTEIDQUAL63: str
    :cvar ODETTEIDQUAL65: "ODETTEIDQUAL_65"
    :vartype ODETTEIDQUAL65: str
    :cvar ODETTEIDQUAL80: "ODETTEIDQUAL_80"
    :vartype ODETTEIDQUAL80: str
    :cvar ODETTEIDQUAL82: "ODETTEIDQUAL_82"
    :vartype ODETTEIDQUAL82: str
    :cvar ODETTEIDQUAL84: "ODETTEIDQUAL_84"
    :vartype ODETTEIDQUAL84: str
    :cvar ODETTEIDQUAL85: "ODETTEIDQUAL_85"
    :vartype ODETTEIDQUAL85: str
    :cvar ODETTEIDQUAL86: "ODETTEIDQUAL_86"
    :vartype ODETTEIDQUAL86: str
    :cvar ODETTEIDQUAL87: "ODETTEIDQUAL_87"
    :vartype ODETTEIDQUAL87: str
    :cvar ODETTEIDQUAL89: "ODETTEIDQUAL_89"
    :vartype ODETTEIDQUAL89: str
    :cvar ODETTEIDQUAL90: "ODETTEIDQUAL_90"
    :vartype ODETTEIDQUAL90: str
    :cvar ODETTEIDQUAL91: "ODETTEIDQUAL_91"
    :vartype ODETTEIDQUAL91: str
    :cvar ODETTEIDQUAL92: "ODETTEIDQUAL_92"
    :vartype ODETTEIDQUAL92: str
    :cvar ODETTEIDQUAL103: "ODETTEIDQUAL_103"
    :vartype ODETTEIDQUAL103: str
    :cvar ODETTEIDQUAL128: "ODETTEIDQUAL_128"
    :vartype ODETTEIDQUAL128: str
    :cvar ODETTEIDQUAL129: "ODETTEIDQUAL_129"
    :vartype ODETTEIDQUAL129: str
    :cvar ODETTEIDQUAL144: "ODETTEIDQUAL_144"
    :vartype ODETTEIDQUAL144: str
    :cvar ODETTEIDQUAL145: "ODETTEIDQUAL_145"
    :vartype ODETTEIDQUAL145: str
    :cvar ODETTEIDQUAL146: "ODETTEIDQUAL_146"
    :vartype ODETTEIDQUAL146: str
    :cvar ODETTEIDQUAL147: "ODETTEIDQUAL_147"
    :vartype ODETTEIDQUAL147: str
    :cvar ODETTEIDQUAL148: "ODETTEIDQUAL_148"
    :vartype ODETTEIDQUAL148: str
    :cvar ODETTEIDQUALZ01: "ODETTEIDQUAL_Z01"
    :vartype ODETTEIDQUALZ01: str
    :cvar ODETTEIDQUALZZZ: "ODETTEIDQUAL_ZZZ"
    :vartype ODETTEIDQUALZZZ: str
    :cvar ODETTEIDQUALZZ: "ODETTEIDQUAL_ZZ"
    :vartype ODETTEIDQUALZZ: str
    """

    ODETTEIDQUALNA = "ODETTEIDQUAL_NA"
    ODETTEIDQUAL1 = "ODETTEIDQUAL_1"
    ODETTEIDQUAL4 = "ODETTEIDQUAL_4"
    ODETTEIDQUAL5 = "ODETTEIDQUAL_5"
    ODETTEIDQUAL8 = "ODETTEIDQUAL_8"
    ODETTEIDQUAL9 = "ODETTEIDQUAL_9"
    ODETTEIDQUAL12 = "ODETTEIDQUAL_12"
    ODETTEIDQUAL14 = "ODETTEIDQUAL_14"
    ODETTEIDQUAL18 = "ODETTEIDQUAL_18"
    ODETTEIDQUAL22 = "ODETTEIDQUAL_22"
    ODETTEIDQUAL30 = "ODETTEIDQUAL_30"
    ODETTEIDQUAL31 = "ODETTEIDQUAL_31"
    ODETTEIDQUAL33 = "ODETTEIDQUAL_33"
    ODETTEIDQUAL34 = "ODETTEIDQUAL_34"
    ODETTEIDQUAL51 = "ODETTEIDQUAL_51"
    ODETTEIDQUAL52 = "ODETTEIDQUAL_52"
    ODETTEIDQUAL53 = "ODETTEIDQUAL_53"
    ODETTEIDQUAL54 = "ODETTEIDQUAL_54"
    ODETTEIDQUAL55 = "ODETTEIDQUAL_55"
    ODETTEIDQUAL57 = "ODETTEIDQUAL_57"
    ODETTEIDQUAL58 = "ODETTEIDQUAL_58"
    ODETTEIDQUAL59 = "ODETTEIDQUAL_59"
    ODETTEIDQUAL61 = "ODETTEIDQUAL_61"
    ODETTEIDQUAL63 = "ODETTEIDQUAL_63"
    ODETTEIDQUAL65 = "ODETTEIDQUAL_65"
    ODETTEIDQUAL80 = "ODETTEIDQUAL_80"
    ODETTEIDQUAL82 = "ODETTEIDQUAL_82"
    ODETTEIDQUAL84 = "ODETTEIDQUAL_84"
    ODETTEIDQUAL85 = "ODETTEIDQUAL_85"
    ODETTEIDQUAL86 = "ODETTEIDQUAL_86"
    ODETTEIDQUAL87 = "ODETTEIDQUAL_87"
    ODETTEIDQUAL89 = "ODETTEIDQUAL_89"
    ODETTEIDQUAL90 = "ODETTEIDQUAL_90"
    ODETTEIDQUAL91 = "ODETTEIDQUAL_91"
    ODETTEIDQUAL92 = "ODETTEIDQUAL_92"
    ODETTEIDQUAL103 = "ODETTEIDQUAL_103"
    ODETTEIDQUAL128 = "ODETTEIDQUAL_128"
    ODETTEIDQUAL129 = "ODETTEIDQUAL_129"
    ODETTEIDQUAL144 = "ODETTEIDQUAL_144"
    ODETTEIDQUAL145 = "ODETTEIDQUAL_145"
    ODETTEIDQUAL146 = "ODETTEIDQUAL_146"
    ODETTEIDQUAL147 = "ODETTEIDQUAL_147"
    ODETTEIDQUAL148 = "ODETTEIDQUAL_148"
    ODETTEIDQUALZ01 = "ODETTEIDQUAL_Z01"
    ODETTEIDQUALZZZ = "ODETTEIDQUAL_ZZZ"
    ODETTEIDQUALZZ = "ODETTEIDQUAL_ZZ"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                OdetteUnbControlInfoInterchangeIdQual._member_map_.values(),
            )
        )


class OdetteUnbControlInfoPriority(Enum):
    """An enumeration representing different categories.

    :cvar NA: "NA"
    :vartype NA: str
    :cvar A: "A"
    :vartype A: str
    """

    NA = "NA"
    A = "A"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, OdetteUnbControlInfoPriority._member_map_.values())
        )


class OdetteUnbControlInfoReferencePasswordQualifier(Enum):
    """An enumeration representing different categories.

    :cvar NA: "NA"
    :vartype NA: str
    :cvar AA: "AA"
    :vartype AA: str
    :cvar BB: "BB"
    :vartype BB: str
    """

    NA = "NA"
    AA = "AA"
    BB = "BB"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                OdetteUnbControlInfoReferencePasswordQualifier._member_map_.values(),
            )
        )


class OdetteUnbControlInfoSyntaxId(Enum):
    """An enumeration representing different categories.

    :cvar UNOA: "UNOA"
    :vartype UNOA: str
    :cvar UNOB: "UNOB"
    :vartype UNOB: str
    :cvar UNOC: "UNOC"
    :vartype UNOC: str
    :cvar UNOD: "UNOD"
    :vartype UNOD: str
    :cvar UNOE: "UNOE"
    :vartype UNOE: str
    :cvar UNOF: "UNOF"
    :vartype UNOF: str
    """

    UNOA = "UNOA"
    UNOB = "UNOB"
    UNOC = "UNOC"
    UNOD = "UNOD"
    UNOE = "UNOE"
    UNOF = "UNOF"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, OdetteUnbControlInfoSyntaxId._member_map_.values())
        )


class OdetteUnbControlInfoSyntaxVersion(Enum):
    """An enumeration representing different categories.

    :cvar ODETTESYNTAXVERSION1: "ODETTESYNTAXVERSION_1"
    :vartype ODETTESYNTAXVERSION1: str
    :cvar ODETTESYNTAXVERSION2: "ODETTESYNTAXVERSION_2"
    :vartype ODETTESYNTAXVERSION2: str
    :cvar ODETTESYNTAXVERSION3: "ODETTESYNTAXVERSION_3"
    :vartype ODETTESYNTAXVERSION3: str
    """

    ODETTESYNTAXVERSION1 = "ODETTESYNTAXVERSION_1"
    ODETTESYNTAXVERSION2 = "ODETTESYNTAXVERSION_2"
    ODETTESYNTAXVERSION3 = "ODETTESYNTAXVERSION_3"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                OdetteUnbControlInfoSyntaxVersion._member_map_.values(),
            )
        )


class OdetteUnbControlInfoTestIndicator(Enum):
    """An enumeration representing different categories.

    :cvar ODETTETESTNA: "ODETTETEST_NA"
    :vartype ODETTETESTNA: str
    :cvar ODETTETEST1: "ODETTETEST_1"
    :vartype ODETTETEST1: str
    """

    ODETTETESTNA = "ODETTETEST_NA"
    ODETTETEST1 = "ODETTETEST_1"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                OdetteUnbControlInfoTestIndicator._member_map_.values(),
            )
        )


@JsonMap(
    {
        "ack_request": "ackRequest",
        "app_reference": "appReference",
        "comm_agreement": "commAgreement",
        "interchange_address": "interchangeAddress",
        "interchange_id": "interchangeId",
        "interchange_id_qual": "interchangeIdQual",
        "interchange_sub_address": "interchangeSubAddress",
        "reference_password": "referencePassword",
        "reference_password_qualifier": "referencePasswordQualifier",
        "syntax_id": "syntaxId",
        "syntax_version": "syntaxVersion",
        "test_indicator": "testIndicator",
    }
)
class OdetteUnbControlInfo(BaseModel):
    """OdetteUnbControlInfo

    :param ack_request: ack_request, defaults to None
    :type ack_request: bool, optional
    :param app_reference: app_reference, defaults to None
    :type app_reference: str, optional
    :param comm_agreement: comm_agreement, defaults to None
    :type comm_agreement: str, optional
    :param interchange_address: interchange_address, defaults to None
    :type interchange_address: str, optional
    :param interchange_id: interchange_id, defaults to None
    :type interchange_id: str, optional
    :param interchange_id_qual: interchange_id_qual, defaults to None
    :type interchange_id_qual: OdetteUnbControlInfoInterchangeIdQual, optional
    :param interchange_sub_address: interchange_sub_address, defaults to None
    :type interchange_sub_address: str, optional
    :param priority: priority, defaults to None
    :type priority: OdetteUnbControlInfoPriority, optional
    :param reference_password: reference_password, defaults to None
    :type reference_password: str, optional
    :param reference_password_qualifier: reference_password_qualifier, defaults to None
    :type reference_password_qualifier: OdetteUnbControlInfoReferencePasswordQualifier, optional
    :param syntax_id: syntax_id, defaults to None
    :type syntax_id: OdetteUnbControlInfoSyntaxId, optional
    :param syntax_version: syntax_version, defaults to None
    :type syntax_version: OdetteUnbControlInfoSyntaxVersion, optional
    :param test_indicator: test_indicator, defaults to None
    :type test_indicator: OdetteUnbControlInfoTestIndicator, optional
    """

    def __init__(
        self,
        ack_request: bool = SENTINEL,
        app_reference: str = SENTINEL,
        comm_agreement: str = SENTINEL,
        interchange_address: str = SENTINEL,
        interchange_id: str = SENTINEL,
        interchange_id_qual: OdetteUnbControlInfoInterchangeIdQual = SENTINEL,
        interchange_sub_address: str = SENTINEL,
        priority: OdetteUnbControlInfoPriority = SENTINEL,
        reference_password: str = SENTINEL,
        reference_password_qualifier: OdetteUnbControlInfoReferencePasswordQualifier = SENTINEL,
        syntax_id: OdetteUnbControlInfoSyntaxId = SENTINEL,
        syntax_version: OdetteUnbControlInfoSyntaxVersion = SENTINEL,
        test_indicator: OdetteUnbControlInfoTestIndicator = SENTINEL,
        **kwargs
    ):
        """OdetteUnbControlInfo

        :param ack_request: ack_request, defaults to None
        :type ack_request: bool, optional
        :param app_reference: app_reference, defaults to None
        :type app_reference: str, optional
        :param comm_agreement: comm_agreement, defaults to None
        :type comm_agreement: str, optional
        :param interchange_address: interchange_address, defaults to None
        :type interchange_address: str, optional
        :param interchange_id: interchange_id, defaults to None
        :type interchange_id: str, optional
        :param interchange_id_qual: interchange_id_qual, defaults to None
        :type interchange_id_qual: OdetteUnbControlInfoInterchangeIdQual, optional
        :param interchange_sub_address: interchange_sub_address, defaults to None
        :type interchange_sub_address: str, optional
        :param priority: priority, defaults to None
        :type priority: OdetteUnbControlInfoPriority, optional
        :param reference_password: reference_password, defaults to None
        :type reference_password: str, optional
        :param reference_password_qualifier: reference_password_qualifier, defaults to None
        :type reference_password_qualifier: OdetteUnbControlInfoReferencePasswordQualifier, optional
        :param syntax_id: syntax_id, defaults to None
        :type syntax_id: OdetteUnbControlInfoSyntaxId, optional
        :param syntax_version: syntax_version, defaults to None
        :type syntax_version: OdetteUnbControlInfoSyntaxVersion, optional
        :param test_indicator: test_indicator, defaults to None
        :type test_indicator: OdetteUnbControlInfoTestIndicator, optional
        """
        if ack_request is not SENTINEL:
            self.ack_request = ack_request
        if app_reference is not SENTINEL:
            self.app_reference = app_reference
        if comm_agreement is not SENTINEL:
            self.comm_agreement = comm_agreement
        if interchange_address is not SENTINEL:
            self.interchange_address = interchange_address
        if interchange_id is not SENTINEL:
            self.interchange_id = interchange_id
        if interchange_id_qual is not SENTINEL:
            self.interchange_id_qual = self._enum_matching(
                interchange_id_qual,
                OdetteUnbControlInfoInterchangeIdQual.list(),
                "interchange_id_qual",
            )
        if interchange_sub_address is not SENTINEL:
            self.interchange_sub_address = interchange_sub_address
        if priority is not SENTINEL:
            self.priority = self._enum_matching(
                priority, OdetteUnbControlInfoPriority.list(), "priority"
            )
        if reference_password is not SENTINEL:
            self.reference_password = reference_password
        if reference_password_qualifier is not SENTINEL:
            self.reference_password_qualifier = self._enum_matching(
                reference_password_qualifier,
                OdetteUnbControlInfoReferencePasswordQualifier.list(),
                "reference_password_qualifier",
            )
        if syntax_id is not SENTINEL:
            self.syntax_id = self._enum_matching(
                syntax_id, OdetteUnbControlInfoSyntaxId.list(), "syntax_id"
            )
        if syntax_version is not SENTINEL:
            self.syntax_version = self._enum_matching(
                syntax_version,
                OdetteUnbControlInfoSyntaxVersion.list(),
                "syntax_version",
            )
        if test_indicator is not SENTINEL:
            self.test_indicator = self._enum_matching(
                test_indicator,
                OdetteUnbControlInfoTestIndicator.list(),
                "test_indicator",
            )
        self._kwargs = kwargs
