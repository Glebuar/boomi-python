# OftpCommunicationOptions

**Properties**

| Name                         | Type                                         | Required | Description |
| :--------------------------- | :------------------------------------------- | :------- | :---------- |
| communication_setting        | OftpCommunicationOptionsCommunicationSetting | ❌       |             |
| oftp_connection_settings     | OftpConnectionSettings                       | ❌       |             |
| oftp_get_options             | OftpGetOptions                               | ❌       |             |
| oftp_send_options            | OftpSendOptions                              | ❌       |             |
| oftp_server_listen_options   | OftpListenOptions                            | ❌       |             |
| shared_communication_channel | SharedCommunicationChannel                   | ❌       |             |

# OftpCommunicationOptionsCommunicationSetting

**Properties**

| Name      | Type | Required | Description |
| :-------- | :--- | :------- | :---------- |
| DEFAULT   | str  | ✅       | "default"   |
| CUSTOM    | str  | ✅       | "custom"    |
| COMPONENT | str  | ✅       | "component" |

