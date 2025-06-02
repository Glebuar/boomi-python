# OrganizationComponentService

A list of all methods in the `OrganizationComponentService` service. Click on the method name to view detailed information about that method.

| Methods                                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| :---------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [create_organization_component](#create_organization_component)         | The CREATE operation creates an Organization Component object with the specified component name. The request body requires the `componentName` field. If you omit the `folderName` field, it requires the `folderId` field — and vice versa. If you omit the `componentID` field, it assigns the value when you create the component. If you omit the `folderID` field, it assigns the value when you create the component.                                                                                                                                                                                         |
| [get_organization_component](#get_organization_component)               | The GET operation returns a single Organization Component object based on the supplied ID. A GET operation specifying the ID of a deleted Organization Component retrieves the component. In the component, the deleted field’s value is _true_.                                                                                                                                                                                                                                                                                                                                                                    |
| [update_organization_component](#update_organization_component)         | The UPDATE operation overwrites the Organization Component object with the specified component ID. An UPDATE operation specifying the ID of a deleted Organization component restores the component to a non-deleted state, assuming the request is otherwise valid.                                                                                                                                                                                                                                                                                                                                                |
| [delete_organization_component](#delete_organization_component)         | The DELETE operation deletes the Organization Component object with the specified component ID. A DELETE operation specifying the ID of a deleted Organization component returns a false response. If the component is deleted successfully, the response is `true`.                                                                                                                                                                                                                                                                                                                                                |
| [bulk_organization_component](#bulk_organization_component)             | The bulk GET operation returns multiple Account objects based on the supplied account IDs, to a maximum of 100. To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).                                                                                                                                                                                                                                                                                                                                                                                              |
| [query_organization_component](#query_organization_component)           | - Only the LIKE operator is allowed with a name filter. Likewise, only the EQUALS operator is permitted with a contactName, email, or phone filter. - If the QUERY request includes multiple filters, you can connect the filters with a logical AND operator — the query does not support the logical OR operator . - The QUERY results omit the folderName field. For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging). |
| [query_more_organization_component](#query_more_organization_component) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

## create_organization_component

The CREATE operation creates an Organization Component object with the specified component name. The request body requires the `componentName` field. If you omit the `folderName` field, it requires the `folderId` field — and vice versa. If you omit the `componentID` field, it assigns the value when you create the component. If you omit the `folderID` field, it assigns the value when you create the component.

- HTTP Method: `POST`
- Endpoint: `/OrganizationComponent`

**Parameters**

| Name         | Type                                                        | Required | Description       |
| :----------- | :---------------------------------------------------------- | :------- | :---------------- |
| request_body | [OrganizationComponent](../models/OrganizationComponent.md) | ❌       | The request body. |

**Return Type**

`OrganizationComponent`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import OrganizationComponent

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = OrganizationComponent(
    organization_contact_info={
        "address1": "127 Comstock Ave.",
        "address2": "address2",
        "city": "Philadelphia",
        "contact_name": "Tom Miller",
        "contact_url": "https://www.bestwholesaling.biz",
        "country": "country",
        "email": "tom@bestwholesaling.biz",
        "fax": "311 555-9753",
        "phone": "311 555-3579",
        "postalcode": "19100",
        "state": "PA"
    },
    component_id="89abcdef-0123-4567-89ab-cdef01234567",
    component_name="Best Wholesaling",
    deleted=True,
    description="Shared Organization component for Best Wholesaling",
    folder_id=11356,
    folder_name="Commercial"
)

result = sdk.organization_component.create_organization_component(request_body=request_body)

print(result)
```

## get_organization_component

The GET operation returns a single Organization Component object based on the supplied ID. A GET operation specifying the ID of a deleted Organization Component retrieves the component. In the component, the deleted field’s value is _true_.

- HTTP Method: `GET`
- Endpoint: `/OrganizationComponent/{id}`

**Parameters**

| Name | Type | Required | Description               |
| :--- | :--- | :------- | :------------------------ |
| id\_ | str  | ✅       | Organization component ID |

**Return Type**

`OrganizationComponent`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.organization_component.get_organization_component(id_="id")

print(result)
```

## update_organization_component

The UPDATE operation overwrites the Organization Component object with the specified component ID. An UPDATE operation specifying the ID of a deleted Organization component restores the component to a non-deleted state, assuming the request is otherwise valid.

- HTTP Method: `POST`
- Endpoint: `/OrganizationComponent/{id}`

**Parameters**

| Name         | Type                                                        | Required | Description               |
| :----------- | :---------------------------------------------------------- | :------- | :------------------------ |
| request_body | [OrganizationComponent](../models/OrganizationComponent.md) | ❌       | The request body.         |
| id\_         | str                                                         | ✅       | Organization component ID |

**Return Type**

`OrganizationComponent`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import OrganizationComponent

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = OrganizationComponent(
    organization_contact_info={
        "address1": "127 Comstock Ave.",
        "address2": "address2",
        "city": "Philadelphia",
        "contact_name": "Tom Miller",
        "contact_url": "https://www.bestwholesaling.biz",
        "country": "country",
        "email": "tom@bestwholesaling.biz",
        "fax": "311 555-9753",
        "phone": "311 555-3579",
        "postalcode": "19100",
        "state": "PA"
    },
    component_id="89abcdef-0123-4567-89ab-cdef01234567",
    component_name="Best Wholesaling",
    deleted=True,
    description="Shared Organization component for Best Wholesaling",
    folder_id=11356,
    folder_name="Commercial"
)

result = sdk.organization_component.update_organization_component(
    request_body=request_body,
    id_="id"
)

print(result)
```

## delete_organization_component

The DELETE operation deletes the Organization Component object with the specified component ID. A DELETE operation specifying the ID of a deleted Organization component returns a false response. If the component is deleted successfully, the response is `true`.

- HTTP Method: `DELETE`
- Endpoint: `/OrganizationComponent/{id}`

**Parameters**

| Name | Type | Required | Description                                                    |
| :--- | :--- | :------- | :------------------------------------------------------------- |
| id\_ | str  | ✅       | ID of the Organization component you are attempting to delete. |

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.organization_component.delete_organization_component(id_="id")

print(result)
```

## bulk_organization_component

The bulk GET operation returns multiple Account objects based on the supplied account IDs, to a maximum of 100. To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

- HTTP Method: `POST`
- Endpoint: `/OrganizationComponent/bulk`

**Parameters**

| Name         | Type                                                                              | Required | Description       |
| :----------- | :-------------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [OrganizationComponentBulkRequest](../models/OrganizationComponentBulkRequest.md) | ❌       | The request body. |

**Return Type**

`str`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import OrganizationComponentBulkRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = OrganizationComponentBulkRequest(
    request=[
        {
            "id_": "56789abc-def0-1234-5678-9abcdef01234"
        }
    ],
    type_="GET"
)

result = sdk.organization_component.bulk_organization_component(request_body=request_body)

with open("output-file.ext", "w") as f:
    f.write(result)
```

## query_organization_component

- Only the LIKE operator is allowed with a name filter. Likewise, only the EQUALS operator is permitted with a contactName, email, or phone filter. - If the QUERY request includes multiple filters, you can connect the filters with a logical AND operator — the query does not support the logical OR operator . - The QUERY results omit the folderName field. For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/OrganizationComponent/query`

**Parameters**

| Name         | Type                                                                              | Required | Description       |
| :----------- | :-------------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [OrganizationComponentQueryConfig](../models/OrganizationComponentQueryConfig.md) | ❌       | The request body. |

**Return Type**

`OrganizationComponentQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import OrganizationComponentQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = OrganizationComponentQueryConfig(
    query_filter={
        "expression": {
            "argument": [
                "argument"
            ],
            "operator": "EQUALS",
            "property": "name"
        }
    }
)

result = sdk.organization_component.query_organization_component(request_body=request_body)

print(result)
```

## query_more_organization_component

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/OrganizationComponent/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`OrganizationComponentQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "eu cillum e"

result = sdk.organization_component.query_more_organization_component(request_body=request_body)

print(result)
```

