
from __future__ import annotations
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .edi_delimiter import EdiDelimiter
from .edi_segment_terminator import EdiSegmentTerminator


class Acceptackoption(Enum):
    """An enumeration representing different categories.

    :cvar AL: "AL"
    :vartype AL: str
    :cvar NE: "NE"
    :vartype NE: str
    :cvar ER: "ER"
    :vartype ER: str
    :cvar SU: "SU"
    :vartype SU: str
    :cvar NOTDEFINED: "NOT_DEFINED"
    :vartype NOTDEFINED: str
    """

    AL = "AL"
    NE = "NE"
    ER = "ER"
    SU = "SU"
    NOTDEFINED = "NOT_DEFINED"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, Acceptackoption._member_map_.values()))


class Appackoption(Enum):
    """An enumeration representing different categories.

    :cvar AL: "AL"
    :vartype AL: str
    :cvar NE: "NE"
    :vartype NE: str
    :cvar ER: "ER"
    :vartype ER: str
    :cvar SU: "SU"
    :vartype SU: str
    :cvar NOTDEFINED: "NOT_DEFINED"
    :vartype NOTDEFINED: str
    """

    AL = "AL"
    NE = "NE"
    ER = "ER"
    SU = "SU"
    NOTDEFINED = "NOT_DEFINED"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, Appackoption._member_map_.values()))


class Batchoption(Enum):
    """An enumeration representing different categories.

    :cvar NONE: "none"
    :vartype NONE: str
    :cvar BATCH: "batch"
    :vartype BATCH: str
    """

    NONE = "none"
    BATCH = "batch"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, Batchoption._member_map_.values()))


class Hl7OptionsOutboundValidationOption(Enum):
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
                Hl7OptionsOutboundValidationOption._member_map_.values(),
            )
        )


@JsonMap(
    {
        "composite_delimiter": "compositeDelimiter",
        "element_delimiter": "elementDelimiter",
        "outbound_interchange_validation": "outboundInterchangeValidation",
        "outbound_validation_option": "outboundValidationOption",
        "reject_duplicates": "rejectDuplicates",
        "segment_terminator": "segmentTerminator",
        "sub_composite_delimiter": "subCompositeDelimiter",
    }
)
class Hl7Options(BaseModel):
    """Hl7Options

    :param acceptackoption: acceptackoption, defaults to None
    :type acceptackoption: Acceptackoption, optional
    :param appackoption: appackoption, defaults to None
    :type appackoption: Appackoption, optional
    :param batchoption: batchoption, defaults to None
    :type batchoption: Batchoption, optional
    :param composite_delimiter: composite_delimiter
    :type composite_delimiter: EdiDelimiter
    :param element_delimiter: element_delimiter
    :type element_delimiter: EdiDelimiter
    :param filteracknowledgements: filteracknowledgements, defaults to None
    :type filteracknowledgements: bool, optional
    :param outbound_interchange_validation: outbound_interchange_validation, defaults to None
    :type outbound_interchange_validation: bool, optional
    :param outbound_validation_option: outbound_validation_option, defaults to None
    :type outbound_validation_option: Hl7OptionsOutboundValidationOption, optional
    :param reject_duplicates: reject_duplicates, defaults to None
    :type reject_duplicates: bool, optional
    :param segment_terminator: segment_terminator
    :type segment_terminator: EdiSegmentTerminator
    :param sub_composite_delimiter: sub_composite_delimiter
    :type sub_composite_delimiter: EdiDelimiter
    """

    def __init__(
        self,
        composite_delimiter: EdiDelimiter,
        element_delimiter: EdiDelimiter,
        segment_terminator: EdiSegmentTerminator,
        sub_composite_delimiter: EdiDelimiter,
        acceptackoption: Acceptackoption = SENTINEL,
        appackoption: Appackoption = SENTINEL,
        batchoption: Batchoption = SENTINEL,
        filteracknowledgements: bool = SENTINEL,
        outbound_interchange_validation: bool = SENTINEL,
        outbound_validation_option: Hl7OptionsOutboundValidationOption = SENTINEL,
        reject_duplicates: bool = SENTINEL,
        **kwargs,
    ):
        """Hl7Options

        :param acceptackoption: acceptackoption, defaults to None
        :type acceptackoption: Acceptackoption, optional
        :param appackoption: appackoption, defaults to None
        :type appackoption: Appackoption, optional
        :param batchoption: batchoption, defaults to None
        :type batchoption: Batchoption, optional
        :param composite_delimiter: composite_delimiter
        :type composite_delimiter: EdiDelimiter
        :param element_delimiter: element_delimiter
        :type element_delimiter: EdiDelimiter
        :param filteracknowledgements: filteracknowledgements, defaults to None
        :type filteracknowledgements: bool, optional
        :param outbound_interchange_validation: outbound_interchange_validation, defaults to None
        :type outbound_interchange_validation: bool, optional
        :param outbound_validation_option: outbound_validation_option, defaults to None
        :type outbound_validation_option: Hl7OptionsOutboundValidationOption, optional
        :param reject_duplicates: reject_duplicates, defaults to None
        :type reject_duplicates: bool, optional
        :param segment_terminator: segment_terminator
        :type segment_terminator: EdiSegmentTerminator
        :param sub_composite_delimiter: sub_composite_delimiter
        :type sub_composite_delimiter: EdiDelimiter
        """
        if acceptackoption is not SENTINEL:
            self.acceptackoption = self._enum_matching(
                acceptackoption, Acceptackoption.list(), "acceptackoption"
            )
        if appackoption is not SENTINEL:
            self.appackoption = self._enum_matching(
                appackoption, Appackoption.list(), "appackoption"
            )
        if batchoption is not SENTINEL:
            self.batchoption = self._enum_matching(
                batchoption, Batchoption.list(), "batchoption"
            )
        self.composite_delimiter = self._define_object(
            composite_delimiter, EdiDelimiter
        )
        self.element_delimiter = self._define_object(element_delimiter, EdiDelimiter)
        if filteracknowledgements is not SENTINEL:
            self.filteracknowledgements = filteracknowledgements
        if outbound_interchange_validation is not SENTINEL:
            self.outbound_interchange_validation = outbound_interchange_validation
        if outbound_validation_option is not SENTINEL:
            self.outbound_validation_option = self._enum_matching(
                outbound_validation_option,
                Hl7OptionsOutboundValidationOption.list(),
                "outbound_validation_option",
            )
        if reject_duplicates is not SENTINEL:
            self.reject_duplicates = reject_duplicates
        self.segment_terminator = self._define_object(
            segment_terminator, EdiSegmentTerminator
        )
        self.sub_composite_delimiter = self._define_object(
            sub_composite_delimiter, EdiDelimiter
        )
        self._kwargs = kwargs
