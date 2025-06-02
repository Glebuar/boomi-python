
from __future__ import annotations
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .edi_delimiter import EdiDelimiter
from .edi_segment_terminator import EdiSegmentTerminator


class OdetteOptionsAcknowledgementoption(Enum):
    """An enumeration representing different categories.

    :cvar DONOTACKITEM: "donotackitem"
    :vartype DONOTACKITEM: str
    :cvar ACKITEM: "ackitem"
    :vartype ACKITEM: str
    """

    DONOTACKITEM = "donotackitem"
    ACKITEM = "ackitem"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                OdetteOptionsAcknowledgementoption._member_map_.values(),
            )
        )


class OdetteOptionsEnvelopeoption(Enum):
    """An enumeration representing different categories.

    :cvar GROUPALL: "groupall"
    :vartype GROUPALL: str
    :cvar GROUPMESSAGE: "groupmessage"
    :vartype GROUPMESSAGE: str
    """

    GROUPALL = "groupall"
    GROUPMESSAGE = "groupmessage"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, OdetteOptionsEnvelopeoption._member_map_.values())
        )


class OdetteOptionsOutboundValidationOption(Enum):
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
                OdetteOptionsOutboundValidationOption._member_map_.values(),
            )
        )


@JsonMap(
    {
        "composite_delimiter": "compositeDelimiter",
        "element_delimiter": "elementDelimiter",
        "include_una": "includeUNA",
        "outbound_interchange_validation": "outboundInterchangeValidation",
        "outbound_validation_option": "outboundValidationOption",
        "reject_duplicate_unb": "rejectDuplicateUNB",
        "segment_terminator": "segmentTerminator",
    }
)
class OdetteOptions(BaseModel):
    """OdetteOptions

    :param acknowledgementoption: acknowledgementoption, defaults to None
    :type acknowledgementoption: OdetteOptionsAcknowledgementoption, optional
    :param composite_delimiter: composite_delimiter
    :type composite_delimiter: EdiDelimiter
    :param element_delimiter: element_delimiter
    :type element_delimiter: EdiDelimiter
    :param envelopeoption: envelopeoption, defaults to None
    :type envelopeoption: OdetteOptionsEnvelopeoption, optional
    :param filteracknowledgements: filteracknowledgements, defaults to None
    :type filteracknowledgements: bool, optional
    :param include_una: include_una, defaults to None
    :type include_una: bool, optional
    :param outbound_interchange_validation: outbound_interchange_validation, defaults to None
    :type outbound_interchange_validation: bool, optional
    :param outbound_validation_option: outbound_validation_option, defaults to None
    :type outbound_validation_option: OdetteOptionsOutboundValidationOption, optional
    :param reject_duplicate_unb: reject_duplicate_unb, defaults to None
    :type reject_duplicate_unb: bool, optional
    :param segment_terminator: segment_terminator
    :type segment_terminator: EdiSegmentTerminator
    """

    def __init__(
        self,
        composite_delimiter: EdiDelimiter,
        element_delimiter: EdiDelimiter,
        segment_terminator: EdiSegmentTerminator,
        acknowledgementoption: OdetteOptionsAcknowledgementoption = SENTINEL,
        envelopeoption: OdetteOptionsEnvelopeoption = SENTINEL,
        filteracknowledgements: bool = SENTINEL,
        include_una: bool = SENTINEL,
        outbound_interchange_validation: bool = SENTINEL,
        outbound_validation_option: OdetteOptionsOutboundValidationOption = SENTINEL,
        reject_duplicate_unb: bool = SENTINEL,
        **kwargs,
    ):
        """OdetteOptions

        :param acknowledgementoption: acknowledgementoption, defaults to None
        :type acknowledgementoption: OdetteOptionsAcknowledgementoption, optional
        :param composite_delimiter: composite_delimiter
        :type composite_delimiter: EdiDelimiter
        :param element_delimiter: element_delimiter
        :type element_delimiter: EdiDelimiter
        :param envelopeoption: envelopeoption, defaults to None
        :type envelopeoption: OdetteOptionsEnvelopeoption, optional
        :param filteracknowledgements: filteracknowledgements, defaults to None
        :type filteracknowledgements: bool, optional
        :param include_una: include_una, defaults to None
        :type include_una: bool, optional
        :param outbound_interchange_validation: outbound_interchange_validation, defaults to None
        :type outbound_interchange_validation: bool, optional
        :param outbound_validation_option: outbound_validation_option, defaults to None
        :type outbound_validation_option: OdetteOptionsOutboundValidationOption, optional
        :param reject_duplicate_unb: reject_duplicate_unb, defaults to None
        :type reject_duplicate_unb: bool, optional
        :param segment_terminator: segment_terminator
        :type segment_terminator: EdiSegmentTerminator
        """
        if acknowledgementoption is not SENTINEL:
            self.acknowledgementoption = self._enum_matching(
                acknowledgementoption,
                OdetteOptionsAcknowledgementoption.list(),
                "acknowledgementoption",
            )
        self.composite_delimiter = self._define_object(
            composite_delimiter, EdiDelimiter
        )
        self.element_delimiter = self._define_object(element_delimiter, EdiDelimiter)
        if envelopeoption is not SENTINEL:
            self.envelopeoption = self._enum_matching(
                envelopeoption, OdetteOptionsEnvelopeoption.list(), "envelopeoption"
            )
        if filteracknowledgements is not SENTINEL:
            self.filteracknowledgements = filteracknowledgements
        if include_una is not SENTINEL:
            self.include_una = include_una
        if outbound_interchange_validation is not SENTINEL:
            self.outbound_interchange_validation = outbound_interchange_validation
        if outbound_validation_option is not SENTINEL:
            self.outbound_validation_option = self._enum_matching(
                outbound_validation_option,
                OdetteOptionsOutboundValidationOption.list(),
                "outbound_validation_option",
            )
        if reject_duplicate_unb is not SENTINEL:
            self.reject_duplicate_unb = reject_duplicate_unb
        self.segment_terminator = self._define_object(
            segment_terminator, EdiSegmentTerminator
        )
        self._kwargs = kwargs
