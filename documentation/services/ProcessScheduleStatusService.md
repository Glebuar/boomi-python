# ProcessScheduleStatusService

A list of all methods in the `ProcessScheduleStatusService` service. Click on the method name to view detailed information about that method.

| Methods                                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| :------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [get_process_schedule_status](#get_process_schedule_status)               | Retrieves the Process Schedule Status object with a specified conceptual ID. The ordinary GET operation retrieves the Process Schedules object with a specific conceptual ID. The bulk GET operation retrieves the Process Schedules objects with specific conceptual IDs to a maximum of 100. In addition, you can obtain conceptual IDs from the QUERY operation.                                                                                                                   |
| [update_process_schedule_status](#update_process_schedule_status)         | Stops or resumes process run schedules for a deployed process. The body of the request must specify not only the conceptual Process Schedule Status object ID but also the Runtime and process IDs. You can obtain the object ID from a QUERY operation. You must have the Runtime Management privilege and the Scheduling privilege to perform the UPDATE operation. If you have the Runtime Management Read Accessprivilege, you cannot update the status of process run schedules. |
| [bulk_process_schedule_status](#bulk_process_schedule_status)             | To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).                                                                                                                                                                                                                                                                                                                                                                                |
| [query_process_schedule_status](#query_process_schedule_status)           | For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                                                                                       |
| [query_more_process_schedule_status](#query_more_process_schedule_status) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                                                                                                                                                                                                                                        |

## get_process_schedule_status

Retrieves the Process Schedule Status object with a specified conceptual ID. The ordinary GET operation retrieves the Process Schedules object with a specific conceptual ID. The bulk GET operation retrieves the Process Schedules objects with specific conceptual IDs to a maximum of 100. In addition, you can obtain conceptual IDs from the QUERY operation.

- HTTP Method: `GET`
- Endpoint: `/ProcessScheduleStatus/{id}`

**Parameters**

| Name | Type | Required | Description                                                                        |
| :--- | :--- | :------- | :--------------------------------------------------------------------------------- |
| id\_ | str  | ✅       | The object’s conceptual ID, which is synthesized from the process and Runtime IDs. |

**Return Type**

`ProcessScheduleStatus`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.process_schedule_status.get_process_schedule_status(id_="id")

print(result)
```

## update_process_schedule_status

Stops or resumes process run schedules for a deployed process. The body of the request must specify not only the conceptual Process Schedule Status object ID but also the Runtime and process IDs. You can obtain the object ID from a QUERY operation. You must have the Runtime Management privilege and the Scheduling privilege to perform the UPDATE operation. If you have the Runtime Management Read Accessprivilege, you cannot update the status of process run schedules.

- HTTP Method: `POST`
- Endpoint: `/ProcessScheduleStatus/{id}`

**Parameters**

| Name         | Type                                                        | Required | Description       |
| :----------- | :---------------------------------------------------------- | :------- | :---------------- |
| request_body | [ProcessScheduleStatus](../models/ProcessScheduleStatus.md) | ❌       | The request body. |
| id\_         | str                                                         | ✅       |                   |

**Return Type**

`ProcessScheduleStatus`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import ProcessScheduleStatus

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = ProcessScheduleStatus(
    atom_id="3456789a-bcde-f0123-4567-89abcdef012",
    enabled="true",
    id_="Ab0Cd1Ef1Gh3Ij4Kl5Mn6Op7Qr8St9Uv0Wx9Yz8Zy7Xw6Vu5Ts4Rq3Po2Nm1Lk0Ji1Hg",
    process_id="789abcde-f012-3456-789a-bcdef0123456"
)

result = sdk.process_schedule_status.update_process_schedule_status(
    request_body=request_body,
    id_="id"
)

print(result)
```

## bulk_process_schedule_status

To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

- HTTP Method: `POST`
- Endpoint: `/ProcessScheduleStatus/bulk`

**Parameters**

| Name         | Type                                                                              | Required | Description       |
| :----------- | :-------------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [ProcessScheduleStatusBulkRequest](../models/ProcessScheduleStatusBulkRequest.md) | ❌       | The request body. |

**Return Type**

`ProcessScheduleStatusBulkResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import ProcessScheduleStatusBulkRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = ProcessScheduleStatusBulkRequest(
    request=[
        {
            "id_": "56789abc-def0-1234-5678-9abcdef01234"
        }
    ],
    type_="GET"
)

result = sdk.process_schedule_status.bulk_process_schedule_status(request_body=request_body)

print(result)
```

## query_process_schedule_status

For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/ProcessScheduleStatus/query`

**Parameters**

| Name         | Type                                                                              | Required | Description       |
| :----------- | :-------------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [ProcessScheduleStatusQueryConfig](../models/ProcessScheduleStatusQueryConfig.md) | ❌       | The request body. |

**Return Type**

`ProcessScheduleStatusQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import ProcessScheduleStatusQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = ProcessScheduleStatusQueryConfig(
    query_filter={
        "expression": {
            "argument": [
                "argument"
            ],
            "operator": "EQUALS",
            "property": "processId"
        }
    }
)

result = sdk.process_schedule_status.query_process_schedule_status(request_body=request_body)

print(result)
```

## query_more_process_schedule_status

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/ProcessScheduleStatus/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`ProcessScheduleStatusQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "ullamco"

result = sdk.process_schedule_status.query_more_process_schedule_status(request_body=request_body)

print(result)
```

