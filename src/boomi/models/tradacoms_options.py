
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .edi_delimiter import EdiDelimiter
from .edi_segment_terminator import EdiSegmentTerminator


@JsonMap(
    {
        "composite_delimiter": "compositeDelimiter",
        "element_delimiter": "elementDelimiter",
        "filter_acknowledgements": "filterAcknowledgements",
        "segment_terminator": "segmentTerminator",
        "use_reconciliation_message": "useReconciliationMessage",
    }
)
class TradacomsOptions(BaseModel):
    """TradacomsOptions

    :param composite_delimiter: composite_delimiter, defaults to None
    :type composite_delimiter: EdiDelimiter, optional
    :param element_delimiter: element_delimiter, defaults to None
    :type element_delimiter: EdiDelimiter, optional
    :param filter_acknowledgements: filter_acknowledgements, defaults to None
    :type filter_acknowledgements: bool, optional
    :param segment_terminator: segment_terminator, defaults to None
    :type segment_terminator: EdiSegmentTerminator, optional
    :param use_reconciliation_message: use_reconciliation_message, defaults to None
    :type use_reconciliation_message: bool, optional
    """

    def __init__(
        self,
        composite_delimiter: EdiDelimiter = SENTINEL,
        element_delimiter: EdiDelimiter = SENTINEL,
        filter_acknowledgements: bool = SENTINEL,
        segment_terminator: EdiSegmentTerminator = SENTINEL,
        use_reconciliation_message: bool = SENTINEL,
        **kwargs,
    ):
        """TradacomsOptions

        :param composite_delimiter: composite_delimiter, defaults to None
        :type composite_delimiter: EdiDelimiter, optional
        :param element_delimiter: element_delimiter, defaults to None
        :type element_delimiter: EdiDelimiter, optional
        :param filter_acknowledgements: filter_acknowledgements, defaults to None
        :type filter_acknowledgements: bool, optional
        :param segment_terminator: segment_terminator, defaults to None
        :type segment_terminator: EdiSegmentTerminator, optional
        :param use_reconciliation_message: use_reconciliation_message, defaults to None
        :type use_reconciliation_message: bool, optional
        """
        if composite_delimiter is not SENTINEL:
            self.composite_delimiter = self._define_object(
                composite_delimiter, EdiDelimiter
            )
        if element_delimiter is not SENTINEL:
            self.element_delimiter = self._define_object(
                element_delimiter, EdiDelimiter
            )
        if filter_acknowledgements is not SENTINEL:
            self.filter_acknowledgements = filter_acknowledgements
        if segment_terminator is not SENTINEL:
            self.segment_terminator = self._define_object(
                segment_terminator, EdiSegmentTerminator
            )
        if use_reconciliation_message is not SENTINEL:
            self.use_reconciliation_message = use_reconciliation_message
        self._kwargs = kwargs
