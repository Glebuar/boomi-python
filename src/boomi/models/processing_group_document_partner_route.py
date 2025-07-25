
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({"process_id": "processId", "trading_partner_id": "tradingPartnerId"})
class ProcessingGroupDocumentPartnerRoute(BaseModel):
    """ProcessingGroupDocumentPartnerRoute

    :param process_id: process_id, defaults to None
    :type process_id: str, optional
    :param trading_partner_id: trading_partner_id, defaults to None
    :type trading_partner_id: str, optional
    """

    def __init__(
        self, process_id: str = SENTINEL, trading_partner_id: str = SENTINEL, **kwargs
    ):
        """ProcessingGroupDocumentPartnerRoute

        :param process_id: process_id, defaults to None
        :type process_id: str, optional
        :param trading_partner_id: trading_partner_id, defaults to None
        :type trading_partner_id: str, optional
        """
        if process_id is not SENTINEL:
            self.process_id = process_id
        if trading_partner_id is not SENTINEL:
            self.trading_partner_id = trading_partner_id
        self._kwargs = kwargs
