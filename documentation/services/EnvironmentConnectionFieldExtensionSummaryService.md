# EnvironmentConnectionFieldExtensionSummaryService

A list of all methods in the `EnvironmentConnectionFieldExtensionSummaryService` service. Click on the method name to view detailed information about that method.

| Methods                                                                                                                 | Description                                                                                                                                                                                                                                     |
| :---------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [query_environment_connection_field_extension_summary](#query_environment_connection_field_extension_summary)           | For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging). |
| [query_more_environment_connection_field_extension_summary](#query_more_environment_connection_field_extension_summary) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                  |

## query_environment_connection_field_extension_summary

For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/EnvironmentConnectionFieldExtensionSummary/query`

**Parameters**

| Name         | Type                                                                                                                        | Required | Description       |
| :----------- | :-------------------------------------------------------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [EnvironmentConnectionFieldExtensionSummaryQueryConfig](../models/EnvironmentConnectionFieldExtensionSummaryQueryConfig.md) | ❌       | The request body. |

**Return Type**

`EnvironmentConnectionFieldExtensionSummaryQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import EnvironmentConnectionFieldExtensionSummaryQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = EnvironmentConnectionFieldExtensionSummaryQueryConfig(
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

result = sdk.environment_connection_field_extension_summary.query_environment_connection_field_extension_summary(request_body=request_body)

print(result)
```

## query_more_environment_connection_field_extension_summary

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/EnvironmentConnectionFieldExtensionSummary/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`EnvironmentConnectionFieldExtensionSummaryQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "cupidatat"

result = sdk.environment_connection_field_extension_summary.query_more_environment_connection_field_extension_summary(request_body=request_body)

print(result)
```

