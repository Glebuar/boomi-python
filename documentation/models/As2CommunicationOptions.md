# As2CommunicationOptions

**Properties**

| Name                         | Type                                        | Required | Description |
| :--------------------------- | :------------------------------------------ | :------- | :---------- |
| as2_default_partner_settings | As2SendSettings                             | ❌       |             |
| as2_receive_options          | As2ReceiveOptions                           | ❌       |             |
| as2_send_options             | As2SendOptions                              | ❌       |             |
| as2_send_settings            | As2SendSettings                             | ❌       |             |
| communication_setting        | As2CommunicationOptionsCommunicationSetting | ❌       |             |
| shared_communication_channel | SharedCommunicationChannel                  | ❌       |             |

# As2CommunicationOptionsCommunicationSetting

**Properties**

| Name      | Type | Required | Description |
| :-------- | :--- | :------- | :---------- |
| DEFAULT   | str  | ✅       | "default"   |
| CUSTOM    | str  | ✅       | "custom"    |
| COMPONENT | str  | ✅       | "component" |

