# EnvironmentMapExtensionService

A list of all methods in the `EnvironmentMapExtensionService` service. Click on the method name to view detailed information about that method.

| Methods                                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| :---------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [get_environment_map_extension](#get_environment_map_extension)         | Retrieves an extensible map by its Environment Map Extension object ID. \>**Note:** Extending a source or destination profile by means of browsing an external account may require including credentials in the request. The GET operation uses the credentials from the original process for the browse connection. However, because credential reuse can be problematic when sharing processes in Integration Packs, use the EXECUTE operation instead.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [bulk_environment_map_extension](#bulk_environment_map_extension)       | To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [execute_environment_map_extension](#execute_environment_map_extension) | Use the EXECUTE operation when you want to customize XML profiles by reimporting them from endpoint applications. The EXECUTE operation returns the current Environment Map Extension configuration similar to the GET operation. It also accepts connection credentials and automatically connects to the external application to retrieve additional custom fields for that profile. You must have the Runtime Management privilege to perform the EXECUTE operation. If you have the Runtime Management Read Access privilege, you cannot post connection credentials. For information about using these operations to retrieve or update map functions, refer to [Environment Map Extension functions](/docs/APIs/PlatformAPI/Environment_Map_Extension_functions). Include the `SourceBrowse` and `DestinationBrowse` sections as appropriate to browse the respective profile and include the required BrowseFields for the given connector. If you need to call the EXECUTE action repeatedly for the same map, you can alternatively use the `sessionId` to avoid having to supply the connector fields in subsequent calls. Session caching lasts about 30 minutes. |

## get_environment_map_extension

Retrieves an extensible map by its Environment Map Extension object ID. \>**Note:** Extending a source or destination profile by means of browsing an external account may require including credentials in the request. The GET operation uses the credentials from the original process for the browse connection. However, because credential reuse can be problematic when sharing processes in Integration Packs, use the EXECUTE operation instead.

- HTTP Method: `GET`
- Endpoint: `/EnvironmentMapExtension/{id}`

**Parameters**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| id\_ | str  | ✅       |             |

**Return Type**

`EnvironmentMapExtension`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.environment_map_extension.get_environment_map_extension(id_="id")

print(result)
```

## bulk_environment_map_extension

To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

- HTTP Method: `POST`
- Endpoint: `/EnvironmentMapExtension/bulk`

**Parameters**

| Name         | Type                                                                                  | Required | Description       |
| :----------- | :------------------------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [EnvironmentMapExtensionBulkRequest](../models/EnvironmentMapExtensionBulkRequest.md) | ❌       | The request body. |

**Return Type**

`EnvironmentMapExtensionBulkResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import EnvironmentMapExtensionBulkRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = EnvironmentMapExtensionBulkRequest(
    request=[
        {
            "id_": "56789abc-def0-1234-5678-9abcdef01234"
        }
    ],
    type_="GET"
)

result = sdk.environment_map_extension.bulk_environment_map_extension(request_body=request_body)

print(result)
```

## execute_environment_map_extension

Use the EXECUTE operation when you want to customize XML profiles by reimporting them from endpoint applications. The EXECUTE operation returns the current Environment Map Extension configuration similar to the GET operation. It also accepts connection credentials and automatically connects to the external application to retrieve additional custom fields for that profile. You must have the Runtime Management privilege to perform the EXECUTE operation. If you have the Runtime Management Read Access privilege, you cannot post connection credentials. For information about using these operations to retrieve or update map functions, refer to [Environment Map Extension functions](/docs/APIs/PlatformAPI/Environment_Map_Extension_functions). Include the `SourceBrowse` and `DestinationBrowse` sections as appropriate to browse the respective profile and include the required BrowseFields for the given connector. If you need to call the EXECUTE action repeatedly for the same map, you can alternatively use the `sessionId` to avoid having to supply the connector fields in subsequent calls. Session caching lasts about 30 minutes.

- HTTP Method: `POST`
- Endpoint: `/EnvironmentMapExtension/execute/{id}`

**Parameters**

| Name         | Type                                                            | Required | Description       |
| :----------- | :-------------------------------------------------------------- | :------- | :---------------- |
| request_body | [EnvironmentMapExtension](../models/EnvironmentMapExtension.md) | ❌       | The request body. |
| id\_         | str                                                             | ✅       |                   |

**Return Type**

`EnvironmentMapExtension`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import EnvironmentMapExtension

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = EnvironmentMapExtension(
    map={
        "browse_settings": {
            "destination_browse": {
                "browse_fields": [
                    {
                        "name": "name",
                        "value": "value"
                    }
                ],
                "session_id": "sessionId"
            },
            "source_browse": {
                "browse_fields": [
                    {
                        "name": "name",
                        "value": "value"
                    }
                ],
                "session_id": "sessionId"
            },
            "container_id": "containerId"
        },
        "destination_profile": {
            "node": [
                {
                    "name": "name",
                    "xpath": "xpath"
                }
            ],
            "component_id": "componentId",
            "type_": "type"
        },
        "destination_profile_extensions": {
            "node": [
                {
                    "character": {},
                    "date_time": {
                        "format": "format"
                    },
                    "number": {
                        "format": "format",
                        "implied_decimal": 3,
                        "signed": True
                    },
                    "enforce_unique": False,
                    "field_length_validation": False,
                    "mandatory": True,
                    "max_length": 10,
                    "min_length": 5,
                    "name": "name"
                }
            ]
        },
        "extended_functions": {
            "function": [
                {
                    "configuration": {
                        "cross_reference_lookup": {
                            "inputs": {
                                "input": [
                                    {
                                        "index": 0,
                                        "name": "name",
                                        "ref_id": 4
                                    }
                                ]
                            },
                            "outputs": {
                                "output": [
                                    {
                                        "index": 0,
                                        "name": "name",
                                        "ref_id": 4
                                    }
                                ]
                            },
                            "lookup_table_id": "lookupTableId",
                            "skip_if_no_inputs": False
                        },
                        "doc_cache_lookup": {
                            "inputs": {
                                "input": [
                                    {
                                        "index": 6,
                                        "key_id": 3,
                                        "name": "name"
                                    }
                                ]
                            },
                            "outputs": {
                                "output": [
                                    {
                                        "index": 5,
                                        "key": 10,
                                        "name": "name",
                                        "tag_list_key": 1
                                    }
                                ]
                            },
                            "cache_index": 5,
                            "doc_cache": "docCache"
                        },
                        "document_property": {
                            "default_value": "defaultValue",
                            "persist": True,
                            "property_id": "propertyId",
                            "property_name": "propertyName"
                        },
                        "japanese_character_conversion": {
                            "convert_from": "convertFrom",
                            "convert_to": "convertTo"
                        },
                        "scripting": {
                            "inputs": {
                                "input": [
                                    {
                                        "data_type": "CHARACTER",
                                        "index": 0,
                                        "name": "name"
                                    }
                                ]
                            },
                            "outputs": {
                                "output": [
                                    {
                                        "data_type": "CHARACTER",
                                        "index": 0,
                                        "name": "name"
                                    }
                                ]
                            },
                            "script": "Script",
                            "language": "GROOVY"
                        },
                        "sequential_value": {
                            "batch_size": 3,
                            "key_fix_to_length": 0,
                            "key_name": "keyName"
                        },
                        "simple_lookup": {
                            "table": {
                                "rows": {
                                    "row": [
                                        {
                                            "ref1": "ref1",
                                            "ref2": "ref2"
                                        }
                                    ]
                                }
                            }
                        },
                        "string_concat": {
                            "delimiter": "delimiter",
                            "fixed_length": 1
                        },
                        "string_split": {
                            "delimiter": "delimiter",
                            "split_length": 2
                        },
                        "user_defined_function": {
                            "id_": "id",
                            "version": 1
                        }
                    },
                    "inputs": {
                        "input": [
                            {
                                "default": "default",
                                "key": 6,
                                "name": "name"
                            }
                        ]
                    },
                    "outputs": {
                        "output": [
                            {
                                "key": 6,
                                "name": "name"
                            }
                        ]
                    },
                    "cache_type": "None",
                    "id_": "id",
                    "type_": "Count"
                }
            ]
        },
        "extended_mappings": {
            "mapping": [
                {
                    "from_function": "fromFunction",
                    "from_x_path": "fromXPath",
                    "to_function": "toFunction",
                    "to_x_path": "toXPath"
                }
            ]
        },
        "source_profile": {
            "node": [
                {
                    "name": "name",
                    "xpath": "xpath"
                }
            ],
            "component_id": "componentId",
            "type_": "type"
        },
        "source_profile_extensions": {
            "node": [
                {
                    "character": {},
                    "date_time": {
                        "format": "format"
                    },
                    "number": {
                        "format": "format",
                        "implied_decimal": 3,
                        "signed": True
                    },
                    "enforce_unique": False,
                    "field_length_validation": False,
                    "mandatory": True,
                    "max_length": 10,
                    "min_length": 5,
                    "name": "name"
                }
            ]
        }
    },
    environment_id="456789ab-cdef-0123-4567-89abcdef0123",
    extension_group_id="extensionGroupId",
    id_="Ab0Cd1Ef1Gh3Ij4Kl5Mn6Op7Qr8St9Uv0Wx9Yz8Zy7Xw6Vu5Ts4Rq3Po2Nm1Lk0Ji1Hg",
    map_id="01234567890123456789012345",
    name="Account - Customer",
    process_id="789abcde-f012-3456-789a-bcdef0123456"
)

result = sdk.environment_map_extension.execute_environment_map_extension(
    request_body=request_body,
    id_="id"
)

print(result)
```

