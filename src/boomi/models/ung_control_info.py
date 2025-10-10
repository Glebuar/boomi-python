
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class ApplicationIdQual(Enum):
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
        return list(map(lambda x: x.value, ApplicationIdQual._member_map_.values()))


@JsonMap(
    {
        "application_id": "applicationId",
        "application_id_qual": "applicationIdQual",
        "use_functional_groups": "useFunctionalGroups",
    }
)
class UngControlInfo(BaseModel):
    """UngControlInfo

    :param application_id: application_id, defaults to None
    :type application_id: str, optional
    :param application_id_qual: application_id_qual, defaults to None
    :type application_id_qual: ApplicationIdQual, optional
    :param use_functional_groups: use_functional_groups, defaults to None
    :type use_functional_groups: bool, optional
    """

    def __init__(
        self,
        application_id: str = SENTINEL,
        application_id_qual: ApplicationIdQual = SENTINEL,
        use_functional_groups: bool = SENTINEL,
        **kwargs
    ):
        """UngControlInfo

        :param application_id: application_id, defaults to None
        :type application_id: str, optional
        :param application_id_qual: application_id_qual, defaults to None
        :type application_id_qual: ApplicationIdQual, optional
        :param use_functional_groups: use_functional_groups, defaults to None
        :type use_functional_groups: bool, optional
        """
        if application_id is not SENTINEL:
            self.application_id = application_id
        if application_id_qual is not SENTINEL:
            self.application_id_qual = self._enum_matching(
                application_id_qual, ApplicationIdQual.list(), "application_id_qual"
            )
        if use_functional_groups is not SENTINEL:
            self.use_functional_groups = use_functional_groups
        self._kwargs = kwargs
