
from __future__ import annotations
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .map_extensions_configuration import MapExtensionsConfiguration
from .map_extensions_inputs import MapExtensionsInputs
from .map_extensions_outputs import MapExtensionsOutputs


class MapExtensionsFunctionCacheType(Enum):
    """An enumeration representing different categories.

    :cvar NONE: "None"
    :vartype NONE: str
    :cvar BYDOCUMENT: "ByDocument"
    :vartype BYDOCUMENT: str
    :cvar BYMAP: "ByMap"
    :vartype BYMAP: str
    """

    NONE = "None"
    BYDOCUMENT = "ByDocument"
    BYMAP = "ByMap"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, MapExtensionsFunctionCacheType._member_map_.values())
        )


class MapExtensionsFunctionType(Enum):
    """An enumeration representing different categories.

    :cvar COUNT: "Count"
    :vartype COUNT: str
    :cvar CURRENTDATE: "CurrentDate"
    :vartype CURRENTDATE: str
    :cvar DATEFORMAT: "DateFormat"
    :vartype DATEFORMAT: str
    :cvar LEFTTRIM: "LeftTrim"
    :vartype LEFTTRIM: str
    :cvar LINEITEMINCREMENT: "LineItemIncrement"
    :vartype LINEITEMINCREMENT: str
    :cvar MATHABS: "MathABS"
    :vartype MATHABS: str
    :cvar MATHADD: "MathAdd"
    :vartype MATHADD: str
    :cvar MATHCEIL: "MathCeil"
    :vartype MATHCEIL: str
    :cvar MATHDIVIDE: "MathDivide"
    :vartype MATHDIVIDE: str
    :cvar MATHFLOOR: "MathFloor"
    :vartype MATHFLOOR: str
    :cvar MATHMULTIPLY: "MathMultiply"
    :vartype MATHMULTIPLY: str
    :cvar MATHSETPRECISION: "MathSetPrecision"
    :vartype MATHSETPRECISION: str
    :cvar MATHSUBTRACT: "MathSubtract"
    :vartype MATHSUBTRACT: str
    :cvar NUMBERFORMAT: "NumberFormat"
    :vartype NUMBERFORMAT: str
    :cvar PROPERTYGET: "PropertyGet"
    :vartype PROPERTYGET: str
    :cvar PROPERTYSET: "PropertySet"
    :vartype PROPERTYSET: str
    :cvar RIGHTTRIM: "RightTrim"
    :vartype RIGHTTRIM: str
    :cvar RUNNINGTOTAL: "RunningTotal"
    :vartype RUNNINGTOTAL: str
    :cvar STRINGAPPEND: "StringAppend"
    :vartype STRINGAPPEND: str
    :cvar STRINGPREPEND: "StringPrepend"
    :vartype STRINGPREPEND: str
    :cvar STRINGREMOVE: "StringRemove"
    :vartype STRINGREMOVE: str
    :cvar STRINGREPLACE: "StringReplace"
    :vartype STRINGREPLACE: str
    :cvar STRINGTOLOWER: "StringToLower"
    :vartype STRINGTOLOWER: str
    :cvar STRINGTOUPPER: "StringToUpper"
    :vartype STRINGTOUPPER: str
    :cvar SUM: "Sum"
    :vartype SUM: str
    :cvar TRIMWHITESPACE: "TrimWhitespace"
    :vartype TRIMWHITESPACE: str
    :cvar STRINGCONCAT: "StringConcat"
    :vartype STRINGCONCAT: str
    :cvar STRINGSPLIT: "StringSplit"
    :vartype STRINGSPLIT: str
    :cvar SEQUENTIALVALUE: "SequentialValue"
    :vartype SEQUENTIALVALUE: str
    :cvar SIMPLELOOKUP: "SimpleLookup"
    :vartype SIMPLELOOKUP: str
    :cvar DOCUMENTPROPERTYGET: "DocumentPropertyGet"
    :vartype DOCUMENTPROPERTYGET: str
    :cvar DOCUMENTPROPERTYSET: "DocumentPropertySet"
    :vartype DOCUMENTPROPERTYSET: str
    :cvar CROSSREFLOOKUP: "CrossRefLookup"
    :vartype CROSSREFLOOKUP: str
    :cvar DOCUMENTCACHELOOKUP: "DocumentCacheLookup"
    :vartype DOCUMENTCACHELOOKUP: str
    :cvar CUSTOMSCRIPTING: "CustomScripting"
    :vartype CUSTOMSCRIPTING: str
    :cvar USERDEFINED: "UserDefined"
    :vartype USERDEFINED: str
    :cvar JAPANESECHARACTERCONVERSION: "JapaneseCharacterConversion"
    :vartype JAPANESECHARACTERCONVERSION: str
    """

    COUNT = "Count"
    CURRENTDATE = "CurrentDate"
    DATEFORMAT = "DateFormat"
    LEFTTRIM = "LeftTrim"
    LINEITEMINCREMENT = "LineItemIncrement"
    MATHABS = "MathABS"
    MATHADD = "MathAdd"
    MATHCEIL = "MathCeil"
    MATHDIVIDE = "MathDivide"
    MATHFLOOR = "MathFloor"
    MATHMULTIPLY = "MathMultiply"
    MATHSETPRECISION = "MathSetPrecision"
    MATHSUBTRACT = "MathSubtract"
    NUMBERFORMAT = "NumberFormat"
    PROPERTYGET = "PropertyGet"
    PROPERTYSET = "PropertySet"
    RIGHTTRIM = "RightTrim"
    RUNNINGTOTAL = "RunningTotal"
    STRINGAPPEND = "StringAppend"
    STRINGPREPEND = "StringPrepend"
    STRINGREMOVE = "StringRemove"
    STRINGREPLACE = "StringReplace"
    STRINGTOLOWER = "StringToLower"
    STRINGTOUPPER = "StringToUpper"
    SUM = "Sum"
    TRIMWHITESPACE = "TrimWhitespace"
    STRINGCONCAT = "StringConcat"
    STRINGSPLIT = "StringSplit"
    SEQUENTIALVALUE = "SequentialValue"
    SIMPLELOOKUP = "SimpleLookup"
    DOCUMENTPROPERTYGET = "DocumentPropertyGet"
    DOCUMENTPROPERTYSET = "DocumentPropertySet"
    CROSSREFLOOKUP = "CrossRefLookup"
    DOCUMENTCACHELOOKUP = "DocumentCacheLookup"
    CUSTOMSCRIPTING = "CustomScripting"
    USERDEFINED = "UserDefined"
    JAPANESECHARACTERCONVERSION = "JapaneseCharacterConversion"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, MapExtensionsFunctionType._member_map_.values())
        )


