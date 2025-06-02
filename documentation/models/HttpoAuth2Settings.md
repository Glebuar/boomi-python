# HttpoAuth2Settings

**Properties**

| Name                         | Type                  | Required | Description |
| :--------------------------- | :-------------------- | :------- | :---------- |
| access_token_endpoint        | HttpEndpoint          | ✅       |             |
| access_token_parameters      | HttpRequestParameters | ✅       |             |
| authorization_parameters     | HttpRequestParameters | ✅       |             |
| authorization_token_endpoint | HttpEndpoint          | ✅       |             |
| credentials                  | HttpoAuthCredentials  | ✅       |             |
| scope                        | str                   | ✅       |             |
| grant_type                   | GrantType             | ❌       |             |

# GrantType

**Properties**

| Name              | Type | Required | Description          |
| :---------------- | :--- | :------- | :------------------- |
| CODE              | str  | ✅       | "code"               |
| CLIENTCREDENTIALS | str  | ✅       | "client_credentials" |
| PASSWORD          | str  | ✅       | "password"           |

