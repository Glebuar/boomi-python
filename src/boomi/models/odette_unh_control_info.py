
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class OdetteUnhControlInfoControllingAgency(Enum):
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
                lambda x: x.value,
                OdetteUnhControlInfoControllingAgency._member_map_.values(),
            )
        )


class OdetteUnhControlInfoRelease(Enum):
    """An enumeration representing different categories.

    :cvar ODETTERELEASE1: "ODETTERELEASE_1"
    :vartype ODETTERELEASE1: str
    :cvar ODETTERELEASE2: "ODETTERELEASE_2"
    :vartype ODETTERELEASE2: str
    :cvar ODETTERELEASE902: "ODETTERELEASE_902"
    :vartype ODETTERELEASE902: str
    :cvar ODETTERELEASE911: "ODETTERELEASE_911"
    :vartype ODETTERELEASE911: str
    :cvar ODETTERELEASE912: "ODETTERELEASE_912"
    :vartype ODETTERELEASE912: str
    :cvar ODETTERELEASE921: "ODETTERELEASE_921"
    :vartype ODETTERELEASE921: str
    :cvar ODETTERELEASE932: "ODETTERELEASE_932"
    :vartype ODETTERELEASE932: str
    :cvar ODETTERELEASE93A: "ODETTERELEASE_93A"
    :vartype ODETTERELEASE93A: str
    :cvar ODETTERELEASE94A: "ODETTERELEASE_94A"
    :vartype ODETTERELEASE94A: str
    :cvar ODETTERELEASE94B: "ODETTERELEASE_94B"
    :vartype ODETTERELEASE94B: str
    :cvar ODETTERELEASE95A: "ODETTERELEASE_95A"
    :vartype ODETTERELEASE95A: str
    :cvar ODETTERELEASE95B: "ODETTERELEASE_95B"
    :vartype ODETTERELEASE95B: str
    :cvar ODETTERELEASE96A: "ODETTERELEASE_96A"
    :vartype ODETTERELEASE96A: str
    :cvar ODETTERELEASE96B: "ODETTERELEASE_96B"
    :vartype ODETTERELEASE96B: str
    :cvar ODETTERELEASE97A: "ODETTERELEASE_97A"
    :vartype ODETTERELEASE97A: str
    :cvar ODETTERELEASE97B: "ODETTERELEASE_97B"
    :vartype ODETTERELEASE97B: str
    :cvar ODETTERELEASE98A: "ODETTERELEASE_98A"
    :vartype ODETTERELEASE98A: str
    :cvar ODETTERELEASE98B: "ODETTERELEASE_98B"
    :vartype ODETTERELEASE98B: str
    :cvar ODETTERELEASE99A: "ODETTERELEASE_99A"
    :vartype ODETTERELEASE99A: str
    :cvar ODETTERELEASE99B: "ODETTERELEASE_99B"
    :vartype ODETTERELEASE99B: str
    :cvar ODETTERELEASE00A: "ODETTERELEASE_00A"
    :vartype ODETTERELEASE00A: str
    :cvar ODETTERELEASE00B: "ODETTERELEASE_00B"
    :vartype ODETTERELEASE00B: str
    :cvar ODETTERELEASE01A: "ODETTERELEASE_01A"
    :vartype ODETTERELEASE01A: str
    :cvar ODETTERELEASE01B: "ODETTERELEASE_01B"
    :vartype ODETTERELEASE01B: str
    :cvar ODETTERELEASE02A: "ODETTERELEASE_02A"
    :vartype ODETTERELEASE02A: str
    :cvar ODETTERELEASE02B: "ODETTERELEASE_02B"
    :vartype ODETTERELEASE02B: str
    :cvar ODETTERELEASE03A: "ODETTERELEASE_03A"
    :vartype ODETTERELEASE03A: str
    :cvar ODETTERELEASE03B: "ODETTERELEASE_03B"
    :vartype ODETTERELEASE03B: str
    :cvar ODETTERELEASE04A: "ODETTERELEASE_04A"
    :vartype ODETTERELEASE04A: str
    :cvar ODETTERELEASE04B: "ODETTERELEASE_04B"
    :vartype ODETTERELEASE04B: str
    :cvar ODETTERELEASE05A: "ODETTERELEASE_05A"
    :vartype ODETTERELEASE05A: str
    :cvar ODETTERELEASE05B: "ODETTERELEASE_05B"
    :vartype ODETTERELEASE05B: str
    :cvar ODETTERELEASE06A: "ODETTERELEASE_06A"
    :vartype ODETTERELEASE06A: str
    :cvar ODETTERELEASE06B: "ODETTERELEASE_06B"
    :vartype ODETTERELEASE06B: str
    :cvar ODETTERELEASE07A: "ODETTERELEASE_07A"
    :vartype ODETTERELEASE07A: str
    :cvar ODETTERELEASE07B: "ODETTERELEASE_07B"
    :vartype ODETTERELEASE07B: str
    :cvar ODETTERELEASE08A: "ODETTERELEASE_08A"
    :vartype ODETTERELEASE08A: str
    :cvar ODETTERELEASE08B: "ODETTERELEASE_08B"
    :vartype ODETTERELEASE08B: str
    :cvar ODETTERELEASE09A: "ODETTERELEASE_09A"
    :vartype ODETTERELEASE09A: str
    :cvar ODETTERELEASE09B: "ODETTERELEASE_09B"
    :vartype ODETTERELEASE09B: str
    """

    ODETTERELEASE1 = "ODETTERELEASE_1"
    ODETTERELEASE2 = "ODETTERELEASE_2"
    ODETTERELEASE902 = "ODETTERELEASE_902"
    ODETTERELEASE911 = "ODETTERELEASE_911"
    ODETTERELEASE912 = "ODETTERELEASE_912"
    ODETTERELEASE921 = "ODETTERELEASE_921"
    ODETTERELEASE932 = "ODETTERELEASE_932"
    ODETTERELEASE93A = "ODETTERELEASE_93A"
    ODETTERELEASE94A = "ODETTERELEASE_94A"
    ODETTERELEASE94B = "ODETTERELEASE_94B"
    ODETTERELEASE95A = "ODETTERELEASE_95A"
    ODETTERELEASE95B = "ODETTERELEASE_95B"
    ODETTERELEASE96A = "ODETTERELEASE_96A"
    ODETTERELEASE96B = "ODETTERELEASE_96B"
    ODETTERELEASE97A = "ODETTERELEASE_97A"
    ODETTERELEASE97B = "ODETTERELEASE_97B"
    ODETTERELEASE98A = "ODETTERELEASE_98A"
    ODETTERELEASE98B = "ODETTERELEASE_98B"
    ODETTERELEASE99A = "ODETTERELEASE_99A"
    ODETTERELEASE99B = "ODETTERELEASE_99B"
    ODETTERELEASE00A = "ODETTERELEASE_00A"
    ODETTERELEASE00B = "ODETTERELEASE_00B"
    ODETTERELEASE01A = "ODETTERELEASE_01A"
    ODETTERELEASE01B = "ODETTERELEASE_01B"
    ODETTERELEASE02A = "ODETTERELEASE_02A"
    ODETTERELEASE02B = "ODETTERELEASE_02B"
    ODETTERELEASE03A = "ODETTERELEASE_03A"
    ODETTERELEASE03B = "ODETTERELEASE_03B"
    ODETTERELEASE04A = "ODETTERELEASE_04A"
    ODETTERELEASE04B = "ODETTERELEASE_04B"
    ODETTERELEASE05A = "ODETTERELEASE_05A"
    ODETTERELEASE05B = "ODETTERELEASE_05B"
    ODETTERELEASE06A = "ODETTERELEASE_06A"
    ODETTERELEASE06B = "ODETTERELEASE_06B"
    ODETTERELEASE07A = "ODETTERELEASE_07A"
    ODETTERELEASE07B = "ODETTERELEASE_07B"
    ODETTERELEASE08A = "ODETTERELEASE_08A"
    ODETTERELEASE08B = "ODETTERELEASE_08B"
    ODETTERELEASE09A = "ODETTERELEASE_09A"
    ODETTERELEASE09B = "ODETTERELEASE_09B"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, OdetteUnhControlInfoRelease._member_map_.values())
        )


