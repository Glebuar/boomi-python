
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


def _remove_namespaces(obj):
    """Recursively remove XML namespaces from dictionary keys.
    
    Converts keys like '{http://namespace}elementName' to 'elementName'.
    Handles nested dictionaries, lists, and preserves data structure.
    
    :param obj: The object to process (dict, list, or other)
    :return: Object with namespaces removed from dictionary keys
    """
    if isinstance(obj, dict):
        cleaned_dict = {}
        for key, value in obj.items():
            # Remove namespace from key: {namespace}name -> name
            if isinstance(key, str) and key.startswith('{') and '}' in key:
                # Extract the local name after the namespace
                clean_key = key.split('}', 1)[1]
            else:
                clean_key = key
            
            # Recursively clean the value
            cleaned_dict[clean_key] = _remove_namespaces(value)
        return cleaned_dict
    elif isinstance(obj, list):
        # Recursively clean list items
        return [_remove_namespaces(item) for item in obj]
    else:
        # Return primitive values unchanged
        return obj


def _extract_component_data(parsed_dict):
    """Extract API response data from root wrapper and normalize attribute keys.

    Handles API responses by:
    1. Extracting data from root elements (Component, QueryResult, PackagedComponent, etc.)
    2. Converting '@attributeName' keys to 'attributeName'
    3. Preserving nested structure for object, encryptedValues, result, etc.
    4. Handling empty xsi:type elements (empty async operation results)

    :param parsed_dict: Dictionary from XML parsing with namespaces removed
    :return: Data ready for JsonMap processing
    """
    # Check if this is an AsyncOperationResult response
    if 'AsyncOperationResult' in parsed_dict:
        async_result_data = parsed_dict['AsyncOperationResult']
        if isinstance(async_result_data, dict):
            normalized_data = _normalize_attribute_keys(async_result_data)

            # Special handling for empty result elements with xsi:type attribute
            # When <bns:result xsi:type="bns:SomeType"/> is empty, treat as None/empty
            if 'result' in normalized_data and isinstance(normalized_data['result'], dict):
                result_dict = normalized_data['result']
                # If result only contains a 'type' key, it's an empty element - treat as None
                if list(result_dict.keys()) == ['type']:
                    normalized_data['result'] = None

            return normalized_data

    # Check if this is a Component response
    if 'Component' in parsed_dict:
        component_data = parsed_dict['Component']
        if isinstance(component_data, dict):
            return _normalize_attribute_keys(component_data)
    
    # Check if this is a QueryResult response (ExecutionRecord, etc.)
    elif 'QueryResult' in parsed_dict:
        query_result_data = parsed_dict['QueryResult']
        if isinstance(query_result_data, dict):
            normalized_data = _normalize_attribute_keys(query_result_data)

            # Special handling for QueryResult: ensure 'result' is always a list
            # The API returns a single dict when there's one result, but models expect a list
            if 'result' in normalized_data and not isinstance(normalized_data['result'], list):
                normalized_data['result'] = [normalized_data['result']]

            # Special handling for ProcessSchedules in QueryResult
            # Each ProcessSchedules result may have a Schedule field that needs to be a list
            if 'result' in normalized_data and isinstance(normalized_data['result'], list):
                for item in normalized_data['result']:
                    if isinstance(item, dict) and 'Schedule' in item:
                        if not isinstance(item['Schedule'], list):
                            item['Schedule'] = [item['Schedule']]

            return normalized_data
    
    # Check if this is a LogDownload response (ExecutionArtifacts)
    elif 'LogDownload' in parsed_dict:
        log_download_data = parsed_dict['LogDownload']
        if isinstance(log_download_data, dict):
            return _normalize_attribute_keys(log_download_data)

    # Check if this is a ProcessSchedules response
    elif 'ProcessSchedules' in parsed_dict:
        process_schedules_data = parsed_dict['ProcessSchedules']
        if isinstance(process_schedules_data, dict):
            normalized_data = _normalize_attribute_keys(process_schedules_data)

            # Special handling for ProcessSchedules: ensure 'Schedule' is always a list
            # The API returns a single dict when there's one schedule, but models expect a list
            if 'Schedule' in normalized_data and not isinstance(normalized_data['Schedule'], list):
                normalized_data['Schedule'] = [normalized_data['Schedule']]

            return normalized_data

    # Generic handling for other model types (PackagedComponent, Environment, etc.)
    # If the dict has a single key that looks like a model name (PascalCase),
    # extract its content and normalize
    if len(parsed_dict) == 1:
        root_key = list(parsed_dict.keys())[0]
        # Check if it looks like a model name (starts with uppercase)
        if root_key and root_key[0].isupper():
            inner_data = parsed_dict[root_key]
            if isinstance(inner_data, dict):
                return _normalize_attribute_keys(inner_data)
    
    # For other responses, return as-is
    return parsed_dict


