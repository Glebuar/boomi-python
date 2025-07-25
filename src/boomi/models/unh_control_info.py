
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class UnhControlInfoControllingAgency(Enum):
    """An enumeration representing different categories.

    :cvar AA: "AA"
    :vartype AA: str
    :cvar AB: "AB"
    :vartype AB: str
    :cvar AC: "AC"
    :vartype AC: str
    :cvar AD: "AD"
    :vartype AD: str
    :cvar AE: "AE"
    :vartype AE: str
    :cvar CC: "CC"
    :vartype CC: str
    :cvar CE: "CE"
    :vartype CE: str
    :cvar EC: "EC"
    :vartype EC: str
    :cvar ED: "ED"
    :vartype ED: str
    :cvar EE: "EE"
    :vartype EE: str
    :cvar EN: "EN"
    :vartype EN: str
    :cvar ER: "ER"
    :vartype ER: str
    :cvar EU: "EU"
    :vartype EU: str
    :cvar EX: "EX"
    :vartype EX: str
    :cvar IA: "IA"
    :vartype IA: str
    :cvar KE: "KE"
    :vartype KE: str
    :cvar LI: "LI"
    :vartype LI: str
    :cvar OD: "OD"
    :vartype OD: str
    :cvar RI: "RI"
    :vartype RI: str
    :cvar RT: "RT"
    :vartype RT: str
    :cvar UN: "UN"
    :vartype UN: str
    """

    AA = "AA"
    AB = "AB"
    AC = "AC"
    AD = "AD"
    AE = "AE"
    CC = "CC"
    CE = "CE"
    EC = "EC"
    ED = "ED"
    EE = "EE"
    EN = "EN"
    ER = "ER"
    EU = "EU"
    EX = "EX"
    IA = "IA"
    KE = "KE"
    LI = "LI"
    OD = "OD"
    RI = "RI"
    RT = "RT"
    UN = "UN"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value, UnhControlInfoControllingAgency._member_map_.values()
            )
        )


