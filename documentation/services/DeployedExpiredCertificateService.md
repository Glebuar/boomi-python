# DeployedExpiredCertificateService

A list of all methods in the `DeployedExpiredCertificateService` service. Click on the method name to view detailed information about that method.

| Methods                                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| :---------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [query_deployed_expired_certificate](#query_deployed_expired_certificate)           | If a QUERY omits an explicit timespan filter — that is, the query does not use `expirationBoundary` in an expression — it applies a default timespan filter using the value of 30 and the LESS_THAN operator. This filter specifies expired certificates and certificates expiring within 30 days. For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging). |
| [query_more_deployed_expired_certificate](#query_more_deployed_expired_certificate) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

## query_deployed_expired_certificate

If a QUERY omits an explicit timespan filter — that is, the query does not use `expirationBoundary` in an expression — it applies a default timespan filter using the value of 30 and the LESS_THAN operator. This filter specifies expired certificates and certificates expiring within 30 days. For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/DeployedExpiredCertificate/query`

**Parameters**

| Name         | Type                                                                                        | Required | Description       |
| :----------- | :------------------------------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [DeployedExpiredCertificateQueryConfig](../models/DeployedExpiredCertificateQueryConfig.md) | ❌       | The request body. |

**Return Type**

`DeployedExpiredCertificateQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import DeployedExpiredCertificateQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = DeployedExpiredCertificateQueryConfig(
    query_filter={
        "expression": {
            "argument": [
                "argument"
            ],
            "operator": "LESS_THAN_OR_EQUAL",
            "property": "containerId"
        }
    }
)

result = sdk.deployed_expired_certificate.query_deployed_expired_certificate(request_body=request_body)

print(result)
```

## query_more_deployed_expired_certificate

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/DeployedExpiredCertificate/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`DeployedExpiredCertificateQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "id ipsum nisi s"

result = sdk.deployed_expired_certificate.query_more_deployed_expired_certificate(request_body=request_body)

print(result)
```

