# RuntimeReleaseScheduleService

A list of all methods in the `RuntimeReleaseScheduleService` service. Click on the method name to view detailed information about that method.

| Methods                                                             | Description                                                                                                                                         |
| :------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_runtime_release_schedule](#create_runtime_release_schedule) | The CREATE operation sets a schedule for receiving updates with the scheduleType, dayOfWeek, hourOfDay, and timeZone fields.                        |
| [get_runtime_release_schedule](#get_runtime_release_schedule)       | The GET operation returns the current schedule for receiving updates on a specified Runtime, Runtime cluster, or Runtime cloud.                     |
| [update_runtime_release_schedule](#update_runtime_release_schedule) | The UPDATE operation modifies a set schedule for receiving updates.                                                                                 |
| [delete_runtime_release_schedule](#delete_runtime_release_schedule) | The DELETE operation sets the scheduleType to NEVER, meaning that the Runtime, Runtime cluster, or Runtime cloud receives updates only during the . |
| [bulk_runtime_release_schedule](#bulk_runtime_release_schedule)     |                                                                                                                                                     |

## create_runtime_release_schedule

The CREATE operation sets a schedule for receiving updates with the scheduleType, dayOfWeek, hourOfDay, and timeZone fields.

- HTTP Method: `POST`
- Endpoint: `/RuntimeReleaseSchedule`

**Parameters**

| Name         | Type                                                          | Required | Description       |
| :----------- | :------------------------------------------------------------ | :------- | :---------------- |
| request_body | [RuntimeReleaseSchedule](../models/RuntimeReleaseSchedule.md) | ❌       | The request body. |

**Return Type**

`RuntimeReleaseSchedule`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import RuntimeReleaseSchedule

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = RuntimeReleaseSchedule(
    atom_id="atomId",
    day_of_week="dayOfWeek",
    hour_of_day=6,
    schedule_type="NEVER",
    time_zone="timeZone"
)

result = sdk.runtime_release_schedule.create_runtime_release_schedule(request_body=request_body)

print(result)
```

## get_runtime_release_schedule

The GET operation returns the current schedule for receiving updates on a specified Runtime, Runtime cluster, or Runtime cloud.

- HTTP Method: `GET`
- Endpoint: `/RuntimeReleaseSchedule/{id}`

**Parameters**

| Name | Type | Required | Description                                                   |
| :--- | :--- | :------- | :------------------------------------------------------------ |
| id\_ | str  | ✅       | The ID of the container for which you want to set a schedule. |

**Return Type**

`RuntimeReleaseSchedule`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.runtime_release_schedule.get_runtime_release_schedule(id_="id")

print(result)
```

## update_runtime_release_schedule

The UPDATE operation modifies a set schedule for receiving updates.

- HTTP Method: `POST`
- Endpoint: `/RuntimeReleaseSchedule/{id}`

**Parameters**

| Name         | Type                                                          | Required | Description                                                   |
| :----------- | :------------------------------------------------------------ | :------- | :------------------------------------------------------------ |
| request_body | [RuntimeReleaseSchedule](../models/RuntimeReleaseSchedule.md) | ❌       | The request body.                                             |
| id\_         | str                                                           | ✅       | The ID of the container for which you want to set a schedule. |

**Return Type**

`RuntimeReleaseSchedule`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import RuntimeReleaseSchedule

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = RuntimeReleaseSchedule(
    atom_id="atomId",
    day_of_week="dayOfWeek",
    hour_of_day=6,
    schedule_type="NEVER",
    time_zone="timeZone"
)

result = sdk.runtime_release_schedule.update_runtime_release_schedule(
    request_body=request_body,
    id_="id"
)

print(result)
```

## delete_runtime_release_schedule

The DELETE operation sets the scheduleType to NEVER, meaning that the Runtime, Runtime cluster, or Runtime cloud receives updates only during the .

- HTTP Method: `DELETE`
- Endpoint: `/RuntimeReleaseSchedule/{id}`

**Parameters**

| Name | Type | Required | Description                                                   |
| :--- | :--- | :------- | :------------------------------------------------------------ |
| id\_ | str  | ✅       | The ID of the container for which you want to set a schedule. |

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.runtime_release_schedule.delete_runtime_release_schedule(id_="id")

print(result)
```

## bulk_runtime_release_schedule

- HTTP Method: `POST`
- Endpoint: `/RuntimeReleaseSchedule/bulk`

**Parameters**

| Name         | Type                                                                                | Required | Description       |
| :----------- | :---------------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [RuntimeReleaseScheduleBulkRequest](../models/RuntimeReleaseScheduleBulkRequest.md) | ❌       | The request body. |

**Return Type**

`RuntimeReleaseScheduleBulkResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import RuntimeReleaseScheduleBulkRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = RuntimeReleaseScheduleBulkRequest(
    request=[
        {
            "id_": "56789abc-def0-1234-5678-9abcdef01234"
        }
    ],
    type_="GET"
)

result = sdk.runtime_release_schedule.bulk_runtime_release_schedule(request_body=request_body)

print(result)
```

