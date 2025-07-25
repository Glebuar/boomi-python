# AccountCloudAttachmentPropertiesService

A list of all methods in the `AccountCloudAttachmentPropertiesService` service. Click on the method name to view detailed information about that method.

| Methods                                                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| :-------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [update_account_cloud_attachment_properties](#update_account_cloud_attachment_properties)           | Modifies one or more Account Cloud attachment properties. - To update property values, include all property names that you want to modify including their new values in the request body you do not need to provide the full list of properties in the request. This action is equivalent to editing property values on the [Attachment quotas tab](https://help.boomi.com/docs/Atomsphere/Integration/Integration%20management/r-atm-Attachment_Quotas_tab_4fbc3fff-7aaf-4bbd-a2dc-25d0edb5189c) (Manage \> Cloud Management) in the user interface. - To ensure a successful request, you must provide valid property names and their accepted values in the request body. Otherwise, it returns an error. - The response returns a status code of 200 indicating a successful request. To verify updates made to a property, you can make a new GET request or view the Cloud attachment quotas tab (Manage \> Cloud Management) in the user interface. - To modify properties, you must be the owner of the private Runtime cloud, and both the Runtime cloud and its attachments must be online. |
| [async_get_account_cloud_attachment_properties](#async_get_account_cloud_attachment_properties)     | Use the GET operation to return and view a full list of Account Cloud attachment properties and their current values. This action is equivalent to viewing the [Attachment quotas](https://help.boomi.com/docs/Atomsphere/Integration/Integration%20management/r-atm-Attachment_Quotas_tab_4fbc3fff-7aaf-4bbd-a2dc-25d0edb5189c) tab (Manage \> Cloud Management) in the user interface. \>**Note:** The Cloud and attachments to which you are calling must be online. Cloud owners and users that own the Cloud attachments can use this operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [async_token_account_cloud_attachment_properties](#async_token_account_cloud_attachment_properties) | Send a second GET request with the token returned in the first GET request. The object returns a list of existing property names and values for the given account and Cloud. \>**Note:** The Cloud and attachments to which you are calling must be online. Cloud owners and users that own the Cloud attachments can use this operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

## update_account_cloud_attachment_properties

Modifies one or more Account Cloud attachment properties. - To update property values, include all property names that you want to modify including their new values in the request body you do not need to provide the full list of properties in the request. This action is equivalent to editing property values on the [Attachment quotas tab](https://help.boomi.com/docs/Atomsphere/Integration/Integration%20management/r-atm-Attachment_Quotas_tab_4fbc3fff-7aaf-4bbd-a2dc-25d0edb5189c) (Manage \> Cloud Management) in the user interface. - To ensure a successful request, you must provide valid property names and their accepted values in the request body. Otherwise, it returns an error. - The response returns a status code of 200 indicating a successful request. To verify updates made to a property, you can make a new GET request or view the Cloud attachment quotas tab (Manage \> Cloud Management) in the user interface. - To modify properties, you must be the owner of the private Runtime cloud, and both the Runtime cloud and its attachments must be online.

- HTTP Method: `POST`
- Endpoint: `/AccountCloudAttachmentProperties/{id}`

**Parameters**

| Name         | Type                                                                              | Required | Description       |
| :----------- | :-------------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [AccountCloudAttachmentProperties](../models/AccountCloudAttachmentProperties.md) | ❌       | The request body. |
| id\_         | str                                                                               | ✅       |                   |

**Return Type**

`AccountCloudAttachmentProperties`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import AccountCloudAttachmentProperties

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = AccountCloudAttachmentProperties(
    account_disk_usage=7,
    as2_workload="GENERAL",
    atom_input_size=1,
    atom_output_overflow_size=7,
    atom_working_overflow_size=9,
    cloud_account_execution_limit=2,
    cloud_account_execution_warning_offset=0,
    container_id="containerId",
    download_runnerlogs=False,
    enable_account_data_archiving=False,
    enable_atom_worker_warmup=False,
    flow_control_parallel_process_type_override="NONE",
    http_request_rate=1,
    http_workload="GENERAL",
    listener_max_concurrent_executions=2,
    max_connector_track_docs=3,
    min_numberof_atom_workers=1,
    numberof_atom_workers=3,
    queue_incoming_message_rate_limit=1,
    session_id="sessionId",
    status_code=6,
    test_mode_max_doc_bytes=6,
    test_mode_max_docs=6,
    worker_elastic_scaling_threshold=3,
    worker_max_execution_time=8,
    worker_max_general_execution_time=7,
    worker_max_queued_executions=8,
    worker_max_running_executions=10,
    worker_queued_execution_timeout=10
)

result = sdk.account_cloud_attachment_properties.update_account_cloud_attachment_properties(
    request_body=request_body,
    id_="id"
)

print(result)
```

## async_get_account_cloud_attachment_properties

Use the GET operation to return and view a full list of Account Cloud attachment properties and their current values. This action is equivalent to viewing the [Attachment quotas](https://help.boomi.com/docs/Atomsphere/Integration/Integration%20management/r-atm-Attachment_Quotas_tab_4fbc3fff-7aaf-4bbd-a2dc-25d0edb5189c) tab (Manage \> Cloud Management) in the user interface. \>**Note:** The Cloud and attachments to which you are calling must be online. Cloud owners and users that own the Cloud attachments can use this operation.

- HTTP Method: `GET`
- Endpoint: `/async/AccountCloudAttachmentProperties/{id}`

**Parameters**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| id\_ | str  | ✅       |             |

**Return Type**

`AsyncOperationTokenResult`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.account_cloud_attachment_properties.async_get_account_cloud_attachment_properties(id_="id")

print(result)
```

## async_token_account_cloud_attachment_properties

Send a second GET request with the token returned in the first GET request. The object returns a list of existing property names and values for the given account and Cloud. \>**Note:** The Cloud and attachments to which you are calling must be online. Cloud owners and users that own the Cloud attachments can use this operation.

- HTTP Method: `GET`
- Endpoint: `/async/AccountCloudAttachmentProperties/response/{token}`

**Parameters**

| Name  | Type | Required | Description                                                 |
| :---- | :--- | :------- | :---------------------------------------------------------- |
| token | str  | ✅       | Takes in the token from a previous call to return a result. |

**Return Type**

`AccountCloudAttachmentPropertiesAsyncResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.account_cloud_attachment_properties.async_token_account_cloud_attachment_properties(token="token")

print(result)
```

