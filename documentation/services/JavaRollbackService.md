# JavaRollbackService

A list of all methods in the `JavaRollbackService` service. Click on the method name to view detailed information about that method.

| Methods                                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| :---------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [execute_java_rollback](#execute_java_rollback) | Returns a Runtime, Runtime cluster, Runtime cloud, Authentication Broker, or Gateway to use the previous version of Java with an EXECUTE operation. - After performing the EXECUTE operation, you can determine the success of returning to an earlier version when the **Update to use \<new Java version\>.\<minor_version\>** link displays on the following pages, indicating that a more recent version is available for upgrade: - For Runtimes, Runtime clusters, and Runtime clouds — the **Runtime Information** panel (**Manage** \> **Runtime Management** of the user interface). - For Brokers — the **Broker Information** panel (**Configure Server** \> **Authentication** of the user interface). - For API Gateways — the **Gateway Information** panel (**Configure Server** \> **Gateways** of the user interface). To verify a successful rollback on a Runtime using the user interface, you can also navigate to **Runtime Management** \> **Startup Properties** and reference the Java version number listed in the **Java Home** field. - The container must be online to use the Rollback Java operation. \>**Important:** Only the node that runs upgrades (typically the head node) restarts automatically to run the updated Java version for Runtimes, Runtime clusters, and Runtime clouds. You must restart all other cluster nodes to successfully return to a previous version of Java. \> To successfully return to a previous version of Java for API Management Gateways and Authentication Brokers, you must restart all Gateways and Brokers. |

## execute_java_rollback

Returns a Runtime, Runtime cluster, Runtime cloud, Authentication Broker, or Gateway to use the previous version of Java with an EXECUTE operation. - After performing the EXECUTE operation, you can determine the success of returning to an earlier version when the **Update to use \<new Java version\>.\<minor_version\>** link displays on the following pages, indicating that a more recent version is available for upgrade: - For Runtimes, Runtime clusters, and Runtime clouds — the **Runtime Information** panel (**Manage** \> **Runtime Management** of the user interface). - For Brokers — the **Broker Information** panel (**Configure Server** \> **Authentication** of the user interface). - For API Gateways — the **Gateway Information** panel (**Configure Server** \> **Gateways** of the user interface). To verify a successful rollback on a Runtime using the user interface, you can also navigate to **Runtime Management** \> **Startup Properties** and reference the Java version number listed in the **Java Home** field. - The container must be online to use the Rollback Java operation. \>**Important:** Only the node that runs upgrades (typically the head node) restarts automatically to run the updated Java version for Runtimes, Runtime clusters, and Runtime clouds. You must restart all other cluster nodes to successfully return to a previous version of Java. \> To successfully return to a previous version of Java for API Management Gateways and Authentication Brokers, you must restart all Gateways and Brokers.

- HTTP Method: `POST`
- Endpoint: `/JavaRollback/execute/{id}`

**Parameters**

| Name         | Type                                      | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| :----------- | :---------------------------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [JavaRollback](../models/JavaRollback.md) | ❌       | The request body.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| id\_         | str                                       | ✅       | The unique ID assigned by the system to the container. 1. Use the Runtime ID for Runtimes, Runtime clusters, and Runtime clouds found in the user interface by navigating to **Manage** \> **Runtime Management** and viewing the Runtime Information panel for a selected container. 2. Use the Gateway ID found in the user interface by navigating to **Configure Server** \> **Gateways** \> `\<gatewayName\>` \> Gateway Information panel. 3. Use the Broker ID found in the user interface by navigating to **Configure Server** \> **Authentication** \> `\<brokerName\>` \> Broker Information panel. |

**Return Type**

`JavaRollback`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import JavaRollback

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = JavaRollback(
    atom_id="3456789a-bcde-f012-3456-789abcdef012"
)

result = sdk.java_rollback.execute_java_rollback(
    request_body=request_body,
    id_="id"
)

print(result)
```

