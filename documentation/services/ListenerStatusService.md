# ListenerStatusService

A list of all methods in the `ListenerStatusService` service. Click on the method name to view detailed information about that method.

| Methods                                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| :---------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [async_get_listener_status](#async_get_listener_status)     | Send an HTTP POST where {accountId} is the ID of the authenticating account for the request. \>**Note:** For backward compatibility, Boomi continues to support the legacy URL: https://api.boomi.com/api/rest/v1/accountId/ListenerStatus/query/async. For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging). |
| [async_token_listener_status](#async_token_listener_status) | The ordinary GET operation retrieves async results from the QUERY. Send an HTTP GET where {accountId} is the account that you are authenticating with and {token} is the listener status token returned by your QUERY request. \>**Note:** For backward compatibility, Boomi continues to support the legacy URL: https://api.boomi.com/api/rest/v1/accountId/ListenerStatus/query/async.                                                                                                               |

## async_get_listener_status

Send an HTTP POST where {accountId} is the ID of the authenticating account for the request. \>**Note:** For backward compatibility, Boomi continues to support the legacy URL: https://api.boomi.com/api/rest/v1/accountId/ListenerStatus/query/async. For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/async/ListenerStatus/query`

**Parameters**

| Name         | Type                                                                | Required | Description       |
| :----------- | :------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [ListenerStatusQueryConfig](../models/ListenerStatusQueryConfig.md) | ❌       | The request body. |

**Return Type**

`AsyncOperationTokenResult`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import ListenerStatusQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = ListenerStatusQueryConfig(
    query_filter={
        "expression": {
            "argument": [
                "argument"
            ],
            "operator": "EQUALS",
            "property": "listenerId"
        }
    }
)

result = sdk.listener_status.async_get_listener_status(request_body=request_body)

print(result)
```

## async_token_listener_status

The ordinary GET operation retrieves async results from the QUERY. Send an HTTP GET where {accountId} is the account that you are authenticating with and {token} is the listener status token returned by your QUERY request. \>**Note:** For backward compatibility, Boomi continues to support the legacy URL: https://api.boomi.com/api/rest/v1/accountId/ListenerStatus/query/async.

- HTTP Method: `GET`
- Endpoint: `/async/ListenerStatus/response/{token}`

**Parameters**

| Name  | Type | Required | Description                                                 |
| :---- | :--- | :------- | :---------------------------------------------------------- |
| token | str  | ✅       | Takes in the token from a previous call to return a result. |

**Return Type**

`ListenerStatusAsyncResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.listener_status.async_token_listener_status(token="token")

print(result)
```