class UnhControlInfoRelease(Enum):
    """An enumeration representing different categories.

    :cvar EDIFACTRELEASE1: "EDIFACTRELEASE_1"
    :vartype EDIFACTRELEASE1: str
    :cvar EDIFACTRELEASE2: "EDIFACTRELEASE_2"
    :vartype EDIFACTRELEASE2: str
    :cvar EDIFACTRELEASE902: "EDIFACTRELEASE_902"
    :vartype EDIFACTRELEASE902: str
    :cvar EDIFACTRELEASE911: "EDIFACTRELEASE_911"
    :vartype EDIFACTRELEASE911: str
    :cvar EDIFACTRELEASE912: "EDIFACTRELEASE_912"
    :vartype EDIFACTRELEASE912: str
    :cvar EDIFACTRELEASE921: "EDIFACTRELEASE_921"
    :vartype EDIFACTRELEASE921: str
    :cvar EDIFACTRELEASE932: "EDIFACTRELEASE_932"
    :vartype EDIFACTRELEASE932: str
    :cvar EDIFACTRELEASE93A: "EDIFACTRELEASE_93A"
    :vartype EDIFACTRELEASE93A: str
    :cvar EDIFACTRELEASE94A: "EDIFACTRELEASE_94A"
    :vartype EDIFACTRELEASE94A: str
    :cvar EDIFACTRELEASE94B: "EDIFACTRELEASE_94B"
    :vartype EDIFACTRELEASE94B: str
    :cvar EDIFACTRELEASE95A: "EDIFACTRELEASE_95A"
    :vartype EDIFACTRELEASE95A: str
    :cvar EDIFACTRELEASE95B: "EDIFACTRELEASE_95B"
    :vartype EDIFACTRELEASE95B: str
    :cvar EDIFACTRELEASE96A: "EDIFACTRELEASE_96A"
    :vartype EDIFACTRELEASE96A: str
    :cvar EDIFACTRELEASE96B: "EDIFACTRELEASE_96B"
    :vartype EDIFACTRELEASE96B: str
    :cvar EDIFACTRELEASE97A: "EDIFACTRELEASE_97A"
    :vartype EDIFACTRELEASE97A: str
    :cvar EDIFACTRELEASE97B: "EDIFACTRELEASE_97B"
    :vartype EDIFACTRELEASE97B: str
    :cvar EDIFACTRELEASE98A: "EDIFACTRELEASE_98A"
    :vartype EDIFACTRELEASE98A: str
    :cvar EDIFACTRELEASE98B: "EDIFACTRELEASE_98B"
    :vartype EDIFACTRELEASE98B: str
    :cvar EDIFACTRELEASE99A: "EDIFACTRELEASE_99A"
    :vartype EDIFACTRELEASE99A: str
    :cvar EDIFACTRELEASE99B: "EDIFACTRELEASE_99B"
    :vartype EDIFACTRELEASE99B: str
    :cvar EDIFACTRELEASE00A: "EDIFACTRELEASE_00A"
    :vartype EDIFACTRELEASE00A: str
    :cvar EDIFACTRELEASE00B: "EDIFACTRELEASE_00B"
    :vartype EDIFACTRELEASE00B: str
    :cvar EDIFACTRELEASE01A: "EDIFACTRELEASE_01A"
    :vartype EDIFACTRELEASE01A: str
    :cvar EDIFACTRELEASE01B: "EDIFACTRELEASE_01B"
    :vartype EDIFACTRELEASE01B: str
    :cvar EDIFACTRELEASE02A: "EDIFACTRELEASE_02A"
    :vartype EDIFACTRELEASE02A: str
    :cvar EDIFACTRELEASE02B: "EDIFACTRELEASE_02B"
    :vartype EDIFACTRELEASE02B: str
    :cvar EDIFACTRELEASE03A: "EDIFACTRELEASE_03A"
    :vartype EDIFACTRELEASE03A: str
    :cvar EDIFACTRELEASE03B: "EDIFACTRELEASE_03B"
    :vartype EDIFACTRELEASE03B: str
    :cvar EDIFACTRELEASE04A: "EDIFACTRELEASE_04A"
    :vartype EDIFACTRELEASE04A: str
    :cvar EDIFACTRELEASE04B: "EDIFACTRELEASE_04B"
    :vartype EDIFACTRELEASE04B: str
    :cvar EDIFACTRELEASE05A: "EDIFACTRELEASE_05A"
    :vartype EDIFACTRELEASE05A: str
    :cvar EDIFACTRELEASE05B: "EDIFACTRELEASE_05B"
    :vartype EDIFACTRELEASE05B: str
    :cvar EDIFACTRELEASE06A: "EDIFACTRELEASE_06A"
    :vartype EDIFACTRELEASE06A: str
    :cvar EDIFACTRELEASE06B: "EDIFACTRELEASE_06B"
    :vartype EDIFACTRELEASE06B: str
    :cvar EDIFACTRELEASE07A: "EDIFACTRELEASE_07A"
    :vartype EDIFACTRELEASE07A: str
    :cvar EDIFACTRELEASE07B: "EDIFACTRELEASE_07B"
    :vartype EDIFACTRELEASE07B: str
    :cvar EDIFACTRELEASE08A: "EDIFACTRELEASE_08A"
    :vartype EDIFACTRELEASE08A: str
    :cvar EDIFACTRELEASE08B: "EDIFACTRELEASE_08B"
    :vartype EDIFACTRELEASE08B: str
    :cvar EDIFACTRELEASE09A: "EDIFACTRELEASE_09A"
    :vartype EDIFACTRELEASE09A: str
    :cvar EDIFACTRELEASE09B: "EDIFACTRELEASE_09B"
    :vartype EDIFACTRELEASE09B: str
    """

    EDIFACTRELEASE1 = "EDIFACTRELEASE_1"
    EDIFACTRELEASE2 = "EDIFACTRELEASE_2"
    EDIFACTRELEASE902 = "EDIFACTRELEASE_902"
    EDIFACTRELEASE911 = "EDIFACTRELEASE_911"
    EDIFACTRELEASE912 = "EDIFACTRELEASE_912"
    EDIFACTRELEASE921 = "EDIFACTRELEASE_921"
    EDIFACTRELEASE932 = "EDIFACTRELEASE_932"
    EDIFACTRELEASE93A = "EDIFACTRELEASE_93A"
    EDIFACTRELEASE94A = "EDIFACTRELEASE_94A"
    EDIFACTRELEASE94B = "EDIFACTRELEASE_94B"
    EDIFACTRELEASE95A = "EDIFACTRELEASE_95A"
    EDIFACTRELEASE95B = "EDIFACTRELEASE_95B"
    EDIFACTRELEASE96A = "EDIFACTRELEASE_96A"
    EDIFACTRELEASE96B = "EDIFACTRELEASE_96B"
    EDIFACTRELEASE97A = "EDIFACTRELEASE_97A"
    EDIFACTRELEASE97B = "EDIFACTRELEASE_97B"
    EDIFACTRELEASE98A = "EDIFACTRELEASE_98A"
    EDIFACTRELEASE98B = "EDIFACTRELEASE_98B"
    EDIFACTRELEASE99A = "EDIFACTRELEASE_99A"
    EDIFACTRELEASE99B = "EDIFACTRELEASE_99B"
    EDIFACTRELEASE00A = "EDIFACTRELEASE_00A"
    EDIFACTRELEASE00B = "EDIFACTRELEASE_00B"
    EDIFACTRELEASE01A = "EDIFACTRELEASE_01A"
    EDIFACTRELEASE01B = "EDIFACTRELEASE_01B"
    EDIFACTRELEASE02A = "EDIFACTRELEASE_02A"
    EDIFACTRELEASE02B = "EDIFACTRELEASE_02B"
    EDIFACTRELEASE03A = "EDIFACTRELEASE_03A"
    EDIFACTRELEASE03B = "EDIFACTRELEASE_03B"
    EDIFACTRELEASE04A = "EDIFACTRELEASE_04A"
    EDIFACTRELEASE04B = "EDIFACTRELEASE_04B"
    EDIFACTRELEASE05A = "EDIFACTRELEASE_05A"
    EDIFACTRELEASE05B = "EDIFACTRELEASE_05B"
    EDIFACTRELEASE06A = "EDIFACTRELEASE_06A"
    EDIFACTRELEASE06B = "EDIFACTRELEASE_06B"
    EDIFACTRELEASE07A = "EDIFACTRELEASE_07A"
    EDIFACTRELEASE07B = "EDIFACTRELEASE_07B"
    EDIFACTRELEASE08A = "EDIFACTRELEASE_08A"
    EDIFACTRELEASE08B = "EDIFACTRELEASE_08B"
    EDIFACTRELEASE09A = "EDIFACTRELEASE_09A"
    EDIFACTRELEASE09B = "EDIFACTRELEASE_09B"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, UnhControlInfoRelease._member_map_.values()))


