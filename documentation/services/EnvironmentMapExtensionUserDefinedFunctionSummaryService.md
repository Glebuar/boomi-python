# EnvironmentMapExtensionUserDefinedFunctionSummaryService

A list of all methods in the `EnvironmentMapExtensionUserDefinedFunctionSummaryService` service. Click on the method name to view detailed information about that method.

| Methods                                                                                                                                   | Description                                                                                                                                                                                                                                     |
| :---------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [query_environment_map_extension_user_defined_function_summary](#query_environment_map_extension_user_defined_function_summary)           | For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging). |
| [query_more_environment_map_extension_user_defined_function_summary](#query_more_environment_map_extension_user_defined_function_summary) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                  |

## query_environment_map_extension_user_defined_function_summary

For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/EnvironmentMapExtensionUserDefinedFunctionSummary/query`

**Parameters**

| Name         | Type                                                                                                                                      | Required | Description       |
| :----------- | :---------------------------------------------------------------------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [EnvironmentMapExtensionUserDefinedFunctionSummaryQueryConfig](../models/EnvironmentMapExtensionUserDefinedFunctionSummaryQueryConfig.md) | ❌       | The request body. |

**Return Type**

`EnvironmentMapExtensionUserDefinedFunctionSummaryQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import EnvironmentMapExtensionUserDefinedFunctionSummaryQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = EnvironmentMapExtensionUserDefinedFunctionSummaryQueryConfig(
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

result = sdk.environment_map_extension_user_defined_function_summary.query_environment_map_extension_user_defined_function_summary(request_body=request_body)

print(result)
```

## query_more_environment_map_extension_user_defined_function_summary

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/EnvironmentMapExtensionUserDefinedFunctionSummary/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`EnvironmentMapExtensionUserDefinedFunctionSummaryQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "dolore qui ipsu"

result = sdk.environment_map_extension_user_defined_function_summary.query_more_environment_map_extension_user_defined_function_summary(request_body=request_body)

print(result)
```

