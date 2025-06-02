# JavaUpgradeService

A list of all methods in the `JavaUpgradeService` service. Click on the method name to view detailed information about that method.

| Methods                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| :------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_java_upgrade](#create_java_upgrade) | Download and run the Java upgrader script for a specified Runtime, Runtime cluster, Runtime cloud, Authentication Broker, or API Gateway. Upgrades your selected container to Boomis latest supported version of Java. - After providing the endpoint and a request body that includes the containerID, the CREATE operation immediately upgrades the given container to Boomi's latest supported version of Java. After performing a CREATE operation, you can determine a successful upgrade when the **Update to use Java 11.\<minor_version\>** link no longer appears on the following pages: - For Runtimes, Runtime clusters, and Runtime clouds — the **Runtime Information** panel (**Manage** \> **Runtime Management** of the user interface). - For Brokers (applicable for versions newer than 1.8.0_281-b09)— the **Broker Information** panel (**Configure Server** \> **Authentication** of the user interface). - For API Gateways — the **Gateway Information** panel (**Configure Server** \> **Gateways** of the user interface). - You must have the **Runtime Management** privilege to perform the CREATE operation. If you have the **Runtime Management Read Access** privilege, you cannot use this operation to upgrade your container. - The container must be online to use the Upgrade Java operation. - The container must be eligible for upgrade. \>**Important:** Only the node that runs upgrades (typically the head node) restarts automatically to run the updated Java version. Therefore, you must restart all other cluster nodes to install the upgrade. |

## create_java_upgrade

Download and run the Java upgrader script for a specified Runtime, Runtime cluster, Runtime cloud, Authentication Broker, or API Gateway. Upgrades your selected container to Boomis latest supported version of Java. - After providing the endpoint and a request body that includes the containerID, the CREATE operation immediately upgrades the given container to Boomi's latest supported version of Java. After performing a CREATE operation, you can determine a successful upgrade when the **Update to use Java 11.\<minor_version\>** link no longer appears on the following pages: - For Runtimes, Runtime clusters, and Runtime clouds — the **Runtime Information** panel (**Manage** \> **Runtime Management** of the user interface). - For Brokers (applicable for versions newer than 1.8.0_281-b09)— the **Broker Information** panel (**Configure Server** \> **Authentication** of the user interface). - For API Gateways — the **Gateway Information** panel (**Configure Server** \> **Gateways** of the user interface). - You must have the **Runtime Management** privilege to perform the CREATE operation. If you have the **Runtime Management Read Access** privilege, you cannot use this operation to upgrade your container. - The container must be online to use the Upgrade Java operation. - The container must be eligible for upgrade. \>**Important:** Only the node that runs upgrades (typically the head node) restarts automatically to run the updated Java version. Therefore, you must restart all other cluster nodes to install the upgrade.

- HTTP Method: `POST`
- Endpoint: `/JavaUpgrade`

**Parameters**

| Name         | Type                                    | Required | Description       |
| :----------- | :-------------------------------------- | :------- | :---------------- |
| request_body | [JavaUpgrade](../models/JavaUpgrade.md) | ❌       | The request body. |

**Return Type**

`JavaUpgrade`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import JavaUpgrade

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = JavaUpgrade(
    java_upgrade_options={
        "cacerts_path": "cacertsPath",
        "external_jdk_path": "externalJDKPath",
        "migrate_certificate": False,
        "pref_jre_location": "prefJreLocation"
    },
    atom_id="22f78648-7455-496f-aab7-ca91e31f91fa"
)

result = sdk.java_upgrade.create_java_upgrade(request_body=request_body)

print(result)
```