class OdetteUnhControlInfoVersion(Enum):
    """An enumeration representing different categories.

    :cvar ODETTEVERSION1: "ODETTEVERSION_1"
    :vartype ODETTEVERSION1: str
    :cvar ODETTEVERSION2: "ODETTEVERSION_2"
    :vartype ODETTEVERSION2: str
    :cvar ODETTEVERSION4: "ODETTEVERSION_4"
    :vartype ODETTEVERSION4: str
    :cvar ODETTEVERSION88: "ODETTEVERSION_88"
    :vartype ODETTEVERSION88: str
    :cvar ODETTEVERSION89: "ODETTEVERSION_89"
    :vartype ODETTEVERSION89: str
    :cvar ODETTEVERSION90: "ODETTEVERSION_90"
    :vartype ODETTEVERSION90: str
    :cvar ODETTEVERSIOND: "ODETTEVERSION_D"
    :vartype ODETTEVERSIOND: str
    :cvar ODETTEVERSIONS: "ODETTEVERSION_S"
    :vartype ODETTEVERSIONS: str
    """

    ODETTEVERSION1 = "ODETTEVERSION_1"
    ODETTEVERSION2 = "ODETTEVERSION_2"
    ODETTEVERSION4 = "ODETTEVERSION_4"
    ODETTEVERSION88 = "ODETTEVERSION_88"
    ODETTEVERSION89 = "ODETTEVERSION_89"
    ODETTEVERSION90 = "ODETTEVERSION_90"
    ODETTEVERSIOND = "ODETTEVERSION_D"
    ODETTEVERSIONS = "ODETTEVERSION_S"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, OdetteUnhControlInfoVersion._member_map_.values())
        )


