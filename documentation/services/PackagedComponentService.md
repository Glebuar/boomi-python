# PackagedComponentService

A list of all methods in the `PackagedComponentService` service. Click on the method name to view detailed information about that method.

| Methods                                                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| :-------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_packaged_component](#create_packaged_component)         | - You can use the CREATE operation to perform two different actions. For example, you can create a new packaged component from a specific component ID, or you can restore a deleted packaged component. Both actions use the same object endpoint. However, the information required in the request body differs. - **To create a new packaged component**, you must include a component ID in the request body. You create a packaged component for the specified componentId. Optionally, you can specify a packageVersion value and notes about the package version. \>**Note:** You cannot add package versions and notes after creating the packaged component. However, if not specified, automatically assigns a numerical version number to your new packaged component. - **To restore or recover a deleted packaged component**, you must specify the packageId, componentId, and packageVersion. You can query the Packaged Component object for a list of deleted packaged components. - Specify a `branchName` to create a packaged component on a particular branch. If `branchName` is not provided, the default working branch is used. |
| [get_packaged_component](#get_packaged_component)               | Retrieves the packaged component with the specified ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [delete_packaged_component](#delete_packaged_component)         | - The DELETE operation deletes a specific packaged component version. The id that you provide in the endpoint represents a Packaged Component ID. You can retrieve the Packaged Component ID (packageId) using the GET and QUERY operations, or by viewing the **Packaged Component History** dialog for a specific version in the Integration user interface. \>**Note:** You can restore deleted packaged components using the CREATE operation. See the section **Using the CREATE operation** for more details. - You cannot delete a packaged component if it is already in use. If currently deployed, a packaged component is considered in use if it is used in the **Process Library** or as part of an integration pack.                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [bulk_packaged_component](#bulk_packaged_component)             | To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [query_packaged_component](#query_packaged_component)           | For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [query_more_packaged_component](#query_more_packaged_component) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

## create_packaged_component

- You can use the CREATE operation to perform two different actions. For example, you can create a new packaged component from a specific component ID, or you can restore a deleted packaged component. Both actions use the same object endpoint. However, the information required in the request body differs. - **To create a new packaged component**, you must include a component ID in the request body. You create a packaged component for the specified componentId. Optionally, you can specify a packageVersion value and notes about the package version. \>**Note:** You cannot add package versions and notes after creating the packaged component. However, if not specified, automatically assigns a numerical version number to your new packaged component. - **To restore or recover a deleted packaged component**, you must specify the packageId, componentId, and packageVersion. You can query the Packaged Component object for a list of deleted packaged components. - Specify a `branchName` to create a packaged component on a particular branch. If `branchName` is not provided, the default working branch is used.

- HTTP Method: `POST`
- Endpoint: `/PackagedComponent`

**Parameters**

| Name         | Type                                                | Required | Description       |
| :----------- | :-------------------------------------------------- | :------- | :---------------- |
| request_body | [PackagedComponent](../models/PackagedComponent.md) | ❌       | The request body. |

**Return Type**

`PackagedComponent`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import PackagedComponent

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = PackagedComponent(
    branch_name="branchName",
    component_id="66d665d1-3ec7-479c-9e24-8df3fa728cf8",
    component_type="process",
    component_version="2.0",
    created_by="userboomi.com",
    created_date="2017-03-16T13:34:01Z",
    deleted="false",
    fully_publicly_consumable=False,
    notes="Created for component publication with GUID f7f6ddb6-9437-4a90-9655-f01970068ca8 and version 2.",
    package_id="e8dbc278-e970-49e5-84bd-af39d7d38140",
    package_version="2.0",
    shareable="true"
)

result = sdk.packaged_component.create_packaged_component(request_body=request_body)

print(result)
```

## get_packaged_component

Retrieves the packaged component with the specified ID.

- HTTP Method: `GET`
- Endpoint: `/PackagedComponent/{id}`

**Parameters**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| id\_ | str  | ✅       |             |

**Return Type**

`PackagedComponent`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.packaged_component.get_packaged_component(id_="id")

print(result)
```

## delete_packaged_component

- The DELETE operation deletes a specific packaged component version. The id that you provide in the endpoint represents a Packaged Component ID. You can retrieve the Packaged Component ID (packageId) using the GET and QUERY operations, or by viewing the **Packaged Component History** dialog for a specific version in the Integration user interface. \>**Note:** You can restore deleted packaged components using the CREATE operation. See the section **Using the CREATE operation** for more details. - You cannot delete a packaged component if it is already in use. If currently deployed, a packaged component is considered in use if it is used in the **Process Library** or as part of an integration pack.

- HTTP Method: `DELETE`
- Endpoint: `/PackagedComponent/{id}`

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

result = sdk.packaged_component.delete_packaged_component(id_="id")

print(result)
```

## bulk_packaged_component

To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

- HTTP Method: `POST`
- Endpoint: `/PackagedComponent/bulk`

**Parameters**

| Name         | Type                                                                      | Required | Description       |
| :----------- | :------------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [PackagedComponentBulkRequest](../models/PackagedComponentBulkRequest.md) | ❌       | The request body. |

**Return Type**

`PackagedComponentBulkResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import PackagedComponentBulkRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = PackagedComponentBulkRequest(
    request=[
        {
            "id_": "56789abc-def0-1234-5678-9abcdef01234"
        }
    ],
    type_="GET"
)

result = sdk.packaged_component.bulk_packaged_component(request_body=request_body)

print(result)
```

## query_packaged_component

For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/PackagedComponent/query`

**Parameters**

| Name         | Type                                                                      | Required | Description       |
| :----------- | :------------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [PackagedComponentQueryConfig](../models/PackagedComponentQueryConfig.md) | ❌       | The request body. |

**Return Type**

`PackagedComponentQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import PackagedComponentQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = PackagedComponentQueryConfig(
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

result = sdk.packaged_component.query_packaged_component(request_body=request_body)

print(result)
```

## query_more_packaged_component

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/PackagedComponent/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`PackagedComponentQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "nulla"

result = sdk.packaged_component.query_more_packaged_component(request_body=request_body)

print(result)
```

