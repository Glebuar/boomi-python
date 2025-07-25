
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .oftp_listen_options_info import OftpListenOptionsInfo
from .oftp_partner_group_type import OftpPartnerGroupType


@JsonMap(
    {
        "oftp_listen_options": "OFTPListenOptions",
        "oftp_partner_group": "OFTPPartnerGroup",
        "partner_group_id": "partnerGroupId",
    }
)
class OftpListenOptions(BaseModel):
    """OftpListenOptions

    :param oftp_listen_options: oftp_listen_options
    :type oftp_listen_options: OftpListenOptionsInfo
    :param oftp_partner_group: oftp_partner_group
    :type oftp_partner_group: OftpPartnerGroupType
    :param partner_group_id: partner_group_id, defaults to None
    :type partner_group_id: str, optional
    """

    def __init__(
        self,
        oftp_listen_options: OftpListenOptionsInfo,
        oftp_partner_group: OftpPartnerGroupType,
        partner_group_id: str = SENTINEL,
        **kwargs,
    ):
        """OftpListenOptions

        :param oftp_listen_options: oftp_listen_options
        :type oftp_listen_options: OftpListenOptionsInfo
        :param oftp_partner_group: oftp_partner_group
        :type oftp_partner_group: OftpPartnerGroupType
        :param partner_group_id: partner_group_id, defaults to None
        :type partner_group_id: str, optional
        """
        self.oftp_listen_options = self._define_object(
            oftp_listen_options, OftpListenOptionsInfo
        )
        self.oftp_partner_group = self._define_object(
            oftp_partner_group, OftpPartnerGroupType
        )
        if partner_group_id is not SENTINEL:
            self.partner_group_id = partner_group_id
        self._kwargs = kwargs
