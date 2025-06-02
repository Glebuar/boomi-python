# ComponentMetadataService

A list of all methods in the `ComponentMetadataService` service. Click on the method name to view detailed information about that method.

| Methods                                                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| :-------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_component_metadata](#create_component_metadata)         | The ability to create a new component is not supported at this time. Although, you can create a deleted component, but you cannot create a new component. You will receive an error if you do not specify the deleted component ID in the create request.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [get_component_metadata](#get_component_metadata)               | Returns the latest component revision if you do not provide the version. Providing the version in the format of `\<componentId\>` ~ `\<version\>`, returns the specific version of the component.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [update_component_metadata](#update_component_metadata)         | Only `name` and `folderId` may be updated. They are optional and will only be modified if included in the UPDATE request. `folderId` must be a valid, non-deleted folder. If `folderId` is included in the request but with a blank value, it defaults to the root folder.                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [delete_component_metadata](#delete_component_metadata)         | Lets you delete required components. Note that deleting a component does NOT delete dependent components.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [bulk_component_metadata](#bulk_component_metadata)             | To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [query_component_metadata](#query_component_metadata)           | - By default, QUERY results include previous revisions including deleted versions. Use query filters to exclude previous and deleted versions if desired. For more examples of querying components, see Component Metadata API example requests mentioned above in the API description. - The `version` field must be accompanied by the `componentId` field. You can query all other fields. - The `copiedFromComponentId` field must accompany the `copiedFromComponentVersion` field. For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging). |
| [query_more_component_metadata](#query_more_component_metadata) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

## create_component_metadata

The ability to create a new component is not supported at this time. Although, you can create a deleted component, but you cannot create a new component. You will receive an error if you do not specify the deleted component ID in the create request.

- HTTP Method: `POST`
- Endpoint: `/ComponentMetadata`

**Parameters**

| Name         | Type                                                | Required | Description       |
| :----------- | :-------------------------------------------------- | :------- | :---------------- |
| request_body | [ComponentMetadata](../models/ComponentMetadata.md) | ❌       | The request body. |

**Return Type**

`ComponentMetadata`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import ComponentMetadata

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = ComponentMetadata(
    branch_id="branchId",
    branch_name="branchName",
    component_id="456789a-bcde-f0123-4567-89abcdef012",
    copied_from_component_id="123456a-bcde-f4567-8901-23abcdef456",
    copied_from_component_version="6",
    created_by="johndoeboomi.com",
    created_date="2019-11-05T20:13:25Z",
    current_version="false",
    deleted="true",
    folder_id="\\\"PloxRzM5OTk\\\"",
    folder_name="Boomi",
    modified_by="janedoeboomi.com",
    modified_date="2019-11-26T21:23:55Z",
    name="Component123",
    sub_type="process",
    type_="certificate",
    version="7"
)

result = sdk.component_metadata.create_component_metadata(request_body=request_body)

print(result)
```

## get_component_metadata

Returns the latest component revision if you do not provide the version. Providing the version in the format of `\<componentId\>` ~ `\<version\>`, returns the specific version of the component.

- HTTP Method: `GET`
- Endpoint: `/ComponentMetadata/{id}`

**Parameters**

| Name | Type | Required | Description                                                                                                                                                          |
| :--- | :--- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id\_ | str  | ✅       | Required. Read only. The ID of the component. The component ID is available on the Revision History dialog, which you can access from the Build page in the service. |

**Return Type**

`ComponentMetadata`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.component_metadata.get_component_metadata(id_="id")

print(result)
```

## update_component_metadata

Only `name` and `folderId` may be updated. They are optional and will only be modified if included in the UPDATE request. `folderId` must be a valid, non-deleted folder. If `folderId` is included in the request but with a blank value, it defaults to the root folder.

- HTTP Method: `POST`
- Endpoint: `/ComponentMetadata/{id}`

**Parameters**

| Name         | Type                                                | Required | Description                                                                                                                                                          |
| :----------- | :-------------------------------------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [ComponentMetadata](../models/ComponentMetadata.md) | ❌       | The request body.                                                                                                                                                    |
| id\_         | str                                                 | ✅       | Required. Read only. The ID of the component. The component ID is available on the Revision History dialog, which you can access from the Build page in the service. |

**Return Type**

`ComponentMetadata`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import ComponentMetadata

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = ComponentMetadata(
    branch_id="branchId",
    branch_name="branchName",
    component_id="456789a-bcde-f0123-4567-89abcdef012",
    copied_from_component_id="123456a-bcde-f4567-8901-23abcdef456",
    copied_from_component_version="6",
    created_by="johndoeboomi.com",
    created_date="2019-11-05T20:13:25Z",
    current_version="false",
    deleted="true",
    folder_id="\\\"PloxRzM5OTk\\\"",
    folder_name="Boomi",
    modified_by="janedoeboomi.com",
    modified_date="2019-11-26T21:23:55Z",
    name="Component123",
    sub_type="process",
    type_="certificate",
    version="7"
)

result = sdk.component_metadata.update_component_metadata(
    request_body=request_body,
    id_="id"
)

print(result)
```

## delete_component_metadata

Lets you delete required components. Note that deleting a component does NOT delete dependent components.

- HTTP Method: `DELETE`
- Endpoint: `/ComponentMetadata/{id}`

**Parameters**

| Name | Type | Required | Description                                                                                                                                                          |
| :--- | :--- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id\_ | str  | ✅       | Required. Read only. The ID of the component. The component ID is available on the Revision History dialog, which you can access from the Build page in the service. |

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.component_metadata.delete_component_metadata(id_="id")

print(result)
```

## bulk_component_metadata

To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

- HTTP Method: `POST`
- Endpoint: `/ComponentMetadata/bulk`

**Parameters**

| Name         | Type                                                                      | Required | Description       |
| :----------- | :------------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [ComponentMetadataBulkRequest](../models/ComponentMetadataBulkRequest.md) | ❌       | The request body. |

**Return Type**

`ComponentMetadataBulkResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import ComponentMetadataBulkRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = ComponentMetadataBulkRequest(
    request=[
        {
            "id_": "56789abc-def0-1234-5678-9abcdef01234"
        }
    ],
    type_="GET"
)

result = sdk.component_metadata.bulk_component_metadata(request_body=request_body)

print(result)
```

## query_component_metadata

- By default, QUERY results include previous revisions including deleted versions. Use query filters to exclude previous and deleted versions if desired. For more examples of querying components, see Component Metadata API example requests mentioned above in the API description. - The `version` field must be accompanied by the `componentId` field. You can query all other fields. - The `copiedFromComponentId` field must accompany the `copiedFromComponentVersion` field. For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/ComponentMetadata/query`

**Parameters**

| Name         | Type                                                                      | Required | Description       |
| :----------- | :------------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [ComponentMetadataQueryConfig](../models/ComponentMetadataQueryConfig.md) | ❌       | The request body. |

**Return Type**

`ComponentMetadataQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import ComponentMetadataQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = ComponentMetadataQueryConfig(
    query_filter={
        "expression": {
            "argument": [
                "argument"
            ],
            "operator": "EQUALS",
            "property": "accountId"
        }
    }
)

result = sdk.component_metadata.query_component_metadata(request_body=request_body)

print(result)
```

## query_more_component_metadata

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/ComponentMetadata/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`ComponentMetadataQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "dolore eu Ut a"

result = sdk.component_metadata.query_more_component_metadata(request_body=request_body)

print(result)
```

