# EnvironmentMapExtensionExternalComponentService

A list of all methods in the `EnvironmentMapExtensionExternalComponentService` service. Click on the method name to view detailed information about that method.

| Methods                                                                                                             | Description                                                                                                                                                                                                                                     |
| :------------------------------------------------------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [query_environment_map_extension_external_component](#query_environment_map_extension_external_component)           | For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging). |
| [query_more_environment_map_extension_external_component](#query_more_environment_map_extension_external_component) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                  |

## query_environment_map_extension_external_component

For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/EnvironmentMapExtensionExternalComponent/query`

**Parameters**

| Name         | Type                                                                                                                    | Required | Description       |
| :----------- | :---------------------------------------------------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [EnvironmentMapExtensionExternalComponentQueryConfig](../models/EnvironmentMapExtensionExternalComponentQueryConfig.md) | ❌       | The request body. |

**Return Type**

`EnvironmentMapExtensionExternalComponentQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import EnvironmentMapExtensionExternalComponentQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = EnvironmentMapExtensionExternalComponentQueryConfig(
    query_filter={
        "expression": {
            "argument": [
                "argument"
            ],
            "operator": "EQUALS",
            "property": "ACCOUNT_ID"
        }
    }
)

result = sdk.environment_map_extension_external_component.query_environment_map_extension_external_component(request_body=request_body)

print(result)
```

## query_more_environment_map_extension_external_component

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/EnvironmentMapExtensionExternalComponent/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`EnvironmentMapExtensionExternalComponentQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "labore"

result = sdk.environment_map_extension_external_component.query_more_environment_map_extension_external_component(request_body=request_body)

print(result)
```

