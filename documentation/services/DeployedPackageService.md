# DeployedPackageService

A list of all methods in the `DeployedPackageService` service. Click on the method name to view detailed information about that method.

| Methods                                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| :---------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_deployed_package](#create_deployed_package)         | You can use the CREATE operation in two ways: - With `environmentId` and `packageId`, CREATE deploys the specified packaged component to the identified environment. - With `environmentId` and `componentId`, CREATE packages with the specified component and deploys the package to the specified environment. \>**Note:** By default, deployment of listener processes are in a running state. To deploy a packaged listener process in a paused state, include the `listenerStatus` field with a value of `PAUSED`. |
| [get_deployed_package](#get_deployed_package)               | Returns a single Deployed Package object based on the deployment ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [delete_deployed_package](#delete_deployed_package)         | Removes the packaged component from the environment each with a specific IDs.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [bulk_deployed_package](#bulk_deployed_package)             | To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [query_deployed_package](#query_deployed_package)           | For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                                                                                                                          |
| [query_more_deployed_package](#query_more_deployed_package) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                                                                                                                                                                                                                                                                           |

## create_deployed_package

You can use the CREATE operation in two ways: - With `environmentId` and `packageId`, CREATE deploys the specified packaged component to the identified environment. - With `environmentId` and `componentId`, CREATE packages with the specified component and deploys the package to the specified environment. \>**Note:** By default, deployment of listener processes are in a running state. To deploy a packaged listener process in a paused state, include the `listenerStatus` field with a value of `PAUSED`.

- HTTP Method: `POST`
- Endpoint: `/DeployedPackage`

**Parameters**

| Name         | Type                                            | Required | Description       |
| :----------- | :---------------------------------------------- | :------- | :---------------- |
| request_body | [DeployedPackage](../models/DeployedPackage.md) | ❌       | The request body. |

**Return Type**

`DeployedPackage`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import DeployedPackage

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = DeployedPackage(
    active=True,
    branch_name="branchName",
    component_id="componentId",
    component_type="componentType",
    component_version=1,
    deployed_by="deployedBy",
    deployed_date="deployedDate",
    deployment_id="deploymentId",
    environment_id="environmentId",
    listener_status="RUNNING",
    message="message",
    notes="notes",
    package_id="packageId",
    package_version="packageVersion",
    version=5
)

result = sdk.deployed_package.create_deployed_package(request_body=request_body)

print(result)
```

## get_deployed_package

Returns a single Deployed Package object based on the deployment ID.

- HTTP Method: `GET`
- Endpoint: `/DeployedPackage/{id}`

**Parameters**

| Name | Type | Required | Description                                               |
| :--- | :--- | :------- | :-------------------------------------------------------- |
| id\_ | str  | ✅       | The Deployed Package object you are attempting to DELETE. |

**Return Type**

`DeployedPackage`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.deployed_package.get_deployed_package(id_="id")

print(result)
```

## delete_deployed_package

Removes the packaged component from the environment each with a specific IDs.

- HTTP Method: `DELETE`
- Endpoint: `/DeployedPackage/{id}`

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

result = sdk.deployed_package.delete_deployed_package(id_="id")

print(result)
```

## bulk_deployed_package

To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

- HTTP Method: `POST`
- Endpoint: `/DeployedPackage/bulk`

**Parameters**

| Name         | Type                                                                  | Required | Description       |
| :----------- | :-------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [DeployedPackageBulkRequest](../models/DeployedPackageBulkRequest.md) | ❌       | The request body. |

**Return Type**

`DeployedPackageBulkResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import DeployedPackageBulkRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = DeployedPackageBulkRequest(
    request=[
        {
            "id_": "56789abc-def0-1234-5678-9abcdef01234"
        }
    ],
    type_="GET"
)

result = sdk.deployed_package.bulk_deployed_package(request_body=request_body)

print(result)
```

## query_deployed_package

For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/DeployedPackage/query`

**Parameters**

| Name         | Type                                                                  | Required | Description       |
| :----------- | :-------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [DeployedPackageQueryConfig](../models/DeployedPackageQueryConfig.md) | ❌       | The request body. |

**Return Type**

`DeployedPackageQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import DeployedPackageQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = DeployedPackageQueryConfig(
    query_filter={
        "expression": {
            "argument": [
                "argument"
            ],
            "operator": "EQUALS",
            "property": "uid"
        }
    }
)

result = sdk.deployed_package.query_deployed_package(request_body=request_body)

print(result)
```

## query_more_deployed_package

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/DeployedPackage/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`DeployedPackageQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "venia"

result = sdk.deployed_package.query_more_deployed_package(request_body=request_body)

print(result)
```

