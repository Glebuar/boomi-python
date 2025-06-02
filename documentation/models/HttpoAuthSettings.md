# HttpoAuthSettings

**Properties**

| Name                        | Type            | Required | Description |
| :-------------------------- | :-------------- | :------- | :---------- |
| access_token                | str             | ❌       |             |
| access_token_url            | str             | ❌       |             |
| authorization_url           | str             | ❌       |             |
| consumer_key                | str             | ❌       |             |
| consumer_secret             | str             | ❌       |             |
| realm                       | str             | ❌       |             |
| request_token_url           | str             | ❌       |             |
| signature_method            | SignatureMethod | ❌       |             |
| suppress_blank_access_token | bool            | ❌       |             |
| token_secret                | str             | ❌       |             |

# SignatureMethod

**Properties**

| Name   | Type | Required | Description |
| :----- | :--- | :------- | :---------- |
| SHA1   | str  | ✅       | "SHA1"      |
| SHA256 | str  | ✅       | "SHA256"    |

