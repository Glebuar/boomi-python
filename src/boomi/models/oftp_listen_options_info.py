
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .oftp_partner_group_type import OftpPartnerGroupType


@JsonMap({"gateway_partner_group": "GatewayPartnerGroup", "use_gateway": "useGateway"})
class OftpListenOptionsInfo(BaseModel):
    """OftpListenOptionsInfo

    :param gateway_partner_group: gateway_partner_group
    :type gateway_partner_group: OftpPartnerGroupType
    :param operation: operation, defaults to None
    :type operation: str, optional
    :param use_gateway: use_gateway, defaults to None
    :type use_gateway: bool, optional
    """

    def __init__(
        self,
        gateway_partner_group: OftpPartnerGroupType,
        operation: str = SENTINEL,
        use_gateway: bool = SENTINEL,
        **kwargs,
    ):
        """OftpListenOptionsInfo

        :param gateway_partner_group: gateway_partner_group
        :type gateway_partner_group: OftpPartnerGroupType
        :param operation: operation, defaults to None
        :type operation: str, optional
        :param use_gateway: use_gateway, defaults to None
        :type use_gateway: bool, optional
        """
        self.gateway_partner_group = self._define_object(
            gateway_partner_group, OftpPartnerGroupType
        )
        if operation is not SENTINEL:
            self.operation = operation
        if use_gateway is not SENTINEL:
            self.use_gateway = use_gateway
        self._kwargs = kwargs