@JsonMap(
    {
        "configuration": "Configuration",
        "inputs": "Inputs",
        "outputs": "Outputs",
        "cache_type": "cacheType",
        "id_": "id",
        "type_": "type",
    }
)
class MapExtensionsFunction(BaseModel):
    """MapExtensionsFunction

    :param configuration: configuration
    :type configuration: MapExtensionsConfiguration
    :param inputs: Lists the function's input and outputs according to their user-given names and keys. You must list inputs and outputs sequentially in order according to their key values. When creating or updating functions, it requires all input and output values in the request regardless if they are to be mapped or populated with a default value.   The maximum number of inputs or outputs is 100.
    :type inputs: MapExtensionsInputs
    :param outputs: Lists the function's input and outputs according to their user-given names and keys. You must list inputs and outputs sequentially in order according to their key values. See the following row for more information. When creating or updating functions, it requires all input and output values in the request regardless if they are to be mapped or populated with a default value.   The maximum number of inputs or outputs is 100.
    :type outputs: MapExtensionsOutputs
    :param cache_type: cache_type, defaults to None
    :type cache_type: MapExtensionsFunctionCacheType, optional
    :param id_: id_, defaults to None
    :type id_: str, optional
    :param type_: type_, defaults to None
    :type type_: MapExtensionsFunctionType, optional
    """

    def __init__(
        self,
        configuration: MapExtensionsConfiguration,
        inputs: MapExtensionsInputs,
        outputs: MapExtensionsOutputs,
        cache_type: MapExtensionsFunctionCacheType = SENTINEL,
        id_: str = SENTINEL,
        type_: MapExtensionsFunctionType = SENTINEL,
        **kwargs,
    ):
        """MapExtensionsFunction

        :param configuration: configuration
        :type configuration: MapExtensionsConfiguration
        :param inputs: Lists the function's input and outputs according to their user-given names and keys. You must list inputs and outputs sequentially in order according to their key values. When creating or updating functions, it requires all input and output values in the request regardless if they are to be mapped or populated with a default value.   The maximum number of inputs or outputs is 100.
        :type inputs: MapExtensionsInputs
        :param outputs: Lists the function's input and outputs according to their user-given names and keys. You must list inputs and outputs sequentially in order according to their key values. See the following row for more information. When creating or updating functions, it requires all input and output values in the request regardless if they are to be mapped or populated with a default value.   The maximum number of inputs or outputs is 100.
        :type outputs: MapExtensionsOutputs
        :param cache_type: cache_type, defaults to None
        :type cache_type: MapExtensionsFunctionCacheType, optional
        :param id_: id_, defaults to None
        :type id_: str, optional
        :param type_: type_, defaults to None
        :type type_: MapExtensionsFunctionType, optional
        """
        self.configuration = self._define_object(
            configuration, MapExtensionsConfiguration
        )
        self.inputs = self._define_object(inputs, MapExtensionsInputs)
        self.outputs = self._define_object(outputs, MapExtensionsOutputs)
        if cache_type is not SENTINEL:
            self.cache_type = self._enum_matching(
                cache_type, MapExtensionsFunctionCacheType.list(), "cache_type"
            )
        if id_ is not SENTINEL:
            self.id_ = id_
        if type_ is not SENTINEL:
            self.type_ = self._enum_matching(
                type_, MapExtensionsFunctionType.list(), "type_"
            )
        self._kwargs = kwargs
