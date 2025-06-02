# SftpCommunicationOptions

**Properties**

| Name                         | Type                                         | Required | Description |
| :--------------------------- | :------------------------------------------- | :------- | :---------- |
| communication_setting        | SftpCommunicationOptionsCommunicationSetting | ❌       |             |
| sftp_get_options             | SftpGetOptions                               | ❌       |             |
| sftp_send_options            | SftpSendOptions                              | ❌       |             |
| sftp_settings                | SftpSettings                                 | ❌       |             |
| shared_communication_channel | SharedCommunicationChannel                   | ❌       |             |

# SftpCommunicationOptionsCommunicationSetting

**Properties**

| Name      | Type | Required | Description |
| :-------- | :--- | :------- | :---------- |
| DEFAULT   | str  | ✅       | "default"   |
| CUSTOM    | str  | ✅       | "custom"    |
| COMPONENT | str  | ✅       | "component" |

