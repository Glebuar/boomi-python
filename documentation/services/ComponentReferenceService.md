# ComponentReferenceService

A list of all methods in the `ComponentReferenceService` service. Click on the method name to view detailed information about that method.

| Methods                                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| :---------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [get_component_reference](#get_component_reference)               | Retrieves the component reference for a component ID. Send an HTTP GET to `https://api.boomi.com/api/rest/v1/{accountId}/ComponentReference/{componentId}` where `{accountId}` is the ID of the authenticating account for the request and `{componentId}` is the ID of the secondary component whose references you are attempting to GET. If you want to specify a branch, send an HTTP GET to `https://api.boomi.com/api/rest/v1/{accountId}/ComponentReference/{componentId}~{branchId}` where `{accountId}` is the ID of the authenticating account for the request and `{componentId}` is the ID of the secondary component whose references you are attempting to GET, and `{branchId}` is the branch on which you want to GET component references.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [bulk_component_reference](#bulk_component_reference)             | To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [query_component_reference](#query_component_reference)           | For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging). - You can use the QUERY operation to return the latest version(s) of a primary component(s) that references a given secondary component ID, or all the secondary components that the given primary component ID references. \>**Note:** When querying either primary or secondary component references, the API object returns the immediate reference (one level). It does not recursively trace through nested references like the **Show Where Used** feature does in the user interface. For example, take a process that references a Map component where it references two Profile components. If you query by `parentComponentId=\<process\>`, the API returns a result for the Map component but not the profiles. To get the profiles, you need to perform a second call to query references for the Map component. - You can filter the query operation in one of two ways: - To find all the secondary components referenced by a given primary component, you must provide both the parentComponentId and the parentVersion values. You can optionally use the type filter in your query. - To find all the primary components that reference a given secondary component, you must provide the componentId value. You can optionally include the type filter in your query. - To see more information about a component ID returned in the response, like the component's type or name, you can query that same ID using the [Component Metadata object](/api/platformapi#tag/ComponentMetadata). #### Understanding references to deleted components Filtering or querying by `componentId` only returns the component's current version. If you delete the current component revision, it does not return results. When filtering by `parentComponentId` or `parentVersion`, it saves references to other components for a given version of the primary component. If you delete the given primary component version, it does not return results. Note that it is possible to return a reference to a deleted secondary component if you do not remove the reference in the user interface (appears in red). |
| [query_more_component_reference](#query_more_component_reference) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

## get_component_reference

Retrieves the component reference for a component ID. Send an HTTP GET to `https://api.boomi.com/api/rest/v1/{accountId}/ComponentReference/{componentId}` where `{accountId}` is the ID of the authenticating account for the request and `{componentId}` is the ID of the secondary component whose references you are attempting to GET. If you want to specify a branch, send an HTTP GET to `https://api.boomi.com/api/rest/v1/{accountId}/ComponentReference/{componentId}~{branchId}` where `{accountId}` is the ID of the authenticating account for the request and `{componentId}` is the ID of the secondary component whose references you are attempting to GET, and `{branchId}` is the branch on which you want to GET component references.

- HTTP Method: `GET`
- Endpoint: `/ComponentReference/{componentId}`

**Parameters**

| Name         | Type | Required | Description                                                                                                                                                       |
| :----------- | :--- | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| component_id | str  | ✅       | The ID of the secondary component. The component ID is available in the **Revision History** dialog, which you can access from the **Build** page in the service. |

**Return Type**

`ComponentReference`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.component_reference.get_component_reference(component_id="componentId")

print(result)
```

## bulk_component_reference

To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

- HTTP Method: `POST`
- Endpoint: `/ComponentReference/bulk`

**Parameters**

| Name         | Type                                                                        | Required | Description       |
| :----------- | :-------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [ComponentReferenceBulkRequest](../models/ComponentReferenceBulkRequest.md) | ❌       | The request body. |

**Return Type**

`ComponentReferenceBulkResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import ComponentReferenceBulkRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = ComponentReferenceBulkRequest(
    request=[
        {
            "id_": "56789abc-def0-1234-5678-9abcdef01234"
        }
    ],
    type_="GET"
)

result = sdk.component_reference.bulk_component_reference(request_body=request_body)

print(result)
```

## query_component_reference

For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging). - You can use the QUERY operation to return the latest version(s) of a primary component(s) that references a given secondary component ID, or all the secondary components that the given primary component ID references. \>**Note:** When querying either primary or secondary component references, the API object returns the immediate reference (one level). It does not recursively trace through nested references like the **Show Where Used** feature does in the user interface. For example, take a process that references a Map component where it references two Profile components. If you query by `parentComponentId=\<process\>`, the API returns a result for the Map component but not the profiles. To get the profiles, you need to perform a second call to query references for the Map component. - You can filter the query operation in one of two ways: - To find all the secondary components referenced by a given primary component, you must provide both the parentComponentId and the parentVersion values. You can optionally use the type filter in your query. - To find all the primary components that reference a given secondary component, you must provide the componentId value. You can optionally include the type filter in your query. - To see more information about a component ID returned in the response, like the component's type or name, you can query that same ID using the [Component Metadata object](/api/platformapi#tag/ComponentMetadata). #### Understanding references to deleted components Filtering or querying by `componentId` only returns the component's current version. If you delete the current component revision, it does not return results. When filtering by `parentComponentId` or `parentVersion`, it saves references to other components for a given version of the primary component. If you delete the given primary component version, it does not return results. Note that it is possible to return a reference to a deleted secondary component if you do not remove the reference in the user interface (appears in red).

- HTTP Method: `POST`
- Endpoint: `/ComponentReference/query`

**Parameters**

| Name         | Type                                                                        | Required | Description       |
| :----------- | :-------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [ComponentReferenceQueryConfig](../models/ComponentReferenceQueryConfig.md) | ❌       | The request body. |

**Return Type**

`ComponentReferenceQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import ComponentReferenceQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = ComponentReferenceQueryConfig(
    query_filter={
        "expression": {
            "argument": [
                "argument"
            ],
            "operator": "EQUALS",
            "property": "parentComponentId"
        }
    }
)

result = sdk.component_reference.query_component_reference(request_body=request_body)

print(result)
```

## query_more_component_reference

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/ComponentReference/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`ComponentReferenceQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "ullamco "

result = sdk.component_reference.query_more_component_reference(request_body=request_body)

print(result)
```

