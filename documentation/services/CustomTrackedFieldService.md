# CustomTrackedFieldService

A list of all methods in the `CustomTrackedFieldService` service. Click on the method name to view detailed information about that method.

| Methods                                                             | Description                                                                                                                                                                                                                                                                                                                                     |
| :------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [query_custom_tracked_field](#query_custom_tracked_field)           | For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging). \>**Note:** This operation doesn't accept filters because the list is constrained to 20 fields. |
| [query_more_custom_tracked_field](#query_more_custom_tracked_field) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                                                                                                  |

## query_custom_tracked_field

For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging). \>**Note:** This operation doesn't accept filters because the list is constrained to 20 fields.

- HTTP Method: `POST`
- Endpoint: `/CustomTrackedField/query`

**Parameters**

| Name         | Type                                                                        | Required | Description       |
| :----------- | :-------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [CustomTrackedFieldQueryConfig](../models/CustomTrackedFieldQueryConfig.md) | ❌       | The request body. |

**Return Type**

`CustomTrackedFieldQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import CustomTrackedFieldQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = CustomTrackedFieldQueryConfig(
    query_filter={
        "expression": {
            "argument": [
                "argument"
            ],
            "operator": "EQUALS",
            "property": "property"
        }
    }
)

result = sdk.custom_tracked_field.query_custom_tracked_field(request_body=request_body)

print(result)
```

## query_more_custom_tracked_field

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/CustomTrackedField/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`CustomTrackedFieldQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "ex nisi amet"

result = sdk.custom_tracked_field.query_more_custom_tracked_field(request_body=request_body)

print(result)
```

