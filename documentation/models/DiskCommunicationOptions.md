# DiskCommunicationOptions

**Properties**

| Name                         | Type                                         | Required | Description |
| :--------------------------- | :------------------------------------------- | :------- | :---------- |
| communication_setting        | DiskCommunicationOptionsCommunicationSetting | ❌       |             |
| disk_get_options             | DiskGetOptions                               | ❌       |             |
| disk_send_options            | DiskSendOptions                              | ❌       |             |
| shared_communication_channel | SharedCommunicationChannel                   | ❌       |             |

# DiskCommunicationOptionsCommunicationSetting

**Properties**

| Name      | Type | Required | Description |
| :-------- | :--- | :------- | :---------- |
| DEFAULT   | str  | ✅       | "default"   |
| CUSTOM    | str  | ✅       | "custom"    |
| COMPONENT | str  | ✅       | "component" |

