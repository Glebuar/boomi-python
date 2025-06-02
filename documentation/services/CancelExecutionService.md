# CancelExecutionService

A list of all methods in the `CancelExecutionService` service. Click on the method name to view detailed information about that method.

| Methods                                       | Description                                                                             |
| :-------------------------------------------- | :-------------------------------------------------------------------------------------- |
| [get_cancel_execution](#get_cancel_execution) | This API is supported by the Platform Partner APIs. Refer to the Partner API Reference. |

## get_cancel_execution

This API is supported by the Platform Partner APIs. Refer to the Partner API Reference.

- HTTP Method: `GET`
- Endpoint: `/CancelExecution`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.cancel_execution.get_cancel_execution()

print(result)
```

