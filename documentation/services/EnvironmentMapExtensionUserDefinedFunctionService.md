# EnvironmentMapExtensionUserDefinedFunctionService

A list of all methods in the `EnvironmentMapExtensionUserDefinedFunctionService` service. Click on the method name to view detailed information about that method.

| Methods                                                                                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| :---------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_environment_map_extension_user_defined_function](#create_environment_map_extension_user_defined_function) | The CREATE operation creates a new extensible user-defined function. User-defined functions created using the Environment Map Extension User Defined Function object exists only at the environment extension level and are tied to a single map extension only. When creating a new user-defined function, you define individual function steps that make up the greater user-defined function. Then, in the `\<Mappings\>` section of the request, you determine how to map or link each step to and from the function's input and output. \>**Caution:** Creating new functions requires all existing input and output values in the request regardless if they are mapped or populated with a default value. Otherwise, it overrides and removes those variables from the function. |
| [get_environment_map_extension_user_defined_function](#get_environment_map_extension_user_defined_function)       | Retrieves an extensible user-defined function associated with a given environment map extension function ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [update_environment_map_extension_user_defined_function](#update_environment_map_extension_user_defined_function) | Updates the extended configuration for a single user-defined function. \>**Caution:** Updating functions require all existing input and output values in the request regardless if they are mapped or populated with a default value. Otherwise, it overrides and removes those variables from the function.                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [delete_environment_map_extension_user_defined_function](#delete_environment_map_extension_user_defined_function) | Deletes the specified user-defined function. Deleted user-defined functions return a status of true and are no longer available for use in an API call or on the user interface. ### Restoring a deleted user-defined function Reinstate a deleted user-defined function by providing the function's id in a CREATE operation. You cannot make changes to a function during restoration (in other words, you cannot edit its values in a RESTORE request). By restoring a deleted function, it becomes available for use in an API call and in the user interface. After a successful RESTORE operation, the function returns a deleted status of false.                                                                                                                                |
| [bulk_environment_map_extension_user_defined_function](#bulk_environment_map_extension_user_defined_function)     | To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

## create_environment_map_extension_user_defined_function

The CREATE operation creates a new extensible user-defined function. User-defined functions created using the Environment Map Extension User Defined Function object exists only at the environment extension level and are tied to a single map extension only. When creating a new user-defined function, you define individual function steps that make up the greater user-defined function. Then, in the `\<Mappings\>` section of the request, you determine how to map or link each step to and from the function's input and output. \>**Caution:** Creating new functions requires all existing input and output values in the request regardless if they are mapped or populated with a default value. Otherwise, it overrides and removes those variables from the function.

- HTTP Method: `POST`
- Endpoint: `/EnvironmentMapExtensionUserDefinedFunction`

**Parameters**

| Name         | Type                                                                                                  | Required | Description       |
| :----------- | :---------------------------------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [EnvironmentMapExtensionUserDefinedFunction](../models/EnvironmentMapExtensionUserDefinedFunction.md) | ❌       | The request body. |

**Return Type**

`EnvironmentMapExtensionUserDefinedFunction`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import EnvironmentMapExtensionUserDefinedFunction

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = EnvironmentMapExtensionUserDefinedFunction(
    inputs={
        "input": [
            {
                "default": "default",
                "key": 6,
                "name": "name"
            }
        ]
    },
    mappings={
        "mapping": [
            {
                "from_function": "fromFunction",
                "from_key": 4,
                "to_function": "toFunction",
                "to_key": 10
            }
        ]
    },
    outputs={
        "output": [
            {
                "key": 6,
                "name": "name"
            }
        ]
    },
    steps={
        "step": [
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
                "position": 9,
                "type_": "Count"
            }
        ]
    },
    created_by="createdBy",
    created_date="createdDate",
    deleted=True,
    description="description",
    environment_map_extension_id="environmentMapExtensionId",
    id_="id",
    modified_by="modifiedBy",
    modified_date="modifiedDate",
    name="name"
)

result = sdk.environment_map_extension_user_defined_function.create_environment_map_extension_user_defined_function(request_body=request_body)

print(result)
```

## get_environment_map_extension_user_defined_function

Retrieves an extensible user-defined function associated with a given environment map extension function ID.

- HTTP Method: `GET`
- Endpoint: `/EnvironmentMapExtensionUserDefinedFunction/{id}`

**Parameters**

| Name | Type | Required | Description                                                                       |
| :--- | :--- | :------- | :-------------------------------------------------------------------------------- |
| id\_ | str  | ✅       | Represents the unique, system-generated ID of the extended user-defined function. |

**Return Type**

`EnvironmentMapExtensionUserDefinedFunction`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.environment_map_extension_user_defined_function.get_environment_map_extension_user_defined_function(id_="id")

print(result)
```

## update_environment_map_extension_user_defined_function

Updates the extended configuration for a single user-defined function. \>**Caution:** Updating functions require all existing input and output values in the request regardless if they are mapped or populated with a default value. Otherwise, it overrides and removes those variables from the function.

- HTTP Method: `POST`
- Endpoint: `/EnvironmentMapExtensionUserDefinedFunction/{id}`

**Parameters**

| Name         | Type                                                                                                  | Required | Description                                                                       |
| :----------- | :---------------------------------------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------- |
| request_body | [EnvironmentMapExtensionUserDefinedFunction](../models/EnvironmentMapExtensionUserDefinedFunction.md) | ❌       | The request body.                                                                 |
| id\_         | str                                                                                                   | ✅       | Represents the unique, system-generated ID of the extended user-defined function. |

**Return Type**

`EnvironmentMapExtensionUserDefinedFunction`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import EnvironmentMapExtensionUserDefinedFunction

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = EnvironmentMapExtensionUserDefinedFunction(
    inputs={
        "input": [
            {
                "default": "default",
                "key": 6,
                "name": "name"
            }
        ]
    },
    mappings={
        "mapping": [
            {
                "from_function": "fromFunction",
                "from_key": 4,
                "to_function": "toFunction",
                "to_key": 10
            }
        ]
    },
    outputs={
        "output": [
            {
                "key": 6,
                "name": "name"
            }
        ]
    },
    steps={
        "step": [
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
                "position": 9,
                "type_": "Count"
            }
        ]
    },
    created_by="createdBy",
    created_date="createdDate",
    deleted=True,
    description="description",
    environment_map_extension_id="environmentMapExtensionId",
    id_="id",
    modified_by="modifiedBy",
    modified_date="modifiedDate",
    name="name"
)

result = sdk.environment_map_extension_user_defined_function.update_environment_map_extension_user_defined_function(
    request_body=request_body,
    id_="id"
)

print(result)
```

## delete_environment_map_extension_user_defined_function

Deletes the specified user-defined function. Deleted user-defined functions return a status of true and are no longer available for use in an API call or on the user interface. ### Restoring a deleted user-defined function Reinstate a deleted user-defined function by providing the function's id in a CREATE operation. You cannot make changes to a function during restoration (in other words, you cannot edit its values in a RESTORE request). By restoring a deleted function, it becomes available for use in an API call and in the user interface. After a successful RESTORE operation, the function returns a deleted status of false.

- HTTP Method: `DELETE`
- Endpoint: `/EnvironmentMapExtensionUserDefinedFunction/{id}`

**Parameters**

| Name | Type | Required | Description                                                                       |
| :--- | :--- | :------- | :-------------------------------------------------------------------------------- |
| id\_ | str  | ✅       | Represents the unique, system-generated ID of the extended user-defined function. |

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.environment_map_extension_user_defined_function.delete_environment_map_extension_user_defined_function(id_="id")

print(result)
```

## bulk_environment_map_extension_user_defined_function

To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

- HTTP Method: `POST`
- Endpoint: `/EnvironmentMapExtensionUserDefinedFunction/bulk`

**Parameters**

| Name         | Type                                                                                                                        | Required | Description       |
| :----------- | :-------------------------------------------------------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [EnvironmentMapExtensionUserDefinedFunctionBulkRequest](../models/EnvironmentMapExtensionUserDefinedFunctionBulkRequest.md) | ❌       | The request body. |

**Return Type**

`EnvironmentMapExtensionUserDefinedFunctionBulkResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import EnvironmentMapExtensionUserDefinedFunctionBulkRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = EnvironmentMapExtensionUserDefinedFunctionBulkRequest(
    request=[
        {
            "id_": "56789abc-def0-1234-5678-9abcdef01234"
        }
    ],
    type_="GET"
)

result = sdk.environment_map_extension_user_defined_function.bulk_environment_map_extension_user_defined_function(request_body=request_body)

print(result)
```

