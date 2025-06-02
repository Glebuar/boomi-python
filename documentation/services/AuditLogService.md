# AuditLogService

A list of all methods in the `AuditLogService` service. Click on the method name to view detailed information about that method.

| Methods                                       | Description                                                                                                                                                                                                                                                        |
| :-------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [get_audit_log](#get_audit_log)               | Retrieve audit information for a single audit log entry, like the audit logs action message, the audit log type, action, and modifier. For example, you can use the GET operation to retrieve the environment extensions for a certain date using the document ID. |
| [bulk_audit_log](#bulk_audit_log)             | To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).                                                                                                                                                             |
| [query_audit_log](#query_audit_log)           | For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).                    |
| [query_more_audit_log](#query_more_audit_log) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                     |

## get_audit_log

Retrieve audit information for a single audit log entry, like the audit logs action message, the audit log type, action, and modifier. For example, you can use the GET operation to retrieve the environment extensions for a certain date using the document ID.

- HTTP Method: `GET`
- Endpoint: `/AuditLog/{id}`

**Parameters**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| id\_ | str  | ✅       |             |

**Return Type**

`AuditLog`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.audit_log.get_audit_log(id_="id")

print(result)
```

## bulk_audit_log

To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

- HTTP Method: `POST`
- Endpoint: `/AuditLog/bulk`

**Parameters**

| Name         | Type                                                    | Required | Description       |
| :----------- | :------------------------------------------------------ | :------- | :---------------- |
| request_body | [AuditLogBulkRequest](../models/AuditLogBulkRequest.md) | ❌       | The request body. |

**Return Type**

`AuditLogBulkResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import AuditLogBulkRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = AuditLogBulkRequest(
    request=[
        {
            "id_": "56789abc-def0-1234-5678-9abcdef01234"
        }
    ],
    type_="GET"
)

result = sdk.audit_log.bulk_audit_log(request_body=request_body)

print(result)
```

## query_audit_log

For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/AuditLog/query`

**Parameters**

| Name         | Type                                                    | Required | Description       |
| :----------- | :------------------------------------------------------ | :------- | :---------------- |
| request_body | [AuditLogQueryConfig](../models/AuditLogQueryConfig.md) | ❌       | The request body. |

**Return Type**

`AuditLogQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import AuditLogQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = AuditLogQueryConfig(
    query_filter={
        "expression": {
            "argument": [
                "argument"
            ],
            "operator": "EQUALS",
            "property": "containerId"
        }
    }
)

result = sdk.audit_log.query_audit_log(request_body=request_body)

print(result)
```

## query_more_audit_log

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/AuditLog/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`AuditLogQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "proident sit q"

result = sdk.audit_log.query_more_audit_log(request_body=request_body)

print(result)
```

