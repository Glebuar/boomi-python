
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap(
    {
        "enable_archiving": "enableArchiving",
        "inbound_directory": "inboundDirectory",
        "outbound_directory": "outboundDirectory",
    }
)
class PartnerArchiving(BaseModel):
    """PartnerArchiving

    :param enable_archiving: enable_archiving, defaults to None
    :type enable_archiving: bool, optional
    :param inbound_directory: inbound_directory, defaults to None
    :type inbound_directory: str, optional
    :param outbound_directory: outbound_directory, defaults to None
    :type outbound_directory: str, optional
    """

    def __init__(
        self,
        enable_archiving: bool = SENTINEL,
        inbound_directory: str = SENTINEL,
        outbound_directory: str = SENTINEL,
        **kwargs
    ):
        """PartnerArchiving

        :param enable_archiving: enable_archiving, defaults to None
        :type enable_archiving: bool, optional
        :param inbound_directory: inbound_directory, defaults to None
        :type inbound_directory: str, optional
        :param outbound_directory: outbound_directory, defaults to None
        :type outbound_directory: str, optional
        """
        if enable_archiving is not SENTINEL:
            self.enable_archiving = enable_archiving
        if inbound_directory is not SENTINEL:
            self.inbound_directory = inbound_directory
        if outbound_directory is not SENTINEL:
            self.outbound_directory = outbound_directory
        self._kwargs = kwargs
