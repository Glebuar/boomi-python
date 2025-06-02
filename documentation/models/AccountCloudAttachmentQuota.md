# AccountCloudAttachmentQuota

**Properties**

| Name                | Type | Required | Description                                                                                                                                                                                                 |
| :------------------ | :--- | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id          | str  | ❌       | The ID of the account authorizing the call.                                                                                                                                                                 |
| cloud_id            | str  | ❌       | The ID of the Runtime cloud that you want to get, add, edit, or delete a Cloud quota.                                                                                                                       |
| id\_                | str  | ❌       | A unique ID generated for a newly created or recently updated Cloud quota \(using the Account Cloud Attachment quota object\). You can use this ID to get a Cloud quota for an account's specific Cloud ID. |
| max_atom_attachment | int  | ❌       | The number of Runtime attachments that you want to set on the Cloud quota.                                                                                                                                  |

