# AtomPurgeService

A list of all methods in the `AtomPurgeService` service. Click on the method name to view detailed information about that method.

| Methods                                 | Description                                                                                                                                                                                                        |
| :-------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [update_atom_purge](#update_atom_purge) | You can use the Purge Runtime cloud attachment operation to programmatically start the purge process for test and browse components, logs, processed documents, and temporary data for a Runtime Cloud attachment. |

## update_atom_purge

You can use the Purge Runtime cloud attachment operation to programmatically start the purge process for test and browse components, logs, processed documents, and temporary data for a Runtime Cloud attachment.

- HTTP Method: `POST`
- Endpoint: `/AtomPurge/{id}`

**Parameters**

| Name         | Type                                | Required | Description                                                                                                                                                                                                                             |
| :----------- | :---------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [AtomPurge](../models/AtomPurge.md) | ❌       | The request body.                                                                                                                                                                                                                       |
| id\_         | str                                 | ✅       | The unique ID assigned by the system to the Runtime cloud attachment. The Runtime ID is found in the user interface by navigating to **Manage \> Runtime Management** and viewing the Runtime Information panel for a selected Runtime. |

**Return Type**

`AtomPurge`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import AtomPurge

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = AtomPurge(
    atom_id="3456789a-bcde-f012-3456-789abcdef012"
)

result = sdk.atom_purge.update_atom_purge(
    request_body=request_body,
    id_="id"
)

print(result)
```

