
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .default_oftp_partner_send_settings import DefaultOftpPartnerSendSettings


@JsonMap({"default_partner_settings": "defaultPartnerSettings"})
class OftpSendOptionsInfo(BaseModel):
    """OftpSendOptionsInfo

    :param cd: cd, defaults to None
    :type cd: bool, optional
    :param default_partner_settings: default_partner_settings
    :type default_partner_settings: DefaultOftpPartnerSendSettings
    :param operation: operation, defaults to None
    :type operation: str, optional
    :param sfiddesc: sfiddesc, defaults to None
    :type sfiddesc: str, optional
    :param sfiddsn: sfiddsn, defaults to None
    :type sfiddsn: str, optional
    """

    def __init__(
        self,
        default_partner_settings: DefaultOftpPartnerSendSettings,
        cd: bool = SENTINEL,
        operation: str = SENTINEL,
        sfiddesc: str = SENTINEL,
        sfiddsn: str = SENTINEL,
        **kwargs,
    ):
        """OftpSendOptionsInfo

        :param cd: cd, defaults to None
        :type cd: bool, optional
        :param default_partner_settings: default_partner_settings
        :type default_partner_settings: DefaultOftpPartnerSendSettings
        :param operation: operation, defaults to None
        :type operation: str, optional
        :param sfiddesc: sfiddesc, defaults to None
        :type sfiddesc: str, optional
        :param sfiddsn: sfiddsn, defaults to None
        :type sfiddsn: str, optional
        """
        if cd is not SENTINEL:
            self.cd = cd
        self.default_partner_settings = self._define_object(
            default_partner_settings, DefaultOftpPartnerSendSettings
        )
        if operation is not SENTINEL:
            self.operation = operation
        if sfiddesc is not SENTINEL:
            self.sfiddesc = sfiddesc
        if sfiddsn is not SENTINEL:
            self.sfiddsn = sfiddsn
        self._kwargs = kwargs
