
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .oftp_partner_info import OftpPartnerInfo
from .oftp_local_info import OftpLocalInfo


@JsonMap(
    {
        "default_partner_info": "defaultPartnerInfo",
        "my_company_info": "myCompanyInfo",
        "my_partner_info": "myPartnerInfo",
    }
)
class OftpPartnerGroupType(BaseModel):
    """OftpPartnerGroupType

    :param default_partner_info: default_partner_info, defaults to None
    :type default_partner_info: OftpPartnerInfo, optional
    :param my_company_info: my_company_info
    :type my_company_info: OftpLocalInfo
    :param my_partner_info: my_partner_info
    :type my_partner_info: OftpPartnerInfo
    """

    def __init__(
        self,
        my_company_info: OftpLocalInfo,
        my_partner_info: OftpPartnerInfo,
        default_partner_info: OftpPartnerInfo = SENTINEL,
        **kwargs,
    ):
        """OftpPartnerGroupType

        :param default_partner_info: default_partner_info, defaults to None
        :type default_partner_info: OftpPartnerInfo, optional
        :param my_company_info: my_company_info
        :type my_company_info: OftpLocalInfo
        :param my_partner_info: my_partner_info
        :type my_partner_info: OftpPartnerInfo
        """
        if default_partner_info is not SENTINEL:
            self.default_partner_info = self._define_object(
                default_partner_info, OftpPartnerInfo
            )
        self.my_company_info = self._define_object(my_company_info, OftpLocalInfo)
        self.my_partner_info = self._define_object(my_partner_info, OftpPartnerInfo)
        self._kwargs = kwargs
