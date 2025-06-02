
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .oftp_partner_group_type import OftpPartnerGroupType
from .oftp_send_options_info import OftpSendOptionsInfo


@JsonMap(
    {
        "oftp_partner_group": "OFTPPartnerGroup",
        "oftp_send_options": "OFTPSendOptions",
        "partner_group_id": "partnerGroupId",
    }
)
class OftpSendOptions(BaseModel):
    """OftpSendOptions

    :param oftp_partner_group: oftp_partner_group
    :type oftp_partner_group: OftpPartnerGroupType
    :param oftp_send_options: oftp_send_options
    :type oftp_send_options: OftpSendOptionsInfo
    :param partner_group_id: partner_group_id, defaults to None
    :type partner_group_id: str, optional
    """

    def __init__(
        self,
        oftp_partner_group: OftpPartnerGroupType,
        oftp_send_options: OftpSendOptionsInfo,
        partner_group_id: str = SENTINEL,
        **kwargs,
    ):
        """OftpSendOptions

        :param oftp_partner_group: oftp_partner_group
        :type oftp_partner_group: OftpPartnerGroupType
        :param oftp_send_options: oftp_send_options
        :type oftp_send_options: OftpSendOptionsInfo
        :param partner_group_id: partner_group_id, defaults to None
        :type partner_group_id: str, optional
        """
        self.oftp_partner_group = self._define_object(
            oftp_partner_group, OftpPartnerGroupType
        )
        self.oftp_send_options = self._define_object(
            oftp_send_options, OftpSendOptionsInfo
        )
        if partner_group_id is not SENTINEL:
            self.partner_group_id = partner_group_id
        self._kwargs = kwargs