@JsonMap(
    {
        "assoc_assigned_code": "assocAssignedCode",
        "common_access_ref": "commonAccessRef",
        "controlling_agency": "controllingAgency",
    }
)
class OdetteUnhControlInfo(BaseModel):
    """OdetteUnhControlInfo

    :param assoc_assigned_code: assoc_assigned_code, defaults to None
    :type assoc_assigned_code: str, optional
    :param common_access_ref: common_access_ref, defaults to None
    :type common_access_ref: str, optional
    :param controlling_agency: controlling_agency, defaults to None
    :type controlling_agency: OdetteUnhControlInfoControllingAgency, optional
    :param release: release, defaults to None
    :type release: OdetteUnhControlInfoRelease, optional
    :param version: version, defaults to None
    :type version: OdetteUnhControlInfoVersion, optional
    """

    def __init__(
        self,
        assoc_assigned_code: str = SENTINEL,
        common_access_ref: str = SENTINEL,
        controlling_agency: OdetteUnhControlInfoControllingAgency = SENTINEL,
        release: OdetteUnhControlInfoRelease = SENTINEL,
        version: OdetteUnhControlInfoVersion = SENTINEL,
        **kwargs
    ):
        """OdetteUnhControlInfo

        :param assoc_assigned_code: assoc_assigned_code, defaults to None
        :type assoc_assigned_code: str, optional
        :param common_access_ref: common_access_ref, defaults to None
        :type common_access_ref: str, optional
        :param controlling_agency: controlling_agency, defaults to None
        :type controlling_agency: OdetteUnhControlInfoControllingAgency, optional
        :param release: release, defaults to None
        :type release: OdetteUnhControlInfoRelease, optional
        :param version: version, defaults to None
        :type version: OdetteUnhControlInfoVersion, optional
        """
        if assoc_assigned_code is not SENTINEL:
            self.assoc_assigned_code = assoc_assigned_code
        if common_access_ref is not SENTINEL:
            self.common_access_ref = common_access_ref
        if controlling_agency is not SENTINEL:
            self.controlling_agency = self._enum_matching(
                controlling_agency,
                OdetteUnhControlInfoControllingAgency.list(),
                "controlling_agency",
            )
        if release is not SENTINEL:
            self.release = self._enum_matching(
                release, OdetteUnhControlInfoRelease.list(), "release"
            )
        if version is not SENTINEL:
            self.version = self._enum_matching(
                version, OdetteUnhControlInfoVersion.list(), "version"
            )
        self._kwargs = kwargs
