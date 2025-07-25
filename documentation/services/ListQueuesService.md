# ListQueuesService

A list of all methods in the `ListQueuesService` service. Click on the method name to view detailed information about that method.

| Methods                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| :-------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [async_token_list_queues](#async_token_list_queues) | After receiving a 200 status code response, send a second GET request where {accountId} is the ID of the account authenticating the request and sessionId is the ID provided in the initial response.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [async_get_list_queues](#async_get_list_queues)     | To retrieve a list of message queues, Send an HTTP GET where accountId is the account that you are authenticating with and containerId is the ID of the Runtime, Runtime cluster, or Runtime cloud which owns the message queue that you want to retrieve. \>**Note:** You can find the Account ID for an account by navigating to Settings \> Account Information and Setup in the user interface. Additionally, you can find the container ID by navigating to Manage \> Runtime Management and viewing the Runtime ID value on the Runtime Information panel for a selected Runtime, Runtime cluster, or Runtime cloud. |

## async_token_list_queues

After receiving a 200 status code response, send a second GET request where {accountId} is the ID of the account authenticating the request and sessionId is the ID provided in the initial response.

- HTTP Method: `GET`
- Endpoint: `/async/ListQueues/response/{token}`

**Parameters**

| Name  | Type | Required | Description                                                 |
| :---- | :--- | :------- | :---------------------------------------------------------- |
| token | str  | ✅       | Takes in the token from a previous call to return a result. |

**Return Type**

`ListQueuesAsyncResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.list_queues.async_token_list_queues(token="token")

print(result)
```

## async_get_list_queues

To retrieve a list of message queues, Send an HTTP GET where accountId is the account that you are authenticating with and containerId is the ID of the Runtime, Runtime cluster, or Runtime cloud which owns the message queue that you want to retrieve. \>**Note:** You can find the Account ID for an account by navigating to Settings \> Account Information and Setup in the user interface. Additionally, you can find the container ID by navigating to Manage \> Runtime Management and viewing the Runtime ID value on the Runtime Information panel for a selected Runtime, Runtime cluster, or Runtime cloud.

- HTTP Method: `GET`
- Endpoint: `/async/ListQueues/{id}`

**Parameters**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| id\_ | str  | ✅       |             |

**Return Type**

`AsyncOperationTokenResult`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.list_queues.async_get_list_queues(id_="id")

print(result)
```

