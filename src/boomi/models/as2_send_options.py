
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .as2_mdn_options import As2MdnOptions
from .as2_message_options import As2MessageOptions
from .as2_partner_info import As2PartnerInfo


@JsonMap(
    {
        "as2_mdn_options": "AS2MDNOptions",
        "as2_message_options": "AS2MessageOptions",
        "as2_partner_info": "AS2PartnerInfo",
    }
)
class As2SendOptions(BaseModel):
    """As2SendOptions

    :param as2_mdn_options: as2_mdn_options
    :type as2_mdn_options: As2MdnOptions
    :param as2_message_options: as2_message_options
    :type as2_message_options: As2MessageOptions
    :param as2_partner_info: as2_partner_info, defaults to None
    :type as2_partner_info: As2PartnerInfo, optional
    """

    def __init__(
        self,
        as2_mdn_options: As2MdnOptions,
        as2_message_options: As2MessageOptions,
        as2_partner_info: As2PartnerInfo = SENTINEL,
        **kwargs,
    ):
        """As2SendOptions

        :param as2_mdn_options: as2_mdn_options
        :type as2_mdn_options: As2MdnOptions
        :param as2_message_options: as2_message_options
        :type as2_message_options: As2MessageOptions
        :param as2_partner_info: as2_partner_info, defaults to None
        :type as2_partner_info: As2PartnerInfo, optional
        """
        self.as2_mdn_options = self._define_object(as2_mdn_options, As2MdnOptions)
        self.as2_message_options = self._define_object(
            as2_message_options, As2MessageOptions
        )
        if as2_partner_info is not SENTINEL:
            self.as2_partner_info = self._define_object(
                as2_partner_info, As2PartnerInfo
            )
        self._kwargs = kwargs
