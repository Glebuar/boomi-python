# ConnectionLicensingReportService

A list of all methods in the `ConnectionLicensingReportService` service. Click on the method name to view detailed information about that method.

| Methods                                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| :------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_connection_licensing_report](#create_connection_licensing_report) | Returns the Connection Licensing URL in the response to view or download the deployed connection details. To download connection licensing data for a given connector class: a. Send a POST and request body to `https://api.boomi.com/api/rest/v1/\<accountId\>/ConnectionLicensingReport` where accountId is the ID of the authenticating account for the request. Populate the request body with or without the available filters for the report that you want to download. b. Next, send a GET request using the URL returned in the POST response. The GET does not require a request body, and returns the deployed connection details. \>**Note:** Do not pass any filters in the CREATE payload. This will not help get the Test & Production connections deployed details for all the connector classes. To get the Test and Production deployed connection details you have to pass ONLY the structure in the CREATE request, without any filters. - To apply multiple filters, add the Operator to the payload. Refer to the provided code samples for guidance. - The argument values for the _property_ filters in the CREATE payload should be: - componentId - Must be a valid componentId value. If an invalid value is passed, the report or the GET response will be blank or will have zero records. - environmentId - Must be valid environmentId value. If an invalid value is passed, the report or the GET response will be blank or will have zero records. - containerId - Must be a valid atomId or moleculeId. If an invalid value is passed, the report or the GET response will be blank or will have zero records. - connectorClass - Must be valid connectorClass. Values must be either Standard, Small Business, Trading Partner, or Enterprise. |

## create_connection_licensing_report

Returns the Connection Licensing URL in the response to view or download the deployed connection details. To download connection licensing data for a given connector class: a. Send a POST and request body to `https://api.boomi.com/api/rest/v1/\<accountId\>/ConnectionLicensingReport` where accountId is the ID of the authenticating account for the request. Populate the request body with or without the available filters for the report that you want to download. b. Next, send a GET request using the URL returned in the POST response. The GET does not require a request body, and returns the deployed connection details. \>**Note:** Do not pass any filters in the CREATE payload. This will not help get the Test & Production connections deployed details for all the connector classes. To get the Test and Production deployed connection details you have to pass ONLY the structure in the CREATE request, without any filters. - To apply multiple filters, add the Operator to the payload. Refer to the provided code samples for guidance. - The argument values for the _property_ filters in the CREATE payload should be: - componentId - Must be a valid componentId value. If an invalid value is passed, the report or the GET response will be blank or will have zero records. - environmentId - Must be valid environmentId value. If an invalid value is passed, the report or the GET response will be blank or will have zero records. - containerId - Must be a valid atomId or moleculeId. If an invalid value is passed, the report or the GET response will be blank or will have zero records. - connectorClass - Must be valid connectorClass. Values must be either Standard, Small Business, Trading Partner, or Enterprise.

- HTTP Method: `POST`
- Endpoint: `/ConnectionLicensingReport`

**Parameters**

| Name         | Type                                                                | Required | Description       |
| :----------- | :------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [ConnectionLicensingReport](../models/ConnectionLicensingReport.md) | ❌       | The request body. |

**Return Type**

`ConnectionLicensingDownload`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import ConnectionLicensingReport

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = ConnectionLicensingReport(
    query_filter={
        "expression": {}
    }
)

result = sdk.connection_licensing_report.create_connection_licensing_report(request_body=request_body)

print(result)
```

