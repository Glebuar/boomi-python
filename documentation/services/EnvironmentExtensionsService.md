# EnvironmentExtensionsService

A list of all methods in the `EnvironmentExtensionsService` service. Click on the method name to view detailed information about that method.

| Methods                                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| :---------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [get_environment_extensions](#get_environment_extensions)               | Retrieves the extension values for the environment having the specified ID (except for encrypted values).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [update_environment_extensions](#update_environment_extensions)         | Updates the extension values for the environment having the specified ID. When updating extension values, you must perform either a partial update to update only those extension values requiring modification in the request, or a full update to update the full set of environment extensions in a single request. A partial update is typically recommended because it results in smaller payloads and more targeted updates. \>**Warning:** The UPDATE operation does not support running muliple map extensions requests concurrently. Some map extensions might not get updated properly. #### Performing a partial update To perform a **partial update**, set `partial` to true and then provide only the extension fields and values that you wish to update in the request. \>**Note:** For cross reference tables, you can update a single cross reference table. However, you must provide all values for the entire table. You cannot update individual rows within a table. \> \> - For process property components, you can update a single process property component but you must provide the values for all properties in the component. #### Performing a full update To perform a **full update**, set `partial` to false and then provide all the environment extension fields and values in the request, regardless if you wish to change only some values but not all. \>**Caution:** Values not included in the request are reset to use their default values. If you omit the partial attribute, the behavior defaults to a full update. |
| [bulk_environment_extensions](#bulk_environment_extensions)             | To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [query_environment_extensions](#query_environment_extensions)           | For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [query_more_environment_extensions](#query_more_environment_extensions) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

## get_environment_extensions

Retrieves the extension values for the environment having the specified ID (except for encrypted values).

- HTTP Method: `GET`
- Endpoint: `/EnvironmentExtensions/{id}`

**Parameters**

| Name | Type | Required | Description                                                                                                                                                                                                                                                                     |
| :--- | :--- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| id\_ | str  | ✅       | The ID of the object. This can be either of the following: 1. The value of `environmentId`. 2. A conceptual ID synthesized from the environment ID (`environmentId`) and the ID of the multi-install integration pack to which the extension values apply (`extensionGroupId`). |

**Return Type**

`EnvironmentExtensions`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.environment_extensions.get_environment_extensions(id_="id")

print(result)
```

## update_environment_extensions

Updates the extension values for the environment having the specified ID. When updating extension values, you must perform either a partial update to update only those extension values requiring modification in the request, or a full update to update the full set of environment extensions in a single request. A partial update is typically recommended because it results in smaller payloads and more targeted updates. \>**Warning:** The UPDATE operation does not support running muliple map extensions requests concurrently. Some map extensions might not get updated properly. #### Performing a partial update To perform a **partial update**, set `partial` to true and then provide only the extension fields and values that you wish to update in the request. \>**Note:** For cross reference tables, you can update a single cross reference table. However, you must provide all values for the entire table. You cannot update individual rows within a table. \> \> - For process property components, you can update a single process property component but you must provide the values for all properties in the component. #### Performing a full update To perform a **full update**, set `partial` to false and then provide all the environment extension fields and values in the request, regardless if you wish to change only some values but not all. \>**Caution:** Values not included in the request are reset to use their default values. If you omit the partial attribute, the behavior defaults to a full update.

- HTTP Method: `POST`
- Endpoint: `/EnvironmentExtensions/{id}`

**Parameters**

| Name         | Type                                                        | Required | Description                                                                                                                                                                                                                                                               |
| :----------- | :---------------------------------------------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| request_body | [EnvironmentExtensions](../models/EnvironmentExtensions.md) | ❌       | The request body.                                                                                                                                                                                                                                                         |
| id\_         | str                                                         | ✅       | The ID of the object. This can be either of the following: 1. The value of environmentId. 2. A conceptual ID synthesized from the environment ID (environmentId) and the ID of the multi-install integration pack to which the extension values apply (extensionGroupId). |

**Return Type**

`EnvironmentExtensions`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import EnvironmentExtensions

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = EnvironmentExtensions(
    pgp_certificates={
        "pgp_certificate": [
            {
                "id_": "id",
                "use_default": True,
                "value": "value"
            }
        ]
    },
    connections={
        "connection": [
            {
                "field": [
                    {
                        "component_override": True,
                        "custom_properties": {
                            "properties": [
                                {
                                    "encrypted": False,
                                    "key": "key",
                                    "value": "value"
                                }
                            ]
                        },
                        "encrypted_value_set": True,
                        "id_": "id",
                        "use_default": False,
                        "uses_encryption": True,
                        "value": "value"
                    }
                ],
                "id_": "id",
                "name": "name"
            }
        ]
    },
    cross_references={
        "cross_reference": [
            {
                "cross_reference_rows": {
                    "row": [
                        {
                            "ref1": "ref1",
                            "ref10": "ref10",
                            "ref11": "ref11",
                            "ref12": "ref12",
                            "ref13": "ref13",
                            "ref14": "ref14",
                            "ref15": "ref15",
                            "ref16": "ref16",
                            "ref17": "ref17",
                            "ref18": "ref18",
                            "ref19": "ref19",
                            "ref2": "ref2",
                            "ref20": "ref20",
                            "ref3": "ref3",
                            "ref4": "ref4",
                            "ref5": "ref5",
                            "ref6": "ref6",
                            "ref7": "ref7",
                            "ref8": "ref8",
                            "ref9": "ref9"
                        }
                    ]
                },
                "id_": "id",
                "name": "name",
                "override_values": True
            }
        ]
    },
    environment_id="456789ab-cdef-0123-4567-89abcdef0123",
    extension_group_id="extensionGroupId",
    id_="456789ab-cdef-0123-4567-89abcdef0123",
    operations={
        "operation": [
            {
                "field": [
                    {
                        "component_override": True,
                        "custom_properties": {
                            "properties": [
                                {
                                    "encrypted": False,
                                    "key": "key",
                                    "value": "value"
                                }
                            ]
                        },
                        "encrypted_value_set": True,
                        "id_": "id",
                        "use_default": False,
                        "uses_encryption": True,
                        "value": "value"
                    }
                ],
                "id_": "id",
                "name": "name"
            }
        ]
    },
    partial=True,
    process_properties={
        "process_property": [
            {
                "process_property_value": [
                    {
                        "component_override": False,
                        "encrypted_value_set": False,
                        "key": "key",
                        "label": "label",
                        "use_default": True,
                        "uses_encryption": False,
                        "validate": False,
                        "value": "value"
                    }
                ],
                "id_": "id",
                "name": "name"
            }
        ]
    },
    properties={
        "property": [
            {
                "name": "name",
                "value": "value"
            }
        ]
    },
    shared_communications={
        "shared_communication": [
            {
                "field": [
                    {
                        "component_override": True,
                        "custom_properties": {
                            "properties": [
                                {
                                    "encrypted": False,
                                    "key": "key",
                                    "value": "value"
                                }
                            ]
                        },
                        "encrypted_value_set": True,
                        "id_": "id",
                        "use_default": False,
                        "uses_encryption": True,
                        "value": "value"
                    }
                ],
                "id_": "id",
                "name": "name",
                "type_": "type"
            }
        ]
    },
    trading_partners={
        "trading_partner": [
            {
                "category": [
                    {
                        "field": [
                            {
                                "component_override": True,
                                "custom_properties": {
                                    "properties": [
                                        {
                                            "encrypted": False,
                                            "key": "key",
                                            "value": "value"
                                        }
                                    ]
                                },
                                "encrypted_value_set": True,
                                "id_": "id",
                                "use_default": False,
                                "uses_encryption": True,
                                "value": "value"
                            }
                        ],
                        "id_": "id",
                        "name": "name"
                    }
                ],
                "id_": "id",
                "name": "name"
            }
        ]
    }
)

result = sdk.environment_extensions.update_environment_extensions(
    request_body=request_body,
    id_="id"
)

print(result)
```

## bulk_environment_extensions

To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

- HTTP Method: `POST`
- Endpoint: `/EnvironmentExtensions/bulk`

**Parameters**

| Name         | Type                                                                              | Required | Description       |
| :----------- | :-------------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [EnvironmentExtensionsBulkRequest](../models/EnvironmentExtensionsBulkRequest.md) | ❌       | The request body. |

**Return Type**

`EnvironmentExtensionsBulkResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import EnvironmentExtensionsBulkRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = EnvironmentExtensionsBulkRequest(
    request=[
        {
            "id_": "56789abc-def0-1234-5678-9abcdef01234"
        }
    ],
    type_="GET"
)

result = sdk.environment_extensions.bulk_environment_extensions(request_body=request_body)

print(result)
```

## query_environment_extensions

For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/EnvironmentExtensions/query`

**Parameters**

| Name         | Type                                                                              | Required | Description       |
| :----------- | :-------------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [EnvironmentExtensionsQueryConfig](../models/EnvironmentExtensionsQueryConfig.md) | ❌       | The request body. |

**Return Type**

`EnvironmentExtensionsQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import EnvironmentExtensionsQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = EnvironmentExtensionsQueryConfig(
    query_filter={
        "expression": {
            "argument": [
                "argument"
            ],
            "operator": "EQUALS",
            "property": "environmentId"
        }
    }
)

result = sdk.environment_extensions.query_environment_extensions(request_body=request_body)

print(result)
```

## query_more_environment_extensions

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/EnvironmentExtensions/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`EnvironmentExtensionsQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "cupidatat Lor"

result = sdk.environment_extensions.query_more_environment_extensions(request_body=request_body)

print(result)
```

