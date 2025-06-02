# HttpSettings

**Properties**

| Name                 | Type                           | Required | Description |
| :------------------- | :----------------------------- | :------- | :---------- |
| http_auth_settings   | HttpAuthSettings               | ✅       |             |
| httpssl_options      | HttpsslOptions                 | ✅       |             |
| httpo_auth2_settings | HttpoAuth2Settings             | ❌       |             |
| httpo_auth_settings  | HttpoAuthSettings              | ❌       |             |
| authentication_type  | HttpSettingsAuthenticationType | ❌       |             |
| connect_timeout      | int                            | ❌       |             |
| cookie_scope         | CookieScope                    | ❌       |             |
| read_timeout         | int                            | ❌       |             |
| url                  | str                            | ❌       |             |
| use_basic_auth       | bool                           | ❌       |             |
| use_custom_auth      | bool                           | ❌       |             |
| use_default_settings | bool                           | ❌       |             |

# HttpSettingsAuthenticationType

**Properties**

| Name           | Type | Required | Description       |
| :------------- | :--- | :------- | :---------------- |
| NONE           | str  | ✅       | "NONE"            |
| BASIC          | str  | ✅       | "BASIC"           |
| PASSWORDDIGEST | str  | ✅       | "PASSWORD_DIGEST" |
| CUSTOM         | str  | ✅       | "CUSTOM"          |
| OAUTH          | str  | ✅       | "OAUTH"           |
| OAUTH2         | str  | ✅       | "OAUTH2"          |

# CookieScope

**Properties**

| Name           | Type | Required | Description       |
| :------------- | :--- | :------- | :---------------- |
| IGNORED        | str  | ✅       | "IGNORED"         |
| GLOBAL         | str  | ✅       | "GLOBAL"          |
| CONNECTORSHAPE | str  | ✅       | "CONNECTOR_SHAPE" |

