
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class UnbControlInfoInterchangeIdQual(Enum):
    """An enumeration representing different categories.

    :cvar EDIFACTIDQUALNA: "EDIFACTIDQUAL_NA"
    :vartype EDIFACTIDQUALNA: str
    :cvar EDIFACTIDQUAL1: "EDIFACTIDQUAL_1"
    :vartype EDIFACTIDQUAL1: str
    :cvar EDIFACTIDQUAL4: "EDIFACTIDQUAL_4"
    :vartype EDIFACTIDQUAL4: str
    :cvar EDIFACTIDQUAL5: "EDIFACTIDQUAL_5"
    :vartype EDIFACTIDQUAL5: str
    :cvar EDIFACTIDQUAL8: "EDIFACTIDQUAL_8"
    :vartype EDIFACTIDQUAL8: str
    :cvar EDIFACTIDQUAL9: "EDIFACTIDQUAL_9"
    :vartype EDIFACTIDQUAL9: str
    :cvar EDIFACTIDQUAL12: "EDIFACTIDQUAL_12"
    :vartype EDIFACTIDQUAL12: str
    :cvar EDIFACTIDQUAL14: "EDIFACTIDQUAL_14"
    :vartype EDIFACTIDQUAL14: str
    :cvar EDIFACTIDQUAL18: "EDIFACTIDQUAL_18"
    :vartype EDIFACTIDQUAL18: str
    :cvar EDIFACTIDQUAL22: "EDIFACTIDQUAL_22"
    :vartype EDIFACTIDQUAL22: str
    :cvar EDIFACTIDQUAL30: "EDIFACTIDQUAL_30"
    :vartype EDIFACTIDQUAL30: str
    :cvar EDIFACTIDQUAL31: "EDIFACTIDQUAL_31"
    :vartype EDIFACTIDQUAL31: str
    :cvar EDIFACTIDQUAL33: "EDIFACTIDQUAL_33"
    :vartype EDIFACTIDQUAL33: str
    :cvar EDIFACTIDQUAL34: "EDIFACTIDQUAL_34"
    :vartype EDIFACTIDQUAL34: str
    :cvar EDIFACTIDQUAL51: "EDIFACTIDQUAL_51"
    :vartype EDIFACTIDQUAL51: str
    :cvar EDIFACTIDQUAL52: "EDIFACTIDQUAL_52"
    :vartype EDIFACTIDQUAL52: str
    :cvar EDIFACTIDQUAL53: "EDIFACTIDQUAL_53"
    :vartype EDIFACTIDQUAL53: str
    :cvar EDIFACTIDQUAL54: "EDIFACTIDQUAL_54"
    :vartype EDIFACTIDQUAL54: str
    :cvar EDIFACTIDQUAL55: "EDIFACTIDQUAL_55"
    :vartype EDIFACTIDQUAL55: str
    :cvar EDIFACTIDQUAL57: "EDIFACTIDQUAL_57"
    :vartype EDIFACTIDQUAL57: str
    :cvar EDIFACTIDQUAL58: "EDIFACTIDQUAL_58"
    :vartype EDIFACTIDQUAL58: str
    :cvar EDIFACTIDQUAL59: "EDIFACTIDQUAL_59"
    :vartype EDIFACTIDQUAL59: str
    :cvar EDIFACTIDQUAL61: "EDIFACTIDQUAL_61"
    :vartype EDIFACTIDQUAL61: str
    :cvar EDIFACTIDQUAL63: "EDIFACTIDQUAL_63"
    :vartype EDIFACTIDQUAL63: str
    :cvar EDIFACTIDQUAL65: "EDIFACTIDQUAL_65"
    :vartype EDIFACTIDQUAL65: str
    :cvar EDIFACTIDQUAL80: "EDIFACTIDQUAL_80"
    :vartype EDIFACTIDQUAL80: str
    :cvar EDIFACTIDQUAL82: "EDIFACTIDQUAL_82"
    :vartype EDIFACTIDQUAL82: str
    :cvar EDIFACTIDQUAL84: "EDIFACTIDQUAL_84"
    :vartype EDIFACTIDQUAL84: str
    :cvar EDIFACTIDQUAL85: "EDIFACTIDQUAL_85"
    :vartype EDIFACTIDQUAL85: str
    :cvar EDIFACTIDQUAL86: "EDIFACTIDQUAL_86"
    :vartype EDIFACTIDQUAL86: str
    :cvar EDIFACTIDQUAL87: "EDIFACTIDQUAL_87"
    :vartype EDIFACTIDQUAL87: str
    :cvar EDIFACTIDQUAL89: "EDIFACTIDQUAL_89"
    :vartype EDIFACTIDQUAL89: str
    :cvar EDIFACTIDQUAL90: "EDIFACTIDQUAL_90"
    :vartype EDIFACTIDQUAL90: str
    :cvar EDIFACTIDQUAL91: "EDIFACTIDQUAL_91"
    :vartype EDIFACTIDQUAL91: str
    :cvar EDIFACTIDQUAL92: "EDIFACTIDQUAL_92"
    :vartype EDIFACTIDQUAL92: str
    :cvar EDIFACTIDQUAL103: "EDIFACTIDQUAL_103"
    :vartype EDIFACTIDQUAL103: str
    :cvar EDIFACTIDQUAL128: "EDIFACTIDQUAL_128"
    :vartype EDIFACTIDQUAL128: str
    :cvar EDIFACTIDQUAL129: "EDIFACTIDQUAL_129"
    :vartype EDIFACTIDQUAL129: str
    :cvar EDIFACTIDQUAL144: "EDIFACTIDQUAL_144"
    :vartype EDIFACTIDQUAL144: str
    :cvar EDIFACTIDQUAL145: "EDIFACTIDQUAL_145"
    :vartype EDIFACTIDQUAL145: str
    :cvar EDIFACTIDQUAL146: "EDIFACTIDQUAL_146"
    :vartype EDIFACTIDQUAL146: str
    :cvar EDIFACTIDQUAL147: "EDIFACTIDQUAL_147"
    :vartype EDIFACTIDQUAL147: str
    :cvar EDIFACTIDQUAL148: "EDIFACTIDQUAL_148"
    :vartype EDIFACTIDQUAL148: str
    :cvar EDIFACTIDQUALZ01: "EDIFACTIDQUAL_Z01"
    :vartype EDIFACTIDQUALZ01: str
    :cvar EDIFACTIDQUALZZZ: "EDIFACTIDQUAL_ZZZ"
    :vartype EDIFACTIDQUALZZZ: str
    :cvar EDIFACTIDQUALZZ: "EDIFACTIDQUAL_ZZ"
    :vartype EDIFACTIDQUALZZ: str
    """

    EDIFACTIDQUALNA = "EDIFACTIDQUAL_NA"
    EDIFACTIDQUAL1 = "EDIFACTIDQUAL_1"
    EDIFACTIDQUAL4 = "EDIFACTIDQUAL_4"
    EDIFACTIDQUAL5 = "EDIFACTIDQUAL_5"
    EDIFACTIDQUAL8 = "EDIFACTIDQUAL_8"
    EDIFACTIDQUAL9 = "EDIFACTIDQUAL_9"
    EDIFACTIDQUAL12 = "EDIFACTIDQUAL_12"
    EDIFACTIDQUAL14 = "EDIFACTIDQUAL_14"
    EDIFACTIDQUAL18 = "EDIFACTIDQUAL_18"
    EDIFACTIDQUAL22 = "EDIFACTIDQUAL_22"
    EDIFACTIDQUAL30 = "EDIFACTIDQUAL_30"
    EDIFACTIDQUAL31 = "EDIFACTIDQUAL_31"
    EDIFACTIDQUAL33 = "EDIFACTIDQUAL_33"
    EDIFACTIDQUAL34 = "EDIFACTIDQUAL_34"
    EDIFACTIDQUAL51 = "EDIFACTIDQUAL_51"
    EDIFACTIDQUAL52 = "EDIFACTIDQUAL_52"
    EDIFACTIDQUAL53 = "EDIFACTIDQUAL_53"
    EDIFACTIDQUAL54 = "EDIFACTIDQUAL_54"
    EDIFACTIDQUAL55 = "EDIFACTIDQUAL_55"
    EDIFACTIDQUAL57 = "EDIFACTIDQUAL_57"
    EDIFACTIDQUAL58 = "EDIFACTIDQUAL_58"
    EDIFACTIDQUAL59 = "EDIFACTIDQUAL_59"
    EDIFACTIDQUAL61 = "EDIFACTIDQUAL_61"
    EDIFACTIDQUAL63 = "EDIFACTIDQUAL_63"
    EDIFACTIDQUAL65 = "EDIFACTIDQUAL_65"
    EDIFACTIDQUAL80 = "EDIFACTIDQUAL_80"
    EDIFACTIDQUAL82 = "EDIFACTIDQUAL_82"
    EDIFACTIDQUAL84 = "EDIFACTIDQUAL_84"
    EDIFACTIDQUAL85 = "EDIFACTIDQUAL_85"
    EDIFACTIDQUAL86 = "EDIFACTIDQUAL_86"
    EDIFACTIDQUAL87 = "EDIFACTIDQUAL_87"
    EDIFACTIDQUAL89 = "EDIFACTIDQUAL_89"
    EDIFACTIDQUAL90 = "EDIFACTIDQUAL_90"
    EDIFACTIDQUAL91 = "EDIFACTIDQUAL_91"
    EDIFACTIDQUAL92 = "EDIFACTIDQUAL_92"
    EDIFACTIDQUAL103 = "EDIFACTIDQUAL_103"
    EDIFACTIDQUAL128 = "EDIFACTIDQUAL_128"
    EDIFACTIDQUAL129 = "EDIFACTIDQUAL_129"
    EDIFACTIDQUAL144 = "EDIFACTIDQUAL_144"
    EDIFACTIDQUAL145 = "EDIFACTIDQUAL_145"
    EDIFACTIDQUAL146 = "EDIFACTIDQUAL_146"
    EDIFACTIDQUAL147 = "EDIFACTIDQUAL_147"
    EDIFACTIDQUAL148 = "EDIFACTIDQUAL_148"
    EDIFACTIDQUALZ01 = "EDIFACTIDQUAL_Z01"
    EDIFACTIDQUALZZZ = "EDIFACTIDQUAL_ZZZ"
    EDIFACTIDQUALZZ = "EDIFACTIDQUAL_ZZ"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value, UnbControlInfoInterchangeIdQual._member_map_.values()
            )
        )


