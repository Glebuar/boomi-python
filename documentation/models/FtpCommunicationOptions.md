# FtpCommunicationOptions

**Properties**

| Name                         | Type                                        | Required | Description |
| :--------------------------- | :------------------------------------------ | :------- | :---------- |
| communication_setting        | FtpCommunicationOptionsCommunicationSetting | ❌       |             |
| ftp_get_options              | FtpGetOptions                               | ❌       |             |
| ftp_send_options             | FtpSendOptions                              | ❌       |             |
| ftp_settings                 | FtpSettings                                 | ❌       |             |
| shared_communication_channel | SharedCommunicationChannel                  | ❌       |             |

# FtpCommunicationOptionsCommunicationSetting

**Properties**

| Name      | Type | Required | Description |
| :-------- | :--- | :------- | :---------- |
| DEFAULT   | str  | ✅       | "default"   |
| CUSTOM    | str  | ✅       | "custom"    |
| COMPONENT | str  | ✅       | "component" |

