# DeploymentService

A list of all methods in the `DeploymentService` service. Click on the method name to view detailed information about that method.

| Methods                                                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| :-------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_deployment](#create_deployment)                                                 | The Deployment object is a deprecated API and should no longer be used. Boomi recommends that you take advantage of the API functionality provided by the [Packaged Component](https://help.boomi.com/docs/Atomsphere/Integration/AtomSphere%20API/r-atm-Packaged_Component_object_66fa92c8-948f-46c6-a521-3927ab431c84) and [Deployed Package objects](https://help.boomi.com/docs/Atomsphere/Integration/AtomSphere%20API/r-atm-Deployed_Package_object_897b5068-6daa-44e4-bf04-7e25385157a8) instead. |
| [get_deployment](#get_deployment)                                                       | The Deployment object is a deprecated API and should no longer be used. Boomi recommends that you take advantage of the API functionality provided by the [Packaged Component](https://help.boomi.com/docs/Atomsphere/Integration/AtomSphere%20API/r-atm-Packaged_Component_object_66fa92c8-948f-46c6-a521-3927ab431c84) and [Deployed Package objects](https://help.boomi.com/docs/Atomsphere/Integration/AtomSphere%20API/r-atm-Deployed_Package_object_897b5068-6daa-44e4-bf04-7e25385157a8) instead. |
| [bulk_deployment](#bulk_deployment)                                                     | To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).                                                                                                                                                                                                                                                                                                                                                                                                   |
| [query_deployment](#query_deployment)                                                   | For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                                                                                                          |
| [query_more_deployment](#query_more_deployment)                                         | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                                                                                                                                                                                                                                                           |
| [query_process_environment_attachment](#query_process_environment_attachment)           | For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                                                                                                          |
| [query_more_process_environment_attachment](#query_more_process_environment_attachment) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                                                                                                                                                                                                                                                           |
| [delete_process_environment_attachment](#delete_process_environment_attachment)         | Detaches a process from an environment where the attachment is specified by the conceptual Process Environment Attachment object ID.                                                                                                                                                                                                                                                                                                                                                                     |

## create_deployment

The Deployment object is a deprecated API and should no longer be used. Boomi recommends that you take advantage of the API functionality provided by the [Packaged Component](https://help.boomi.com/docs/Atomsphere/Integration/AtomSphere%20API/r-atm-Packaged_Component_object_66fa92c8-948f-46c6-a521-3927ab431c84) and [Deployed Package objects](https://help.boomi.com/docs/Atomsphere/Integration/AtomSphere%20API/r-atm-Deployed_Package_object_897b5068-6daa-44e4-bf04-7e25385157a8) instead.

- HTTP Method: `POST`
- Endpoint: `/Deployment`

**Parameters**

| Name         | Type                                  | Required | Description       |
| :----------- | :------------------------------------ | :------- | :---------------- |
| request_body | [Deployment](../models/Deployment.md) | ❌       | The request body. |

**Return Type**

`Deployment`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import Deployment

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = Deployment(
    component_id="789abcde-f012-3456-789a-bcdef0123456",
    component_type="componentType",
    current="true",
    deployed_by="user123company.biz",
    deployed_on="2013-08-13T17:13:46Z",
    digest="abb98d1a5b659afbe77cc361cb255c8b",
    environment_id="456789ab-cdef-0123-4567-89abcdef0123",
    id_="89abcdef-0123-4567-89ab-cdef01234567",
    listener_status="RUNNING",
    message="message",
    notes="Added Message step",
    process_id="processId",
    version="54"
)

result = sdk.deployment.create_deployment(request_body=request_body)

print(result)
```

## get_deployment

The Deployment object is a deprecated API and should no longer be used. Boomi recommends that you take advantage of the API functionality provided by the [Packaged Component](https://help.boomi.com/docs/Atomsphere/Integration/AtomSphere%20API/r-atm-Packaged_Component_object_66fa92c8-948f-46c6-a521-3927ab431c84) and [Deployed Package objects](https://help.boomi.com/docs/Atomsphere/Integration/AtomSphere%20API/r-atm-Deployed_Package_object_897b5068-6daa-44e4-bf04-7e25385157a8) instead.

- HTTP Method: `GET`
- Endpoint: `/Deployment/{id}`

**Parameters**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| id\_ | str  | ✅       |             |

**Return Type**

`Deployment`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.deployment.get_deployment(id_="id")

print(result)
```

## bulk_deployment

To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

- HTTP Method: `POST`
- Endpoint: `/Deployment/bulk`

**Parameters**

| Name         | Type                                                        | Required | Description       |
| :----------- | :---------------------------------------------------------- | :------- | :---------------- |
| request_body | [DeploymentBulkRequest](../models/DeploymentBulkRequest.md) | ❌       | The request body. |

**Return Type**

`DeploymentBulkResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import DeploymentBulkRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = DeploymentBulkRequest(
    request=[
        {
            "id_": "56789abc-def0-1234-5678-9abcdef01234"
        }
    ],
    type_="GET"
)

result = sdk.deployment.bulk_deployment(request_body=request_body)

print(result)
```

## query_deployment

For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/Deployment/query`

**Parameters**

| Name         | Type                                                        | Required | Description       |
| :----------- | :---------------------------------------------------------- | :------- | :---------------- |
| request_body | [DeploymentQueryConfig](../models/DeploymentQueryConfig.md) | ❌       | The request body. |

**Return Type**

`DeploymentQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import DeploymentQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = DeploymentQueryConfig(
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

result = sdk.deployment.query_deployment(request_body=request_body)

print(result)
```

## query_more_deployment

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/Deployment/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`DeploymentQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "sint dolore e"

result = sdk.deployment.query_more_deployment(request_body=request_body)

print(result)
```

## query_process_environment_attachment

For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/ProcessEnvironmentAttachment/query`

**Parameters**

| Name         | Type                                                                                            | Required | Description       |
| :----------- | :---------------------------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [ProcessEnvironmentAttachmentQueryConfig](../models/ProcessEnvironmentAttachmentQueryConfig.md) | ❌       | The request body. |

**Return Type**

`ProcessEnvironmentAttachmentQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import ProcessEnvironmentAttachmentQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = ProcessEnvironmentAttachmentQueryConfig(
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

result = sdk.deployment.query_process_environment_attachment(request_body=request_body)

print(result)
```

## query_more_process_environment_attachment

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/ProcessEnvironmentAttachment/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`ProcessEnvironmentAttachmentQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "consec"

result = sdk.deployment.query_more_process_environment_attachment(request_body=request_body)

print(result)
```

## delete_process_environment_attachment

Detaches a process from an environment where the attachment is specified by the conceptual Process Environment Attachment object ID.

- HTTP Method: `DELETE`
- Endpoint: `/ProcessEnvironmentAttachment/{id}`

**Parameters**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| id\_ | str  | ✅       |             |

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.deployment.delete_process_environment_attachment(id_="id")

print(result)
```