class UnbControlInfoPriority(Enum):
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
            map(lambda x: x.value, UnbControlInfoPriority._member_map_.values())
        )


class UnbControlInfoReferencePasswordQualifier(Enum):
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
                UnbControlInfoReferencePasswordQualifier._member_map_.values(),
            )
        )


class UnbControlInfoSyntaxId(Enum):
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
            map(lambda x: x.value, UnbControlInfoSyntaxId._member_map_.values())
        )


class UnbControlInfoSyntaxVersion(Enum):
    """An enumeration representing different categories.

    :cvar EDIFACTSYNTAXVERSION1: "EDIFACTSYNTAXVERSION_1"
    :vartype EDIFACTSYNTAXVERSION1: str
    :cvar EDIFACTSYNTAXVERSION2: "EDIFACTSYNTAXVERSION_2"
    :vartype EDIFACTSYNTAXVERSION2: str
    :cvar EDIFACTSYNTAXVERSION3: "EDIFACTSYNTAXVERSION_3"
    :vartype EDIFACTSYNTAXVERSION3: str
    """

    EDIFACTSYNTAXVERSION1 = "EDIFACTSYNTAXVERSION_1"
    EDIFACTSYNTAXVERSION2 = "EDIFACTSYNTAXVERSION_2"
    EDIFACTSYNTAXVERSION3 = "EDIFACTSYNTAXVERSION_3"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, UnbControlInfoSyntaxVersion._member_map_.values())
        )


