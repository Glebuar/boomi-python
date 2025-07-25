# ProcessSchedulesService

A list of all methods in the `ProcessSchedulesService` service. Click on the method name to view detailed information about that method.

| Methods                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| :------------------------------------------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [get_process_schedules](#get_process_schedules)               | Retrieves the Process Schedules object with a specific conceptual ID. The ordinary GET operation retrieves the Process Schedules object with a specific conceptual ID. The bulk GET operation retrieves the Process Schedules objects with specific conceptual IDs to a maximum of 100. In addition, you can obtain conceptual IDs from the QUERY operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [update_process_schedules](#update_process_schedules)         | Clears and updates the process run schedules specified in the Process Schedules object with a specific ID. The body of the request must specify not only the conceptual object ID but also the Runtime and process IDs. You can obtain the object ID from a QUERY operation. A Process Schedules object exists for every deployed process. If you do not update the schedule, the object is empty and a run schedule is not in effect. \>**Note:** Listener processes cannot be scheduled. If a listener process is referenced, the call will fail with a 400 status code. You must have the **Runtime Management** privilege and the **Scheduling** privilege to perform the UPDATE operation. If you have the **Runtime Management Read Access** privilege, you cannot update process run schedules. \>**Note:** After you update run schedules for a process on a Runtime, those schedules appear in the **Scheduling** dialog using the Advanced (cron) syntax. You can additionally employ a Bulk UPDATE operation for the Process Schedules object. See related links for more information about performing a Bulk UPDATE operation. |
| [bulk_process_schedules](#bulk_process_schedules)             | To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [query_process_schedules](#query_process_schedules)           | For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [query_more_process_schedules](#query_more_process_schedules) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

## get_process_schedules

Retrieves the Process Schedules object with a specific conceptual ID. The ordinary GET operation retrieves the Process Schedules object with a specific conceptual ID. The bulk GET operation retrieves the Process Schedules objects with specific conceptual IDs to a maximum of 100. In addition, you can obtain conceptual IDs from the QUERY operation.

- HTTP Method: `GET`
- Endpoint: `/ProcessSchedules/{id}`

**Parameters**

| Name | Type | Required | Description                                                                        |
| :--- | :--- | :------- | :--------------------------------------------------------------------------------- |
| id\_ | str  | ✅       | The object’s conceptual ID, which is synthesized from the process and Runtime IDs. |

**Return Type**

`ProcessSchedules`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.process_schedules.get_process_schedules(id_="id")

print(result)
```

## update_process_schedules

Clears and updates the process run schedules specified in the Process Schedules object with a specific ID. The body of the request must specify not only the conceptual object ID but also the Runtime and process IDs. You can obtain the object ID from a QUERY operation. A Process Schedules object exists for every deployed process. If you do not update the schedule, the object is empty and a run schedule is not in effect. \>**Note:** Listener processes cannot be scheduled. If a listener process is referenced, the call will fail with a 400 status code. You must have the **Runtime Management** privilege and the **Scheduling** privilege to perform the UPDATE operation. If you have the **Runtime Management Read Access** privilege, you cannot update process run schedules. \>**Note:** After you update run schedules for a process on a Runtime, those schedules appear in the **Scheduling** dialog using the Advanced (cron) syntax. You can additionally employ a Bulk UPDATE operation for the Process Schedules object. See related links for more information about performing a Bulk UPDATE operation.

- HTTP Method: `POST`
- Endpoint: `/ProcessSchedules/{id}`

**Parameters**

| Name         | Type                                              | Required | Description                                                                        |
| :----------- | :------------------------------------------------ | :------- | :--------------------------------------------------------------------------------- |
| request_body | [ProcessSchedules](../models/ProcessSchedules.md) | ❌       | The request body.                                                                  |
| id\_         | str                                               | ✅       | The object’s conceptual ID, which is synthesized from the process and Runtime IDs. |

**Return Type**

`ProcessSchedules`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import ProcessSchedules

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = ProcessSchedules(
    retry={
        "schedule": [
            {
                "days_of_month": "daysOfMonth",
                "days_of_week": "daysOfWeek",
                "hours": "hours",
                "minutes": "minutes",
                "months": "months",
                "years": "years"
            }
        ],
        "max_retry": 9
    },
    schedule=[
        {
            "days_of_month": "daysOfMonth",
            "days_of_week": "daysOfWeek",
            "hours": "hours",
            "minutes": "minutes",
            "months": "months",
            "years": "years"
        }
    ],
    atom_id="3456789a-bcde-f0123-4567-89abcdef012",
    id_="Ab0Cd1Ef1Gh3Ij4Kl5Mn6Op7Qr8St9Uv0Wx9Yz8Zy7Xw6Vu5Ts4Rq3Po2Nm1Lk0Ji1Hg",
    process_id="789abcde-f012-3456-789a-bcdef0123456"
)

result = sdk.process_schedules.update_process_schedules(
    request_body=request_body,
    id_="id"
)

print(result)
```

## bulk_process_schedules

To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

- HTTP Method: `POST`
- Endpoint: `/ProcessSchedules/bulk`

**Parameters**

| Name         | Type                                                                    | Required | Description       |
| :----------- | :---------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [ProcessSchedulesBulkRequest](../models/ProcessSchedulesBulkRequest.md) | ❌       | The request body. |

**Return Type**

`ProcessSchedulesBulkResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import ProcessSchedulesBulkRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = ProcessSchedulesBulkRequest(
    request=[
        {
            "id_": "56789abc-def0-1234-5678-9abcdef01234"
        }
    ],
    type_="GET"
)

result = sdk.process_schedules.bulk_process_schedules(request_body=request_body)

print(result)
```

## query_process_schedules

For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/ProcessSchedules/query`

**Parameters**

| Name         | Type                                                                    | Required | Description       |
| :----------- | :---------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [ProcessSchedulesQueryConfig](../models/ProcessSchedulesQueryConfig.md) | ❌       | The request body. |

**Return Type**

`ProcessSchedulesQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import ProcessSchedulesQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = ProcessSchedulesQueryConfig(
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

result = sdk.process_schedules.query_process_schedules(request_body=request_body)

print(result)
```

## query_more_process_schedules

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/ProcessSchedules/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`ProcessSchedulesQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "dolore in n"

result = sdk.process_schedules.query_more_process_schedules(request_body=request_body)

print(result)
```

