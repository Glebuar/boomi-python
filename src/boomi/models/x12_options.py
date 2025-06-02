
from __future__ import annotations
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .edi_delimiter import EdiDelimiter
from .edi_segment_terminator import EdiSegmentTerminator


class X12OptionsAcknowledgementoption(Enum):
    """An enumeration representing different categories.

    :cvar DONOTACKITEM: "donotackitem"
    :vartype DONOTACKITEM: str
    :cvar ACKFUNCITEM: "ackfuncitem"
    :vartype ACKFUNCITEM: str
    :cvar ACKTRANITEM: "acktranitem"
    :vartype ACKTRANITEM: str
    """

    DONOTACKITEM = "donotackitem"
    ACKFUNCITEM = "ackfuncitem"
    ACKTRANITEM = "acktranitem"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value, X12OptionsAcknowledgementoption._member_map_.values()
            )
        )


class X12OptionsEnvelopeoption(Enum):
    """An enumeration representing different categories.

    :cvar GROUPALL: "groupall"
    :vartype GROUPALL: str
    :cvar GROUPFG: "groupfg"
    :vartype GROUPFG: str
    :cvar GROUPST: "groupst"
    :vartype GROUPST: str
    """

    GROUPALL = "groupall"
    GROUPFG = "groupfg"
    GROUPST = "groupst"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, X12OptionsEnvelopeoption._member_map_.values())
        )


class X12OptionsOutboundValidationOption(Enum):
    """An enumeration representing different categories.

    :cvar FILTERERROR: "filterError"
    :vartype FILTERERROR: str
    :cvar FAILALL: "failAll"
    :vartype FAILALL: str
    """

    FILTERERROR = "filterError"
    FAILALL = "failAll"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                X12OptionsOutboundValidationOption._member_map_.values(),
            )
        )


@JsonMap(
    {
        "element_delimiter": "elementDelimiter",
        "outbound_interchange_validation": "outboundInterchangeValidation",
        "outbound_validation_option": "outboundValidationOption",
        "reject_duplicate_interchange": "rejectDuplicateInterchange",
        "segment_terminator": "segmentTerminator",
    }
)
class X12Options(BaseModel):
    """X12Options

    :param acknowledgementoption: acknowledgementoption, defaults to None
    :type acknowledgementoption: X12OptionsAcknowledgementoption, optional
    :param element_delimiter: element_delimiter
    :type element_delimiter: EdiDelimiter
    :param envelopeoption: envelopeoption, defaults to None
    :type envelopeoption: X12OptionsEnvelopeoption, optional
    :param filteracknowledgements: filteracknowledgements, defaults to None
    :type filteracknowledgements: bool, optional
    :param outbound_interchange_validation: outbound_interchange_validation, defaults to None
    :type outbound_interchange_validation: bool, optional
    :param outbound_validation_option: outbound_validation_option, defaults to None
    :type outbound_validation_option: X12OptionsOutboundValidationOption, optional
    :param reject_duplicate_interchange: reject_duplicate_interchange, defaults to None
    :type reject_duplicate_interchange: bool, optional
    :param segment_terminator: segment_terminator
    :type segment_terminator: EdiSegmentTerminator
    """

    def __init__(
        self,
        element_delimiter: EdiDelimiter,
        segment_terminator: EdiSegmentTerminator,
        acknowledgementoption: X12OptionsAcknowledgementoption = SENTINEL,
        envelopeoption: X12OptionsEnvelopeoption = SENTINEL,
        filteracknowledgements: bool = SENTINEL,
        outbound_interchange_validation: bool = SENTINEL,
        outbound_validation_option: X12OptionsOutboundValidationOption = SENTINEL,
        reject_duplicate_interchange: bool = SENTINEL,
        **kwargs,
    ):
        """X12Options

        :param acknowledgementoption: acknowledgementoption, defaults to None
        :type acknowledgementoption: X12OptionsAcknowledgementoption, optional
        :param element_delimiter: element_delimiter
        :type element_delimiter: EdiDelimiter
        :param envelopeoption: envelopeoption, defaults to None
        :type envelopeoption: X12OptionsEnvelopeoption, optional
        :param filteracknowledgements: filteracknowledgements, defaults to None
        :type filteracknowledgements: bool, optional
        :param outbound_interchange_validation: outbound_interchange_validation, defaults to None
        :type outbound_interchange_validation: bool, optional
        :param outbound_validation_option: outbound_validation_option, defaults to None
        :type outbound_validation_option: X12OptionsOutboundValidationOption, optional
        :param reject_duplicate_interchange: reject_duplicate_interchange, defaults to None
        :type reject_duplicate_interchange: bool, optional
        :param segment_terminator: segment_terminator
        :type segment_terminator: EdiSegmentTerminator
        """
        if acknowledgementoption is not SENTINEL:
            self.acknowledgementoption = self._enum_matching(
                acknowledgementoption,
                X12OptionsAcknowledgementoption.list(),
                "acknowledgementoption",
            )
        self.element_delimiter = self._define_object(element_delimiter, EdiDelimiter)
        if envelopeoption is not SENTINEL:
            self.envelopeoption = self._enum_matching(
                envelopeoption, X12OptionsEnvelopeoption.list(), "envelopeoption"
            )
        if filteracknowledgements is not SENTINEL:
            self.filteracknowledgements = filteracknowledgements
        if outbound_interchange_validation is not SENTINEL:
            self.outbound_interchange_validation = outbound_interchange_validation
        if outbound_validation_option is not SENTINEL:
            self.outbound_validation_option = self._enum_matching(
                outbound_validation_option,
                X12OptionsOutboundValidationOption.list(),
                "outbound_validation_option",
            )
        if reject_duplicate_interchange is not SENTINEL:
            self.reject_duplicate_interchange = reject_duplicate_interchange
        self.segment_terminator = self._define_object(
            segment_terminator, EdiSegmentTerminator
        )
        self._kwargs = kwargs
