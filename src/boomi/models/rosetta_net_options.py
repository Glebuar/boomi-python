
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class RosettaNetOptionsVersion(Enum):
    """An enumeration representing different categories.

    :cvar V11: "v11"
    :vartype V11: str
    :cvar V20: "v20"
    :vartype V20: str
    """

    V11 = "v11"
    V20 = "v20"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, RosettaNetOptionsVersion._member_map_.values())
        )


@JsonMap(
    {
        "filter_signals": "filterSignals",
        "outbound_document_validation": "outboundDocumentValidation",
        "reject_duplicate_transactions": "rejectDuplicateTransactions",
    }
)
class RosettaNetOptions(BaseModel):
    """RosettaNetOptions

    :param filter_signals: filter_signals, defaults to None
    :type filter_signals: bool, optional
    :param outbound_document_validation: outbound_document_validation, defaults to None
    :type outbound_document_validation: bool, optional
    :param reject_duplicate_transactions: reject_duplicate_transactions, defaults to None
    :type reject_duplicate_transactions: bool, optional
    :param version: version, defaults to None
    :type version: RosettaNetOptionsVersion, optional
    """

    def __init__(
        self,
        filter_signals: bool = SENTINEL,
        outbound_document_validation: bool = SENTINEL,
        reject_duplicate_transactions: bool = SENTINEL,
        version: RosettaNetOptionsVersion = SENTINEL,
        **kwargs
    ):
        """RosettaNetOptions

        :param filter_signals: filter_signals, defaults to None
        :type filter_signals: bool, optional
        :param outbound_document_validation: outbound_document_validation, defaults to None
        :type outbound_document_validation: bool, optional
        :param reject_duplicate_transactions: reject_duplicate_transactions, defaults to None
        :type reject_duplicate_transactions: bool, optional
        :param version: version, defaults to None
        :type version: RosettaNetOptionsVersion, optional
        """
        if filter_signals is not SENTINEL:
            self.filter_signals = filter_signals
        if outbound_document_validation is not SENTINEL:
            self.outbound_document_validation = outbound_document_validation
        if reject_duplicate_transactions is not SENTINEL:
            self.reject_duplicate_transactions = reject_duplicate_transactions
        if version is not SENTINEL:
            self.version = self._enum_matching(
                version, RosettaNetOptionsVersion.list(), "version"
            )
        self._kwargs = kwargs
