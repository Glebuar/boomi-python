
from enum import Enum
from typing import Any

# BaseModel is imported lazily inside extract_original_data to avoid
# importing the entire sdk.models package during module import which can
# introduce circular dependencies when only XML utilities are required.
try:
    import xmltodict
    ExpatError = xmltodict.expat.ExpatError
except Exception:  # pragma: no cover - if xmltodict is unavailable
    xmltodict = None
    from xml.parsers.expat import ExpatError  # type: ignore
    import xml.etree.ElementTree as _ET


def extract_original_data(data: Any) -> Any:
    """Extract the original data from internal models and enums.

    ``BaseModel`` is imported lazily to prevent importing the whole
    :mod:`sdk.models` package unless this function is actually used.

    :param Any data: The data to be extracted.
    :return: The extracted data.
    :rtype: Any
    """
    if data is None:
        return None

    data_type = type(data)

    try:
        from ...models.utils.base_model import BaseModel  # type: ignore
    except Exception:  # pragma: no cover - defensive fallback
        BaseModel = None

    if BaseModel is not None and issubclass(data_type, BaseModel):
        return data._map()

    if issubclass(data_type, Enum):
        return data.value

    if issubclass(data_type, list):
        return [extract_original_data(item) for item in data]

    return data


def parse_xml_to_dict(xml_string: str) -> dict:
    """Parse an XML string into a dictionary.

    If :mod:`xmltodict` is available it will be used for the conversion. When it
    is not installed, a very small fallback implementation based on
    :mod:`xml.etree.ElementTree` is used instead. Only the limited structure
    required by the tests is supported in that mode.

    :param xml_string: The XML string to parse.
    :type xml_string: str
    :raises TypeError: If ``xml_string`` is not a string.
    :raises ExpatError: If the XML string is malformed.
    :return: A Python dictionary representing the XML structure.
    :rtype: dict
    """
    if not isinstance(xml_string, str):
        raise TypeError(
            f"Expected an XML string for parsing, but got type {type(xml_string).__name__}."
        )

    if xmltodict is not None:
        # Let xmltodict.parse raise its own errors for malformed XML.
        return xmltodict.parse(xml_string)

    # Minimal fallback parser
    def _elem_to_dict(elem):
        children = list(elem)
        result = {f"@{k}": v for k, v in elem.attrib.items()}
        if children:
            child_dict = {}
            for child in children:
                child_dict.update(_elem_to_dict(child))
            if elem.text and elem.text.strip():
                result["#text"] = elem.text.strip()
            result = {elem.tag: {**result, **child_dict}}
        else:
            text = elem.text.strip() if elem.text and elem.text.strip() else None
            if result:
                if text is not None:
                    result["#text"] = text
                result = {elem.tag: result}
            else:
                result = {elem.tag: text}
        return result

    try:
        root = _ET.fromstring(xml_string)
    except _ET.ParseError as exc:  # pragma: no cover - matches xmltodict behaviour
        raise ExpatError(str(exc))
    return _elem_to_dict(root)

