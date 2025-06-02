# ComponentDiffRequestService

A list of all methods in the `ComponentDiffRequestService` service. Click on the method name to view detailed information about that method.

| Methods                                                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                   |
| :-------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_component_diff_request](#create_component_diff_request) | Contains a diff visualization option to help understand the differences between component versions. For more information, refer to the Postman article [Visualize request responses using Postman Visualizer](https://learning.postman.com/docs/sending-requests/response-data/visualizer/).                                                                                                                                  |
| [get_component_diff_request](#get_component_diff_request)       | If you use Postman to make API calls, the GET response contains a diff visualization option to help understand the differences between component versions. For more information, refer to the Postman article [Visualize request responses using Postman Visualizer](https://learning.postman.com/docs/sending-requests/response-data/visualizer/). The Postman visualization feature currently supports only JSON responses. |
| [bulk_component_diff_request](#bulk_component_diff_request)     | To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).                                                                                                                                                                                                                                                                                                                        |

## create_component_diff_request

Contains a diff visualization option to help understand the differences between component versions. For more information, refer to the Postman article [Visualize request responses using Postman Visualizer](https://learning.postman.com/docs/sending-requests/response-data/visualizer/).

- HTTP Method: `POST`
- Endpoint: `/ComponentDiffRequest`

**Parameters**

| Name         | Type                                                      | Required | Description       |
| :----------- | :-------------------------------------------------------- | :------- | :---------------- |
| request_body | [ComponentDiffRequest](../models/ComponentDiffRequest.md) | ❌       | The request body. |

**Return Type**

`ComponentDiffResponseCreate`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import ComponentDiffRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = ComponentDiffRequest(
    comp_diff_config={
        "comp_diff_element": [
            {
                "comp_diff_attribute": [
                    {
                        "idpart": False,
                        "ignored": True,
                        "name": "name"
                    }
                ],
                "ignored": False,
                "name": "name",
                "ordered": False,
                "parent": "parent"
            }
        ],
        "component_type": "certificate"
    },
    component_id="componentId",
    source_version=7,
    target_version=7
)

result = sdk.component_diff_request.create_component_diff_request(request_body=request_body)

print(result)
```

## get_component_diff_request

If you use Postman to make API calls, the GET response contains a diff visualization option to help understand the differences between component versions. For more information, refer to the Postman article [Visualize request responses using Postman Visualizer](https://learning.postman.com/docs/sending-requests/response-data/visualizer/). The Postman visualization feature currently supports only JSON responses.

- HTTP Method: `GET`
- Endpoint: `/ComponentDiffRequest/{componentId}`

**Parameters**

| Name         | Type | Required | Description                                                     |
| :----------- | :--- | :------- | :-------------------------------------------------------------- |
| component_id | str  | ✅       | The ID of the component for which you want to compare versions. |

**Return Type**

`ComponentDiffRequest`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.component_diff_request.get_component_diff_request(component_id="componentId")

print(result)
```

## bulk_component_diff_request

To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

- HTTP Method: `POST`
- Endpoint: `/ComponentDiffRequest/bulk`

**Parameters**

| Name         | Type                                                                            | Required | Description       |
| :----------- | :------------------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [ComponentDiffRequestBulkRequest](../models/ComponentDiffRequestBulkRequest.md) | ❌       | The request body. |

**Return Type**

`ComponentDiffRequestBulkResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import ComponentDiffRequestBulkRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = ComponentDiffRequestBulkRequest(
    request=[
        {
            "id_": "56789abc-def0-1234-5678-9abcdef01234"
        }
    ],
    type_="GET"
)

result = sdk.component_diff_request.bulk_component_diff_request(request_body=request_body)

print(result)
```

