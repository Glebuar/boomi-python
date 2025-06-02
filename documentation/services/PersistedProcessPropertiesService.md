# PersistedProcessPropertiesService

A list of all methods in the `PersistedProcessPropertiesService` service. Click on the method name to view detailed information about that method.

| Methods                                                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| :-------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [update_persisted_process_properties](#update_persisted_process_properties) | The UPDATE operation updates Persisted Process Property values for the specified Runtime. Using the UPDATE operation overrides all current property settings. Therefore, strongly recommends that you include a complete list of all Persisted Process properties you want to keep or update. If you do not list a current persisted process property in the Persisted Process properties object, the UPDATE operation deletes those properties. \>**Note:** You can update the Persisted Process properties if you have either the Runtime Management privilege or the Runtime Management Read Access, along with the Persisted Process Property Read and Write Access privilege. |

## update_persisted_process_properties

The UPDATE operation updates Persisted Process Property values for the specified Runtime. Using the UPDATE operation overrides all current property settings. Therefore, strongly recommends that you include a complete list of all Persisted Process properties you want to keep or update. If you do not list a current persisted process property in the Persisted Process properties object, the UPDATE operation deletes those properties. \>**Note:** You can update the Persisted Process properties if you have either the Runtime Management privilege or the Runtime Management Read Access, along with the Persisted Process Property Read and Write Access privilege.

- HTTP Method: `POST`
- Endpoint: `/PersistedProcessProperties/{id}`

**Parameters**

| Name         | Type                                                                  | Required | Description                                        |
| :----------- | :-------------------------------------------------------------------- | :------- | :------------------------------------------------- |
| request_body | [PersistedProcessProperties](../models/PersistedProcessProperties.md) | ❌       | The request body.                                  |
| id\_         | str                                                                   | ✅       | A unique ID assigned by the system to the Runtime. |

**Return Type**

`PersistedProcessProperties`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import PersistedProcessProperties

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = PersistedProcessProperties(
    process=[
        {
            "process_properties": {
                "process_property": [
                    {
                        "process_property_value": [
                            {
                                "component_override": False,
                                "encrypted_value_set": False,
                                "key": "key",
                                "label": "label",
                                "use_default": True,
                                "uses_encryption": False,
                                "validate": False,
                                "value": "value"
                            }
                        ],
                        "component_id": "componentId"
                    }
                ]
            },
            "process_id": "processId"
        }
    ],
    atom_id="atomId"
)

result = sdk.persisted_process_properties.update_persisted_process_properties(
    request_body=request_body,
    id_="id"
)

print(result)
```

