# ExecutionRequestService

A list of all methods in the `ExecutionRequestService` service. Click on the method name to view detailed information about that method.

| Methods                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| :---------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_execution_request](#create_execution_request) | Submits the process to run and returns results immediately. The operation does not wait for the run to complete. - The Execution Request response returns a requestID, which you use to make a subsequent call to the [Execution Record object](/api/platformapi#tag/ExecutionRecord) to retrieve detailed information about the process run. - This operation returns an error when the client: - Fails authentication or does not have the correct permissions - Supplies an invalid Account ID - Supplies an invalid Runtime ID - Attempts to reach a deleted Atom - Supplies an invalid Process ID - Missing privileges to run processes on the given Runtime or its associated Environment. |

## create_execution_request

Submits the process to run and returns results immediately. The operation does not wait for the run to complete. - The Execution Request response returns a requestID, which you use to make a subsequent call to the [Execution Record object](/api/platformapi#tag/ExecutionRecord) to retrieve detailed information about the process run. - This operation returns an error when the client: - Fails authentication or does not have the correct permissions - Supplies an invalid Account ID - Supplies an invalid Runtime ID - Attempts to reach a deleted Atom - Supplies an invalid Process ID - Missing privileges to run processes on the given Runtime or its associated Environment.

- HTTP Method: `POST`
- Endpoint: `/ExecutionRequest`

**Parameters**

| Name         | Type                                              | Required | Description       |
| :----------- | :------------------------------------------------ | :------- | :---------------- |
| request_body | [ExecutionRequest](../models/ExecutionRequest.md) | ❌       | The request body. |

**Return Type**

`ExecutionRequest`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import ExecutionRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = ExecutionRequest(
    dynamic_process_properties={
        "dynamic_process_property": [
            {
                "name": "name",
                "value": "value"
            }
        ]
    },
    process_properties={
        "process_property": [
            {
                "process_property_value": [
                    {
                        "component_override": False,
                        "encrypted_value_set": False,
                        "key": "key",
                        "label": "label",
                        "use_default": True,
                        "uses_encryption": False,
                        "validate": False,
                        "value": "value"
                    }
                ],
                "component_id": "componentId"
            }
        ]
    },
    atom_id="3456789a-bcde-f0123-4567-89abcdef012",
    process_id="789abcde-f012-3456-789a-bcdef0123456",
    process_name="processName",
    record_url="https://api.boomi.com/api/rest/v1/account1234/ExecutionRecord/async/executionrecord-110b23f4-567a-8d90-1234-56789e0b123d",
    request_id="executionrecord-110b23f4-567a-8d90-1234-56789e0b123d"
)

result = sdk.execution_request.create_execution_request(request_body=request_body)

print(result)
```