def _normalize_attribute_keys(data_dict):
    """Normalize XML attribute keys for JsonMap compatibility.

    Converts '@attributeName' keys to 'attributeName' recursively.
    Also removes namespaces from attribute keys (e.g., '@{namespace}attr' -> 'attr').

    :param data_dict: Dictionary with potential XML attribute keys
    :return: Dictionary with normalized keys
    """
    if not isinstance(data_dict, dict):
        return data_dict

    normalized_data = {}

    for key, value in data_dict.items():
        # Convert @attributeName to attributeName for JsonMap compatibility
        if isinstance(key, str) and key.startswith('@'):
            clean_key = key[1:]  # Remove @ prefix
            # Also remove namespace if present: {namespace}name -> name
            if clean_key.startswith('{') and '}' in clean_key:
                clean_key = clean_key.split('}', 1)[1]
        else:
            clean_key = key

        # Recursively normalize nested dictionaries
        if isinstance(value, dict):
            normalized_data[clean_key] = _normalize_attribute_keys(value)
        elif isinstance(value, list):
            # Handle lists that might contain dictionaries
            normalized_data[clean_key] = [
                _normalize_attribute_keys(item) if isinstance(item, dict) else item
                for item in value
            ]
        else:
            normalized_data[clean_key] = value

    return normalized_data


def parse_xml_to_dict(xml_string: str) -> dict:
    """Parse an XML string into a dictionary.

    If :mod:`xmltodict` is available it will be used for the conversion with
    force_list parameter to handle duplicate XML elements correctly. When it
    is not installed, a fallback implementation based on
    :mod:`xml.etree.ElementTree` is used that properly handles duplicate elements.

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
        # Use force_list to ensure duplicate XML elements are converted to lists
        # Common Boomi API elements that may appear multiple times
        force_list_elements = [
            'shape', 'property', 'step', 'connection', 'component', 'item',
            'element', 'field', 'parameter', 'value', 'node', 'entry', 'Schedule'
        ]
        # Let xmltodict.parse raise its own errors for malformed XML.
        parsed = xmltodict.parse(xml_string, force_list=force_list_elements)
        
        # Remove namespaces and extract Component data for JsonMap compatibility
        cleaned = _remove_namespaces(parsed)
        return _extract_component_data(cleaned)

    # Enhanced fallback parser that handles duplicate elements correctly
    def _elem_to_dict(elem):
        children = list(elem)
        result = {f"@{k}": v for k, v in elem.attrib.items()}
        if children:
            child_dict = {}
            # Track element names to detect duplicates
            element_counts = {}
            
            for child in children:
                child_result = _elem_to_dict(child)
                child_tag = child.tag
                child_data = child_result[child_tag]
                
                # Count occurrences of this element name
                element_counts[child_tag] = element_counts.get(child_tag, 0) + 1
                
                if child_tag in child_dict:
                    # Convert to list if we encounter a duplicate
                    if not isinstance(child_dict[child_tag], list):
                        child_dict[child_tag] = [child_dict[child_tag]]
                    child_dict[child_tag].append(child_data)
                else:
                    child_dict[child_tag] = child_data
            
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
    
    # Parse with fallback parser and apply namespace/Component processing
    parsed = _elem_to_dict(root)
    cleaned = _remove_namespaces(parsed)
    return _extract_component_data(cleaned)


def parse_xml_to_dict_with_preservation(xml_string: str) -> dict:
    """Parse XML to dict while preserving original XML for round-tripping.
    
    This function works like parse_xml_to_dict but also stores the original
    XML and object element for perfect round-trip preservation. Used by
    Component model to enable lossless XML updates.
    
    :param xml_string: The XML string to parse
    :type xml_string: str
    :return: Dict with additional XML preservation fields
    :rtype: dict
    """
    from xml.etree import ElementTree as ET
    
    # First, do the normal parsing for backward compatibility
    result = parse_xml_to_dict(xml_string)
    
    # Now add XML preservation data
    try:
        root = ET.fromstring(xml_string)
        
        # Store the original XML
        result['_original_xml'] = xml_string
        
        # Extract and store the object element as raw XML
        ns = "http://api.platform.boomi.com/"
        obj_elem = root.find(f"{{{ns}}}object")
        if obj_elem is not None:
            # Store the inner XML (the content inside <bns:object>)
            inner_xml = ""
            for child in obj_elem:
                inner_xml += ET.tostring(child, encoding='unicode')
            result['object_xml'] = inner_xml
            result['_object_element'] = obj_elem
        
    except ET.ParseError:
        # If XML parsing fails, just use the regular result
        pass
    
    return result

