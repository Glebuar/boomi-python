# ApiUsageCountService

A list of all methods in the `ApiUsageCountService` service. Click on the method name to view detailed information about that method.

| Methods                                                   | Description                                                                                                                                                                                                                                     |
| :-------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [query_api_usage_count](#query_api_usage_count)           | For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging). |
| [query_more_api_usage_count](#query_more_api_usage_count) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                  |

## query_api_usage_count

For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/ApiUsageCount/query`

**Parameters**

| Name         | Type                                                              | Required | Description       |
| :----------- | :---------------------------------------------------------------- | :------- | :---------------- |
| request_body | [ApiUsageCountQueryConfig](../models/ApiUsageCountQueryConfig.md) | ❌       | The request body. |

**Return Type**

`ApiUsageCountQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import ApiUsageCountQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = ApiUsageCountQueryConfig(
    query_filter={
        "expression": {
            "argument": [
                "argument"
            ],
            "operator": "EQUALS",
            "property": "processDate"
        }
    }
)

result = sdk.api_usage_count.query_api_usage_count(request_body=request_body)

print(result)
```

## query_more_api_usage_count

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/ApiUsageCount/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`ApiUsageCountQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "ad proident m"

result = sdk.api_usage_count.query_more_api_usage_count(request_body=request_body)

print(result)
```

