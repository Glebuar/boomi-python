# AtomCountersService

A list of all methods in the `AtomCountersService` service. Click on the method name to view detailed information about that method.

| Methods                                       | Description                                                                                                                                                                                                                                                                               |
| :-------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [update_atom_counters](#update_atom_counters) | The UPDATE operation updates Runtime Counter values for a specific Runtime. Using the UPDATE operation overrides all settings set on the current counter. However, calling the UPDATE operation does not delete any existing counters that are not included in the `AtomCounters` object. |

## update_atom_counters

The UPDATE operation updates Runtime Counter values for a specific Runtime. Using the UPDATE operation overrides all settings set on the current counter. However, calling the UPDATE operation does not delete any existing counters that are not included in the `AtomCounters` object.

- HTTP Method: `POST`
- Endpoint: `/AtomCounters/{id}`

**Parameters**

| Name         | Type                                      | Required | Description                                        |
| :----------- | :---------------------------------------- | :------- | :------------------------------------------------- |
| request_body | [AtomCounters](../models/AtomCounters.md) | ❌       | The request body.                                  |
| id\_         | str                                       | ✅       | A unique ID assigned by the system to the Runtime. |

**Return Type**

`AtomCounters`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import AtomCounters

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = AtomCounters(
    atom_id="atomId",
    counter=[
        {
            "name": "name",
            "value": 6
        }
    ]
)

result = sdk.atom_counters.update_atom_counters(
    request_body=request_body,
    id_="id"
)

print(result)
```

