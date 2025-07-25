# AccountCloudAttachmentQuotaService

A list of all methods in the `AccountCloudAttachmentQuotaService` service. Click on the method name to view detailed information about that method.

| Methods                                                                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| :------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_account_cloud_attachment_quota](#create_account_cloud_attachment_quota) | - Use the CREATE operation to create a new Cloud quota and determine the maximum number of Runtime attachments that you can create on the account. - You can use the CREATE or UPDATE operations interchangeably to edit a Cloud quota value. Both operations can act as an update after creating the quota. - CREATE and UPDATE use the same REST endpoint, as seen in the next section of sample code REST calls. When calling the endpoint for an account that has a quota set, the endpoint acts as an update and modifies the existing value, as explained in the previous item. When calling the endpoint for an account that does not already have a quota set, the endpoint creates a new quota. - You cannot set the Cloud quota less than the number of attachments that currently exist on the account, unless you are setting the value to -1 for unlimited. Attempting to do so returns an error. - The CREATE operation returns an id value that you can use in a GET operation to retrieve the existing quota for a specific account's Cloud ID. |
| [get_account_cloud_attachment_quota](#get_account_cloud_attachment_quota)       | Retrieves the Cloud quota value currently existing for a Cloud ID on a specific account. The GET operation requires an additional ID (id), and differs from the `cloudId` and `accountId`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [update_account_cloud_attachment_quota](#update_account_cloud_attachment_quota) | Edit the number of Runtime attachments that you can create on the given account. Specify the IDs of both the account and the Runtime cloud that you want to update. You cannot set the Cloud quota less than the number of attachments that currently exist on the account, unless you are setting the value to -1 for unlimited. Attempting to do so returns an error.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [delete_account_cloud_attachment_quota](#delete_account_cloud_attachment_quota) | Deletes a Cloud quota for a given account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [bulk_account_cloud_attachment_quota](#bulk_account_cloud_attachment_quota)     | To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

## create_account_cloud_attachment_quota

- Use the CREATE operation to create a new Cloud quota and determine the maximum number of Runtime attachments that you can create on the account. - You can use the CREATE or UPDATE operations interchangeably to edit a Cloud quota value. Both operations can act as an update after creating the quota. - CREATE and UPDATE use the same REST endpoint, as seen in the next section of sample code REST calls. When calling the endpoint for an account that has a quota set, the endpoint acts as an update and modifies the existing value, as explained in the previous item. When calling the endpoint for an account that does not already have a quota set, the endpoint creates a new quota. - You cannot set the Cloud quota less than the number of attachments that currently exist on the account, unless you are setting the value to -1 for unlimited. Attempting to do so returns an error. - The CREATE operation returns an id value that you can use in a GET operation to retrieve the existing quota for a specific account's Cloud ID.

- HTTP Method: `POST`
- Endpoint: `/AccountCloudAttachmentQuota`

**Parameters**

| Name         | Type                                                                    | Required | Description       |
| :----------- | :---------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [AccountCloudAttachmentQuota](../models/AccountCloudAttachmentQuota.md) | ❌       | The request body. |

**Return Type**

`AccountCloudAttachmentQuota`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import AccountCloudAttachmentQuota

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = AccountCloudAttachmentQuota(
    account_id="accountId",
    cloud_id="cloudId",
    id_="id",
    max_atom_attachment=10
)

result = sdk.account_cloud_attachment_quota.create_account_cloud_attachment_quota(request_body=request_body)

print(result)
```

## get_account_cloud_attachment_quota

Retrieves the Cloud quota value currently existing for a Cloud ID on a specific account. The GET operation requires an additional ID (id), and differs from the `cloudId` and `accountId`.

- HTTP Method: `GET`
- Endpoint: `/AccountCloudAttachmentQuota/{id}`

**Parameters**

| Name | Type | Required | Description                                                                                                                                                                                               |
| :--- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id\_ | str  | ✅       | A unique ID generated for a newly created or recently updated Cloud quota (using the Account Cloud Attachment quota object). You can use this ID to get a Cloud quota for an account's specific Cloud ID. |

**Return Type**

`AccountCloudAttachmentQuota`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.account_cloud_attachment_quota.get_account_cloud_attachment_quota(id_="id")

print(result)
```

## update_account_cloud_attachment_quota

Edit the number of Runtime attachments that you can create on the given account. Specify the IDs of both the account and the Runtime cloud that you want to update. You cannot set the Cloud quota less than the number of attachments that currently exist on the account, unless you are setting the value to -1 for unlimited. Attempting to do so returns an error.

- HTTP Method: `POST`
- Endpoint: `/AccountCloudAttachmentQuota/{id}`

**Parameters**

| Name         | Type                                                                    | Required | Description                                                                                                                                                                                               |
| :----------- | :---------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [AccountCloudAttachmentQuota](../models/AccountCloudAttachmentQuota.md) | ❌       | The request body.                                                                                                                                                                                         |
| id\_         | str                                                                     | ✅       | A unique ID generated for a newly created or recently updated Cloud quota (using the Account Cloud Attachment quota object). You can use this ID to get a Cloud quota for an account's specific Cloud ID. |

**Return Type**

`AccountCloudAttachmentQuota`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import AccountCloudAttachmentQuota

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = AccountCloudAttachmentQuota(
    account_id="accountId",
    cloud_id="cloudId",
    id_="id",
    max_atom_attachment=10
)

result = sdk.account_cloud_attachment_quota.update_account_cloud_attachment_quota(
    request_body=request_body,
    id_="id"
)

print(result)
```

## delete_account_cloud_attachment_quota

Deletes a Cloud quota for a given account.

- HTTP Method: `DELETE`
- Endpoint: `/AccountCloudAttachmentQuota/{id}`

**Parameters**

| Name | Type | Required | Description                                                                                                                                                                                               |
| :--- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id\_ | str  | ✅       | A unique ID generated for a newly created or recently updated Cloud quota (using the Account Cloud Attachment quota object). You can use this ID to get a Cloud quota for an account's specific Cloud ID. |

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.account_cloud_attachment_quota.delete_account_cloud_attachment_quota(id_="id")

print(result)
```

## bulk_account_cloud_attachment_quota

To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

- HTTP Method: `POST`
- Endpoint: `/AccountCloudAttachmentQuota/bulk`

**Parameters**

| Name         | Type                                                                                          | Required | Description       |
| :----------- | :-------------------------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [AccountCloudAttachmentQuotaBulkRequest](../models/AccountCloudAttachmentQuotaBulkRequest.md) | ❌       | The request body. |

**Return Type**

`AccountCloudAttachmentQuotaBulkResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import AccountCloudAttachmentQuotaBulkRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = AccountCloudAttachmentQuotaBulkRequest(
    request=[
        {
            "id_": "56789abc-def0-1234-5678-9abcdef01234"
        }
    ],
    type_="GET"
)

result = sdk.account_cloud_attachment_quota.bulk_account_cloud_attachment_quota(request_body=request_body)

print(result)
```