class UnbControlInfoTestIndicator(Enum):
    """An enumeration representing different categories.

    :cvar EDIFACTTESTNA: "EDIFACTTEST_NA"
    :vartype EDIFACTTESTNA: str
    :cvar EDIFACTTEST1: "EDIFACTTEST_1"
    :vartype EDIFACTTEST1: str
    """

    EDIFACTTESTNA = "EDIFACTTEST_NA"
    EDIFACTTEST1 = "EDIFACTTEST_1"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, UnbControlInfoTestIndicator._member_map_.values())
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
class UnbControlInfo(BaseModel):
    """UnbControlInfo

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
    :type interchange_id_qual: UnbControlInfoInterchangeIdQual, optional
    :param interchange_sub_address: interchange_sub_address, defaults to None
    :type interchange_sub_address: str, optional
    :param priority: priority, defaults to None
    :type priority: UnbControlInfoPriority, optional
    :param reference_password: reference_password, defaults to None
    :type reference_password: str, optional
    :param reference_password_qualifier: reference_password_qualifier, defaults to None
    :type reference_password_qualifier: UnbControlInfoReferencePasswordQualifier, optional
    :param syntax_id: syntax_id, defaults to None
    :type syntax_id: UnbControlInfoSyntaxId, optional
    :param syntax_version: syntax_version, defaults to None
    :type syntax_version: UnbControlInfoSyntaxVersion, optional
    :param test_indicator: test_indicator, defaults to None
    :type test_indicator: UnbControlInfoTestIndicator, optional
    """

    def __init__(
        self,
        ack_request: bool = SENTINEL,
        app_reference: str = SENTINEL,
        comm_agreement: str = SENTINEL,
        interchange_address: str = SENTINEL,
        interchange_id: str = SENTINEL,
        interchange_id_qual: UnbControlInfoInterchangeIdQual = SENTINEL,
        interchange_sub_address: str = SENTINEL,
        priority: UnbControlInfoPriority = SENTINEL,
        reference_password: str = SENTINEL,
        reference_password_qualifier: UnbControlInfoReferencePasswordQualifier = SENTINEL,
        syntax_id: UnbControlInfoSyntaxId = SENTINEL,
        syntax_version: UnbControlInfoSyntaxVersion = SENTINEL,
        test_indicator: UnbControlInfoTestIndicator = SENTINEL,
        **kwargs
    ):
        """UnbControlInfo

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
        :type interchange_id_qual: UnbControlInfoInterchangeIdQual, optional
        :param interchange_sub_address: interchange_sub_address, defaults to None
        :type interchange_sub_address: str, optional
        :param priority: priority, defaults to None
        :type priority: UnbControlInfoPriority, optional
        :param reference_password: reference_password, defaults to None
        :type reference_password: str, optional
        :param reference_password_qualifier: reference_password_qualifier, defaults to None
        :type reference_password_qualifier: UnbControlInfoReferencePasswordQualifier, optional
        :param syntax_id: syntax_id, defaults to None
        :type syntax_id: UnbControlInfoSyntaxId, optional
        :param syntax_version: syntax_version, defaults to None
        :type syntax_version: UnbControlInfoSyntaxVersion, optional
        :param test_indicator: test_indicator, defaults to None
        :type test_indicator: UnbControlInfoTestIndicator, optional
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
                UnbControlInfoInterchangeIdQual.list(),
                "interchange_id_qual",
            )
        if interchange_sub_address is not SENTINEL:
            self.interchange_sub_address = interchange_sub_address
        if priority is not SENTINEL:
            self.priority = self._enum_matching(
                priority, UnbControlInfoPriority.list(), "priority"
            )
        if reference_password is not SENTINEL:
            self.reference_password = reference_password
        if reference_password_qualifier is not SENTINEL:
            self.reference_password_qualifier = self._enum_matching(
                reference_password_qualifier,
                UnbControlInfoReferencePasswordQualifier.list(),
                "reference_password_qualifier",
            )
        if syntax_id is not SENTINEL:
            self.syntax_id = self._enum_matching(
                syntax_id, UnbControlInfoSyntaxId.list(), "syntax_id"
            )
        if syntax_version is not SENTINEL:
            self.syntax_version = self._enum_matching(
                syntax_version, UnbControlInfoSyntaxVersion.list(), "syntax_version"
            )
        if test_indicator is not SENTINEL:
            self.test_indicator = self._enum_matching(
                test_indicator, UnbControlInfoTestIndicator.list(), "test_indicator"
            )
        self._kwargs = kwargs
