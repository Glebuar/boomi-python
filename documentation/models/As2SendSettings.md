# As2SendSettings

**Properties**

| Name                   | Type                              | Required | Description |
| :--------------------- | :-------------------------------- | :------- | :---------- |
| client_ssl_certificate | PrivateCertificate                | ✅       |             |
| ssl_certificate        | PublicCertificate                 | ✅       |             |
| url                    | str                               | ✅       |             |
| auth_settings          | As2BasicAuthInfo                  | ❌       |             |
| authentication_type    | As2SendSettingsAuthenticationType | ❌       |             |
| use_default_settings   | bool                              | ❌       |             |
| verify_hostname        | bool                              | ❌       |             |

# As2SendSettingsAuthenticationType

**Properties**

| Name  | Type | Required | Description |
| :---- | :--- | :------- | :---------- |
| NONE  | str  | ✅       | "NONE"      |
| BASIC | str  | ✅       | "BASIC"     |

