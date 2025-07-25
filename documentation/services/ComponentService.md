# ComponentService

A list of all methods in the `ComponentService` service. Click on the method name to view detailed information about that method.

| Methods                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| :------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_component](#create_component) | - Cannot create components for types not eligible for your account. For example, if your account does not have the B2B/EDI feature, you will not be able to create Trading Partner components. - Request will not be processed in case if the payload has invalid attributes and tags under the \<object\> section. - Include the `branchId` in the request body to specify a branch on which you want to create the component. - \>**Note:** To create or update a component, you must supply a valid component XML format for the given type. The component XML can be rather complex with many optional fields and nested configuration. For this reason we strongly recommend approaching it by first creating the desired component structure/skeleton as you would normally in the Build page UI, then exporting the XML using the Component object GET. This will provide an accurate example or template of the XML you will need to create. You can replace values or continue that pattern as you need for your use case. |
| [get_component](#get_component)       | - When using the GET operation by componentId, it returns the latest component if you do not provide the version. - When you provide the version in the format of `\<componentId\>` ~ `\<version\>`, it returns the specific version of the component. - The GET operation only accepts mediaType `application/xml` for the API response. - The limit is 5 requests for the BULK GET operation. All other API objects have a limit of 100 BULK GET requests. - If you want information for a component on a specific branch, include the branchId in the GET request: `https://api.boomi.com/api/rest/v1/{accountId}/Component/{componentId}~{branchId}`                                                                                                                                                                                                                                                                                                                                                                            |
| [update_component](#update_component) | - Full updates only. No partial updates. If part of the object’s configuration is omitted, the component will be updated without that configuration. - The only exception is for encrypted fields such as passwords. Omitting an encrypted field from the update request will NOT impact the saved value. - Requests without material changes to configuration will be rejected to prevent unnecessary revisions. - Request will not be processed in case if the payload has invalid attributes and tags under the `\<object\>` section. - For the saved process property components, modifications to the data type are not permitted. - Include the `branchId` in the request body to specify the branch on which you want to update the component. - \>**Note:** To create or update a component, you must supply a valid component XML format for the given type.                                                                                                                                                               |
| [bulk_component](#bulk_component)     | The limit for the BULK GET operation is 5 requests. All other API objects have a limit of 100 BULK GET requests. To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

## create_component

- Cannot create components for types not eligible for your account. For example, if your account does not have the B2B/EDI feature, you will not be able to create Trading Partner components. - Request will not be processed in case if the payload has invalid attributes and tags under the \<object\> section. - Include the `branchId` in the request body to specify a branch on which you want to create the component. - \>**Note:** To create or update a component, you must supply a valid component XML format for the given type. The component XML can be rather complex with many optional fields and nested configuration. For this reason we strongly recommend approaching it by first creating the desired component structure/skeleton as you would normally in the Build page UI, then exporting the XML using the Component object GET. This will provide an accurate example or template of the XML you will need to create. You can replace values or continue that pattern as you need for your use case.

- HTTP Method: `POST`
- Endpoint: `/Component`

**Parameters**

| Name         | Type                    | Required | Description       |
| :----------- | :---------------------- | :------- | :---------------- |
| request_body | [str](../models/str.md) | ❌       | The request body. |

**Return Type**

`Component`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import Component

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

with open("file.ext", "r") as f:
    request_body = f.read()

result = sdk.component.create_component(request_body=request_body)

print(result)
```

## get_component

- When using the GET operation by componentId, it returns the latest component if you do not provide the version. - When you provide the version in the format of `\<componentId\>` ~ `\<version\>`, it returns the specific version of the component. - The GET operation only accepts mediaType `application/xml` for the API response. - The limit is 5 requests for the BULK GET operation. All other API objects have a limit of 100 BULK GET requests. - If you want information for a component on a specific branch, include the branchId in the GET request: `https://api.boomi.com/api/rest/v1/{accountId}/Component/{componentId}~{branchId}`

- HTTP Method: `GET`
- Endpoint: `/Component/{componentId}`

**Parameters**

| Name         | Type | Required | Description                                                                                                                                                                                                                                |
| :----------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| component_id | str  | ✅       | The ID of the component. The component ID is available on the Revision History dialog, which you can access from the Build page in the service. This must be omitted for the CREATE operation but it is required for the UPDATE operation. |

**Return Type**

`Component`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.component.get_component(component_id="componentId")

print(result)
```

## update_component

- Full updates only. No partial updates. If part of the object’s configuration is omitted, the component will be updated without that configuration. - The only exception is for encrypted fields such as passwords. Omitting an encrypted field from the update request will NOT impact the saved value. - Requests without material changes to configuration will be rejected to prevent unnecessary revisions. - Request will not be processed in case if the payload has invalid attributes and tags under the `\<object\>` section. - For the saved process property components, modifications to the data type are not permitted. - Include the `branchId` in the request body to specify the branch on which you want to update the component. - \>**Note:** To create or update a component, you must supply a valid component XML format for the given type.

- HTTP Method: `POST`
- Endpoint: `/Component/{componentId}`

**Parameters**

| Name         | Type                    | Required | Description                                                                                                                                                                                                                                |
| :----------- | :---------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [str](../models/str.md) | ❌       | The request body.                                                                                                                                                                                                                          |
| component_id | str                     | ✅       | The ID of the component. The component ID is available on the Revision History dialog, which you can access from the Build page in the service. This must be omitted for the CREATE operation but it is required for the UPDATE operation. |

**Return Type**

`Component`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import Component

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

with open("file.ext", "r") as f:
    request_body = f.read()

result = sdk.component.update_component(
    request_body=request_body,
    component_id="componentId"
)

print(result)
```

## bulk_component

The limit for the BULK GET operation is 5 requests. All other API objects have a limit of 100 BULK GET requests. To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

- HTTP Method: `POST`
- Endpoint: `/Component/bulk`

**Parameters**

| Name         | Type                                                      | Required | Description       |
| :----------- | :-------------------------------------------------------- | :------- | :---------------- |
| request_body | [ComponentBulkRequest](../models/ComponentBulkRequest.md) | ❌       | The request body. |

**Return Type**

`str`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import ComponentBulkRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = ComponentBulkRequest(
    request=[
        {
            "id_": "56789abc-def0-1234-5678-9abcdef01234"
        }
    ],
    type_="GET"
)

result = sdk.component.bulk_component(request_body=request_body)

with open("output-file.ext", "w") as f:
    f.write(result)
```

