# HttpCommunicationOptions

**Properties**

| Name                         | Type                                         | Required | Description |
| :--------------------------- | :------------------------------------------- | :------- | :---------- |
| communication_setting        | HttpCommunicationOptionsCommunicationSetting | ❌       |             |
| http_get_options             | HttpGetOptions                               | ❌       |             |
| http_listen_options          | HttpListenOptions                            | ❌       |             |
| http_send_options            | HttpSendOptions                              | ❌       |             |
| http_settings                | HttpSettings                                 | ❌       |             |
| shared_communication_channel | SharedCommunicationChannel                   | ❌       |             |

# HttpCommunicationOptionsCommunicationSetting

**Properties**

| Name      | Type | Required | Description |
| :-------- | :--- | :------- | :---------- |
| DEFAULT   | str  | ✅       | "default"   |
| CUSTOM    | str  | ✅       | "custom"    |
| COMPONENT | str  | ✅       | "component" |

