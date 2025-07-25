# GetAssignableRolesService

A list of all methods in the `GetAssignableRolesService` service. Click on the method name to view detailed information about that method.

| Methods                                               | Description                                                                                                     |
| :---------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------- |
| [get_get_assignable_roles](#get_get_assignable_roles) | You can use the Get Assignable Roles operation to retrieve a list of roles that are assignable under a account. |

## get_get_assignable_roles

You can use the Get Assignable Roles operation to retrieve a list of roles that are assignable under a account.

- HTTP Method: `GET`
- Endpoint: `/GetAssignableRoles`

**Return Type**

`Roles`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.get_assignable_roles.get_get_assignable_roles()

print(result)
```

