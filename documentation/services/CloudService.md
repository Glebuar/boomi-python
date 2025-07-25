# CloudService

A list of all methods in the `CloudService` service. Click on the method name to view detailed information about that method.

| Methods                               | Description                                                                                                                                                                                                                                     |
| :------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [get_cloud](#get_cloud)               | Retrieves the properties of the Runtime cloud having the specified ID.                                                                                                                                                                          |
| [bulk_cloud](#bulk_cloud)             | To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).                                                                                                                                          |
| [query_cloud](#query_cloud)           | For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging). |
| [query_more_cloud](#query_more_cloud) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                  |

## get_cloud

Retrieves the properties of the Runtime cloud having the specified ID.

- HTTP Method: `GET`
- Endpoint: `/Cloud/{id}`

**Parameters**

| Name | Type | Required | Description                                              |
| :--- | :--- | :------- | :------------------------------------------------------- |
| id\_ | str  | ✅       | A unique ID assigned by the system to the Runtime cloud. |

**Return Type**

`Cloud`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.cloud.get_cloud(id_="id")

print(result)
```

## bulk_cloud

To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

- HTTP Method: `POST`
- Endpoint: `/Cloud/bulk`

**Parameters**

| Name         | Type                                              | Required | Description       |
| :----------- | :------------------------------------------------ | :------- | :---------------- |
| request_body | [CloudBulkRequest](../models/CloudBulkRequest.md) | ❌       | The request body. |

**Return Type**

`CloudBulkResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import CloudBulkRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = CloudBulkRequest(
    request=[
        {
            "id_": "56789abc-def0-1234-5678-9abcdef01234"
        }
    ],
    type_="GET"
)

result = sdk.cloud.bulk_cloud(request_body=request_body)

print(result)
```

## query_cloud

For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/Cloud/query`

**Parameters**

| Name         | Type                                              | Required | Description       |
| :----------- | :------------------------------------------------ | :------- | :---------------- |
| request_body | [CloudQueryConfig](../models/CloudQueryConfig.md) | ❌       | The request body. |

**Return Type**

`CloudQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import CloudQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = CloudQueryConfig(
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

result = sdk.cloud.query_cloud(request_body=request_body)

print(result)
```

## query_more_cloud

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/Cloud/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`CloudQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "adipisicing "

result = sdk.cloud.query_more_cloud(request_body=request_body)

print(result)
```

