# TradingPartnerProcessingGroupService

A list of all methods in the `TradingPartnerProcessingGroupService` service. Click on the method name to view detailed information about that method.

| Methods                                                                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| :------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_trading_partner_processing_group](#create_trading_partner_processing_group)         | Send an HTTP POST request where `accountId` is the ID of the authenticating account for the request. If you omit the folderName field, you must include the folderId field — and vice versa.                                                                                                                                                                                                                                                                                     |
| [get_trading_partner_processing_group](#get_trading_partner_processing_group)               | The ordinary GET operation returns a single Trading Partner Processing Group object based on the supplied ID. The bulk GET operation returns multiple Trading Partner Processing Group objects based on the supplied IDs, to a maximum of 100. A GET operation specifying the ID of a deleted processing group component retrieves the component. In the component, the deleted field’s value is true.                                                                           |
| [update_trading_partner_processing_group](#update_trading_partner_processing_group)         | An UPDATE operation specifying the ID of a deleted processing group component restores the component to a non-deleted state, assuming the request is otherwise valid. It also overwrites the entire processing group component.                                                                                                                                                                                                                                                  |
| [delete_trading_partner_processing_group](#delete_trading_partner_processing_group)         | A DELETE operation specifying the ID of a deleted processing group component returns a false response. If you deleted the component successfully, the response is "true".                                                                                                                                                                                                                                                                                                        |
| [bulk_trading_partner_processing_group](#bulk_trading_partner_processing_group)             | To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).                                                                                                                                                                                                                                                                                                                                                                           |
| [query_trading_partner_processing_group](#query_trading_partner_processing_group)           | The QUERY operation returns all of the authenticating account’s processing group components. The operation does not return full component representations; it returns, for each result, the component’s name, ID, and folder ID. For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging). |
| [query_more_trading_partner_processing_group](#query_more_trading_partner_processing_group) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                                                                                                                                                                                                                                   |

## create_trading_partner_processing_group

Send an HTTP POST request where `accountId` is the ID of the authenticating account for the request. If you omit the folderName field, you must include the folderId field — and vice versa.

- HTTP Method: `POST`
- Endpoint: `/TradingPartnerProcessingGroup`

**Parameters**

| Name         | Type                                                                        | Required | Description       |
| :----------- | :-------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [TradingPartnerProcessingGroup](../models/TradingPartnerProcessingGroup.md) | ❌       | The request body. |

**Return Type**

`TradingPartnerProcessingGroup`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import TradingPartnerProcessingGroup

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = TradingPartnerProcessingGroup(
    default_routing={
        "process_id": "processId"
    },
    document_routing={
        "standard_route": [
            {
                "document_type_route": [
                    {
                        "partner_route": [
                            {
                                "process_id": "processId",
                                "trading_partner_id": "tradingPartnerId"
                            }
                        ],
                        "document_type": "documentType",
                        "process_id": "processId"
                    }
                ],
                "process_id": "processId",
                "standard": "x12"
            }
        ],
        "process_id": "processId"
    },
    partner_routing={
        "partner_route": [
            {
                "standard_route": [
                    {
                        "document_type_route": [
                            {
                                "document_type": "documentType",
                                "process_id": "processId"
                            }
                        ],
                        "process_id": "processId",
                        "standard": "x12"
                    }
                ],
                "process_id": "processId",
                "trading_partner_id": "tradingPartnerId"
            }
        ],
        "process_id": "processId"
    },
    trading_partners={
        "trading_partner": [
            {
                "id_": "id"
            }
        ]
    },
    component_id="3456789a-bcde-f012-34-56789abcdef012",
    component_name="East Coast partners",
    deleted=True,
    description="description",
    folder_id="11669",
    folder_name="Home:TPs:PGs:Domestic"
)

result = sdk.trading_partner_processing_group.create_trading_partner_processing_group(request_body=request_body)

print(result)
```

## get_trading_partner_processing_group

The ordinary GET operation returns a single Trading Partner Processing Group object based on the supplied ID. The bulk GET operation returns multiple Trading Partner Processing Group objects based on the supplied IDs, to a maximum of 100. A GET operation specifying the ID of a deleted processing group component retrieves the component. In the component, the deleted field’s value is true.

- HTTP Method: `GET`
- Endpoint: `/TradingPartnerProcessingGroup/{id}`

**Parameters**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| id\_ | str  | ✅       |             |

**Return Type**

`TradingPartnerProcessingGroup`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.trading_partner_processing_group.get_trading_partner_processing_group(id_="id")

print(result)
```

## update_trading_partner_processing_group

An UPDATE operation specifying the ID of a deleted processing group component restores the component to a non-deleted state, assuming the request is otherwise valid. It also overwrites the entire processing group component.

- HTTP Method: `POST`
- Endpoint: `/TradingPartnerProcessingGroup/{id}`

**Parameters**

| Name         | Type                                                                        | Required | Description       |
| :----------- | :-------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [TradingPartnerProcessingGroup](../models/TradingPartnerProcessingGroup.md) | ❌       | The request body. |
| id\_         | str                                                                         | ✅       |                   |

**Return Type**

`TradingPartnerProcessingGroup`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import TradingPartnerProcessingGroup

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = TradingPartnerProcessingGroup(
    default_routing={
        "process_id": "processId"
    },
    document_routing={
        "standard_route": [
            {
                "document_type_route": [
                    {
                        "partner_route": [
                            {
                                "process_id": "processId",
                                "trading_partner_id": "tradingPartnerId"
                            }
                        ],
                        "document_type": "documentType",
                        "process_id": "processId"
                    }
                ],
                "process_id": "processId",
                "standard": "x12"
            }
        ],
        "process_id": "processId"
    },
    partner_routing={
        "partner_route": [
            {
                "standard_route": [
                    {
                        "document_type_route": [
                            {
                                "document_type": "documentType",
                                "process_id": "processId"
                            }
                        ],
                        "process_id": "processId",
                        "standard": "x12"
                    }
                ],
                "process_id": "processId",
                "trading_partner_id": "tradingPartnerId"
            }
        ],
        "process_id": "processId"
    },
    trading_partners={
        "trading_partner": [
            {
                "id_": "id"
            }
        ]
    },
    component_id="3456789a-bcde-f012-34-56789abcdef012",
    component_name="East Coast partners",
    deleted=True,
    description="description",
    folder_id="11669",
    folder_name="Home:TPs:PGs:Domestic"
)

result = sdk.trading_partner_processing_group.update_trading_partner_processing_group(
    request_body=request_body,
    id_="id"
)

print(result)
```

## delete_trading_partner_processing_group

A DELETE operation specifying the ID of a deleted processing group component returns a false response. If you deleted the component successfully, the response is "true".

- HTTP Method: `DELETE`
- Endpoint: `/TradingPartnerProcessingGroup/{id}`

**Parameters**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| id\_ | str  | ✅       |             |

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.trading_partner_processing_group.delete_trading_partner_processing_group(id_="id")

print(result)
```

## bulk_trading_partner_processing_group

To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

- HTTP Method: `POST`
- Endpoint: `/TradingPartnerProcessingGroup/bulk`

**Parameters**

| Name         | Type                                                                                              | Required | Description       |
| :----------- | :------------------------------------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [TradingPartnerProcessingGroupBulkRequest](../models/TradingPartnerProcessingGroupBulkRequest.md) | ❌       | The request body. |

**Return Type**

`TradingPartnerProcessingGroupBulkResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import TradingPartnerProcessingGroupBulkRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = TradingPartnerProcessingGroupBulkRequest(
    request=[
        {
            "id_": "56789abc-def0-1234-5678-9abcdef01234"
        }
    ],
    type_="GET"
)

result = sdk.trading_partner_processing_group.bulk_trading_partner_processing_group(request_body=request_body)

print(result)
```

## query_trading_partner_processing_group

The QUERY operation returns all of the authenticating account’s processing group components. The operation does not return full component representations; it returns, for each result, the component’s name, ID, and folder ID. For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/TradingPartnerProcessingGroup/query`

**Parameters**

| Name         | Type                                                                                              | Required | Description       |
| :----------- | :------------------------------------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [TradingPartnerProcessingGroupQueryConfig](../models/TradingPartnerProcessingGroupQueryConfig.md) | ❌       | The request body. |

**Return Type**

`TradingPartnerProcessingGroupQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import TradingPartnerProcessingGroupQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = TradingPartnerProcessingGroupQueryConfig(
    query_filter={
        "expression": {
            "argument": [
                "argument"
            ],
            "operator": "EQUALS",
            "property": "property"
        }
    }
)

result = sdk.trading_partner_processing_group.query_trading_partner_processing_group(request_body=request_body)

print(result)
```

## query_more_trading_partner_processing_group

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/TradingPartnerProcessingGroup/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`TradingPartnerProcessingGroupQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "in sed a"

result = sdk.trading_partner_processing_group.query_more_trading_partner_processing_group(request_body=request_body)

print(result)
```

