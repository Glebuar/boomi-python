
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .map_extensions_cross_reference_lookup import MapExtensionsCrossReferenceLookup
from .map_extensions_doc_cache_lookup import MapExtensionsDocCacheLookup
from .map_extensions_document_property import MapExtensionsDocumentProperty
from .map_extensions_japanese_character_conversion import (
    MapExtensionsJapaneseCharacterConversion,
)
from .map_extensions_scripting import MapExtensionsScripting
from .map_extensions_sequential_value import MapExtensionsSequentialValue
from .map_extensions_simple_lookup import MapExtensionsSimpleLookup
from .map_extensions_string_concat import MapExtensionsStringConcat
from .map_extensions_string_split import MapExtensionsStringSplit
from .map_extensions_user_defined_function import MapExtensionsUserDefinedFunction


@JsonMap(
    {
        "cross_reference_lookup": "CrossReferenceLookup",
        "doc_cache_lookup": "DocCacheLookup",
        "document_property": "DocumentProperty",
        "japanese_character_conversion": "JapaneseCharacterConversion",
        "scripting": "Scripting",
        "sequential_value": "SequentialValue",
        "simple_lookup": "SimpleLookup",
        "string_concat": "StringConcat",
        "string_split": "StringSplit",
        "user_defined_function": "UserDefinedFunction",
    }
)
class MapExtensionsConfiguration(BaseModel):
    """MapExtensionsConfiguration

    :param cross_reference_lookup: cross_reference_lookup, defaults to None
    :type cross_reference_lookup: MapExtensionsCrossReferenceLookup, optional
    :param doc_cache_lookup: doc_cache_lookup, defaults to None
    :type doc_cache_lookup: MapExtensionsDocCacheLookup, optional
    :param document_property: document_property, defaults to None
    :type document_property: MapExtensionsDocumentProperty, optional
    :param japanese_character_conversion: japanese_character_conversion, defaults to None
    :type japanese_character_conversion: MapExtensionsJapaneseCharacterConversion, optional
    :param scripting: scripting, defaults to None
    :type scripting: MapExtensionsScripting, optional
    :param sequential_value: sequential_value, defaults to None
    :type sequential_value: MapExtensionsSequentialValue, optional
    :param simple_lookup: simple_lookup, defaults to None
    :type simple_lookup: MapExtensionsSimpleLookup, optional
    :param string_concat: string_concat, defaults to None
    :type string_concat: MapExtensionsStringConcat, optional
    :param string_split: string_split, defaults to None
    :type string_split: MapExtensionsStringSplit, optional
    :param user_defined_function: user_defined_function, defaults to None
    :type user_defined_function: MapExtensionsUserDefinedFunction, optional
    """

    def __init__(
        self,
        cross_reference_lookup: MapExtensionsCrossReferenceLookup = SENTINEL,
        doc_cache_lookup: MapExtensionsDocCacheLookup = SENTINEL,
        document_property: MapExtensionsDocumentProperty = SENTINEL,
        japanese_character_conversion: MapExtensionsJapaneseCharacterConversion = SENTINEL,
        scripting: MapExtensionsScripting = SENTINEL,
        sequential_value: MapExtensionsSequentialValue = SENTINEL,
        simple_lookup: MapExtensionsSimpleLookup = SENTINEL,
        string_concat: MapExtensionsStringConcat = SENTINEL,
        string_split: MapExtensionsStringSplit = SENTINEL,
        user_defined_function: MapExtensionsUserDefinedFunction = SENTINEL,
        **kwargs,
    ):
        """MapExtensionsConfiguration

        :param cross_reference_lookup: cross_reference_lookup, defaults to None
        :type cross_reference_lookup: MapExtensionsCrossReferenceLookup, optional
        :param doc_cache_lookup: doc_cache_lookup, defaults to None
        :type doc_cache_lookup: MapExtensionsDocCacheLookup, optional
        :param document_property: document_property, defaults to None
        :type document_property: MapExtensionsDocumentProperty, optional
        :param japanese_character_conversion: japanese_character_conversion, defaults to None
        :type japanese_character_conversion: MapExtensionsJapaneseCharacterConversion, optional
        :param scripting: scripting, defaults to None
        :type scripting: MapExtensionsScripting, optional
        :param sequential_value: sequential_value, defaults to None
        :type sequential_value: MapExtensionsSequentialValue, optional
        :param simple_lookup: simple_lookup, defaults to None
        :type simple_lookup: MapExtensionsSimpleLookup, optional
        :param string_concat: string_concat, defaults to None
        :type string_concat: MapExtensionsStringConcat, optional
        :param string_split: string_split, defaults to None
        :type string_split: MapExtensionsStringSplit, optional
        :param user_defined_function: user_defined_function, defaults to None
        :type user_defined_function: MapExtensionsUserDefinedFunction, optional
        """
        if cross_reference_lookup is not SENTINEL:
            self.cross_reference_lookup = self._define_object(
                cross_reference_lookup, MapExtensionsCrossReferenceLookup
            )
        if doc_cache_lookup is not SENTINEL:
            self.doc_cache_lookup = self._define_object(
                doc_cache_lookup, MapExtensionsDocCacheLookup
            )
        if document_property is not SENTINEL:
            self.document_property = self._define_object(
                document_property, MapExtensionsDocumentProperty
            )
        if japanese_character_conversion is not SENTINEL:
            self.japanese_character_conversion = self._define_object(
                japanese_character_conversion, MapExtensionsJapaneseCharacterConversion
            )
        if scripting is not SENTINEL:
            self.scripting = self._define_object(scripting, MapExtensionsScripting)
        if sequential_value is not SENTINEL:
            self.sequential_value = self._define_object(
                sequential_value, MapExtensionsSequentialValue
            )
        if simple_lookup is not SENTINEL:
            self.simple_lookup = self._define_object(
                simple_lookup, MapExtensionsSimpleLookup
            )
        if string_concat is not SENTINEL:
            self.string_concat = self._define_object(
                string_concat, MapExtensionsStringConcat
            )
        if string_split is not SENTINEL:
            self.string_split = self._define_object(
                string_split, MapExtensionsStringSplit
            )
        if user_defined_function is not SENTINEL:
            self.user_defined_function = self._define_object(
                user_defined_function, MapExtensionsUserDefinedFunction
            )
        self._kwargs = kwargs
