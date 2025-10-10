# EnvironmentService

A list of all methods in the `EnvironmentService` service. Click on the method name to view detailed information about that method.

| Methods                                                               | Description                                                                                                                                                                                                                                     |
| :-------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_environment](#create_environment)                             | Creates an environment having the specified name. Environment names must be unique.                                                                                                                                                             |
| [get_environment](#get_environment)                                   | Retrieves the properties of the environment with a specified ID.                                                                                                                                                                                |
| [update_environment](#update_environment)                             | Updates the Environment object having the specified ID. You can edit the name field only.                                                                                                                                                       |
| [delete_environment](#delete_environment)                             | Deletes the Environment object with a specified ID. It is not possible to delete an environment that has attached Runtimes or integration packs.                                                                                                |
| [bulk_environment](#bulk_environment)                                 | To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).                                                                                                                                          |
| [query_environment](#query_environment)                               | For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging). |
| [query_more_environment](#query_more_environment)                     | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                  |
| [update_environment_map_extension](#update_environment_map_extension) | Updates the extended mapping configuration for the specified Environment Map Extension object ID.                                                                                                                                               |

## create_environment

Creates an environment having the specified name. Environment names must be unique.

- HTTP Method: `POST`
- Endpoint: `/Environment`

**Parameters**

| Name         | Type                                    | Required | Description       |
| :----------- | :-------------------------------------- | :------- | :---------------- |
| request_body | [Environment](../models/Environment.md) | ❌       | The request body. |

**Return Type**

`Environment`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import Environment

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = Environment(
    classification="PROD",
    id_="456789ab-cdef-0123-4567-89abcdef0123",
    name="My Production Environment",
    parent_account="parentAccount",
    parent_environment="parentEnvironment"
)

result = sdk.environment.create_environment(request_body=request_body)

print(result)
```

## get_environment

Retrieves the properties of the environment with a specified ID.

- HTTP Method: `GET`
- Endpoint: `/Environment/{id}`

**Parameters**

| Name | Type | Required | Description                                            |
| :--- | :--- | :------- | :----------------------------------------------------- |
| id\_ | str  | ✅       | A unique ID assigned by the system to the environment. |

**Return Type**

`Environment`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.environment.get_environment(id_="id")

print(result)
```

## update_environment

Updates the Environment object having the specified ID. You can edit the name field only.

- HTTP Method: `POST`
- Endpoint: `/Environment/{id}`

**Parameters**

| Name         | Type                                    | Required | Description                                            |
| :----------- | :-------------------------------------- | :------- | :----------------------------------------------------- |
| request_body | [Environment](../models/Environment.md) | ❌       | The request body.                                      |
| id\_         | str                                     | ✅       | A unique ID assigned by the system to the environment. |

**Return Type**

`Environment`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import Environment

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = Environment(
    classification="PROD",
    id_="456789ab-cdef-0123-4567-89abcdef0123",
    name="My Production Environment",
    parent_account="parentAccount",
    parent_environment="parentEnvironment"
)

result = sdk.environment.update_environment(
    request_body=request_body,
    id_="id"
)

print(result)
```

## delete_environment

Deletes the Environment object with a specified ID. It is not possible to delete an environment that has attached Runtimes or integration packs.

- HTTP Method: `DELETE`
- Endpoint: `/Environment/{id}`

**Parameters**

| Name | Type | Required | Description                                            |
| :--- | :--- | :------- | :----------------------------------------------------- |
| id\_ | str  | ✅       | A unique ID assigned by the system to the environment. |

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.environment.delete_environment(id_="id")

print(result)
```

## bulk_environment

To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

- HTTP Method: `POST`
- Endpoint: `/Environment/bulk`

**Parameters**

| Name         | Type                                                          | Required | Description       |
| :----------- | :------------------------------------------------------------ | :------- | :---------------- |
| request_body | [EnvironmentBulkRequest](../models/EnvironmentBulkRequest.md) | ❌       | The request body. |

**Return Type**

`EnvironmentBulkResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import EnvironmentBulkRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = EnvironmentBulkRequest(
    request=[
        {
            "id_": "56789abc-def0-1234-5678-9abcdef01234"
        }
    ],
    type_="GET"
)

result = sdk.environment.bulk_environment(request_body=request_body)

print(result)
```

## query_environment

For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/Environment/query`

**Parameters**

| Name         | Type                                                          | Required | Description       |
| :----------- | :------------------------------------------------------------ | :------- | :---------------- |
| request_body | [EnvironmentQueryConfig](../models/EnvironmentQueryConfig.md) | ❌       | The request body. |

**Return Type**

`EnvironmentQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import EnvironmentQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = EnvironmentQueryConfig(
    query_filter={
        "expression": {
            "argument": [
                "argument"
            ],
            "operator": "EQUALS",
            "property": "name"
        }
    }
)

result = sdk.environment.query_environment(request_body=request_body)

print(result)
```

## query_more_environment

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/Environment/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`EnvironmentQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "dolore non "

result = sdk.environment.query_more_environment(request_body=request_body)

print(result)
```

## update_environment_map_extension

Updates the extended mapping configuration for the specified Environment Map Extension object ID.

- HTTP Method: `POST`
- Endpoint: `/EnvironmentMapExtension/{id}`

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

result = sdk.environment.update_environment_map_extension(
    request_body=request_body,
    id_="id"
)

print(result)
```