class UnhControlInfoVersion(Enum):
    """An enumeration representing different categories.

    :cvar EDIFACTVERSION1: "EDIFACTVERSION_1"
    :vartype EDIFACTVERSION1: str
    :cvar EDIFACTVERSION2: "EDIFACTVERSION_2"
    :vartype EDIFACTVERSION2: str
    :cvar EDIFACTVERSION4: "EDIFACTVERSION_4"
    :vartype EDIFACTVERSION4: str
    :cvar EDIFACTVERSION88: "EDIFACTVERSION_88"
    :vartype EDIFACTVERSION88: str
    :cvar EDIFACTVERSION89: "EDIFACTVERSION_89"
    :vartype EDIFACTVERSION89: str
    :cvar EDIFACTVERSION90: "EDIFACTVERSION_90"
    :vartype EDIFACTVERSION90: str
    :cvar EDIFACTVERSIOND: "EDIFACTVERSION_D"
    :vartype EDIFACTVERSIOND: str
    :cvar EDIFACTVERSIONS: "EDIFACTVERSION_S"
    :vartype EDIFACTVERSIONS: str
    """

    EDIFACTVERSION1 = "EDIFACTVERSION_1"
    EDIFACTVERSION2 = "EDIFACTVERSION_2"
    EDIFACTVERSION4 = "EDIFACTVERSION_4"
    EDIFACTVERSION88 = "EDIFACTVERSION_88"
    EDIFACTVERSION89 = "EDIFACTVERSION_89"
    EDIFACTVERSION90 = "EDIFACTVERSION_90"
    EDIFACTVERSIOND = "EDIFACTVERSION_D"
    EDIFACTVERSIONS = "EDIFACTVERSION_S"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, UnhControlInfoVersion._member_map_.values()))


@JsonMap(
    {
        "assoc_assigned_code": "assocAssignedCode",
        "common_access_ref": "commonAccessRef",
        "controlling_agency": "controllingAgency",
    }
)
class UnhControlInfo(BaseModel):
    """UnhControlInfo

    :param assoc_assigned_code: assoc_assigned_code, defaults to None
    :type assoc_assigned_code: str, optional
    :param common_access_ref: common_access_ref, defaults to None
    :type common_access_ref: str, optional
    :param controlling_agency: controlling_agency, defaults to None
    :type controlling_agency: UnhControlInfoControllingAgency, optional
    :param release: release, defaults to None
    :type release: UnhControlInfoRelease, optional
    :param version: version, defaults to None
    :type version: UnhControlInfoVersion, optional
    """

    def __init__(
        self,
        assoc_assigned_code: str = SENTINEL,
        common_access_ref: str = SENTINEL,
        controlling_agency: UnhControlInfoControllingAgency = SENTINEL,
        release: UnhControlInfoRelease = SENTINEL,
        version: UnhControlInfoVersion = SENTINEL,
        **kwargs
    ):
        """UnhControlInfo

        :param assoc_assigned_code: assoc_assigned_code, defaults to None
        :type assoc_assigned_code: str, optional
        :param common_access_ref: common_access_ref, defaults to None
        :type common_access_ref: str, optional
        :param controlling_agency: controlling_agency, defaults to None
        :type controlling_agency: UnhControlInfoControllingAgency, optional
        :param release: release, defaults to None
        :type release: UnhControlInfoRelease, optional
        :param version: version, defaults to None
        :type version: UnhControlInfoVersion, optional
        """
        if assoc_assigned_code is not SENTINEL:
            self.assoc_assigned_code = assoc_assigned_code
        if common_access_ref is not SENTINEL:
            self.common_access_ref = common_access_ref
        if controlling_agency is not SENTINEL:
            self.controlling_agency = self._enum_matching(
                controlling_agency,
                UnhControlInfoControllingAgency.list(),
                "controlling_agency",
            )
        if release is not SENTINEL:
            self.release = self._enum_matching(
                release, UnhControlInfoRelease.list(), "release"
            )
        if version is not SENTINEL:
            self.version = self._enum_matching(
                version, UnhControlInfoVersion.list(), "version"
            )
        self._kwargs = kwargs
