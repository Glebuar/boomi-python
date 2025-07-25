# AtomSecurityPoliciesService

A list of all methods in the `AtomSecurityPoliciesService` service. Click on the method name to view detailed information about that method.

| Methods                                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| :------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [update_atom_security_policies](#update_atom_security_policies)           | Updates the security policy for the specified Runtime cloud or Runtime cluster. You can add, update, or delete permissions by using the UPDATE operation. You can add custom Java runtime permissions you specify in an UPDATE operation to the appropriate High-security policy file. In addition, all High-security policy files contain custom permissions that you specify in the \<common\> section. As confirmation of the changes made, the UPDATE operation returns a copy of the request.                                                 |
| [async_get_atom_security_policies](#async_get_atom_security_policies)     | The initial GET operation returns a security policy token for the specified Runtime cloud or Runtime cluster. Subsequent GET operations return status code 202 (while the request is in progress) or the custom contents of a security policy based on the token that was returned. The GET operation returns only custom runtime permissions that you added to the security policy, not the entire policy file. If you did not update the security policy for a given Runtime cloud or Runtime cluster, the response to a GET operation is empty. |
| [async_token_atom_security_policies](#async_token_atom_security_policies) | Using the token from the initial GET response, send an HTTP GET where accountId is the account with which you are authenticating. Custom Java runtime permissions listed in the `\<common\>` section apply to all High security policy files (procrunner-HIGH.policy, procbrowser-HIGH.policy, and procworker-HIGH.policy). Custom permissions listed in a specific section, such as `\<runner\>`, apply only to the associated security policy file.                                                                                              |

## update_atom_security_policies

Updates the security policy for the specified Runtime cloud or Runtime cluster. You can add, update, or delete permissions by using the UPDATE operation. You can add custom Java runtime permissions you specify in an UPDATE operation to the appropriate High-security policy file. In addition, all High-security policy files contain custom permissions that you specify in the \<common\> section. As confirmation of the changes made, the UPDATE operation returns a copy of the request.

- HTTP Method: `POST`
- Endpoint: `/AtomSecurityPolicies/{id}`

**Parameters**

| Name         | Type                                                      | Required | Description                                                                                                                                                           |
| :----------- | :-------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [AtomSecurityPolicies](../models/AtomSecurityPolicies.md) | ❌       | The request body.                                                                                                                                                     |
| id\_         | str                                                       | ✅       | The runtime (container) id for the applicable runtime (accepts only Runtime cloud cluster and regular Runtime cluster types, no basic runtimes or cloud attachments). |

**Return Type**

`AtomSecurityPolicies`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import AtomSecurityPolicies

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = AtomSecurityPolicies(
    atom_id="4ce4a1c2-5bd9-4bd9-9201-46198e2d88db",
    browser={
        "policies": [
            {
                "arguments": [
                    {
                        "value": "value"
                    }
                ],
                "privilege_type": "privilegeType"
            }
        ]
    },
    common={
        "policies": [
            {
                "arguments": [
                    {
                        "value": "value"
                    }
                ],
                "privilege_type": "privilegeType"
            }
        ]
    },
    runner={
        "policies": [
            {
                "arguments": [
                    {
                        "value": "value"
                    }
                ],
                "privilege_type": "privilegeType"
            }
        ]
    },
    worker={
        "policies": [
            {
                "arguments": [
                    {
                        "value": "value"
                    }
                ],
                "privilege_type": "privilegeType"
            }
        ]
    }
)

result = sdk.atom_security_policies.update_atom_security_policies(
    request_body=request_body,
    id_="id"
)

print(result)
```

## async_get_atom_security_policies

The initial GET operation returns a security policy token for the specified Runtime cloud or Runtime cluster. Subsequent GET operations return status code 202 (while the request is in progress) or the custom contents of a security policy based on the token that was returned. The GET operation returns only custom runtime permissions that you added to the security policy, not the entire policy file. If you did not update the security policy for a given Runtime cloud or Runtime cluster, the response to a GET operation is empty.

- HTTP Method: `GET`
- Endpoint: `/async/AtomSecurityPolicies/{id}`

**Parameters**

| Name | Type | Required | Description                                                                                                                                                           |
| :--- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id\_ | str  | ✅       | The runtime (container) id for the applicable runtime (accepts only Runtime cloud cluster and regular runtime cluster types, no basic runtimes or cloud attachments). |

**Return Type**

`AsyncOperationTokenResult`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.atom_security_policies.async_get_atom_security_policies(id_="id")

print(result)
```

## async_token_atom_security_policies

Using the token from the initial GET response, send an HTTP GET where accountId is the account with which you are authenticating. Custom Java runtime permissions listed in the `\<common\>` section apply to all High security policy files (procrunner-HIGH.policy, procbrowser-HIGH.policy, and procworker-HIGH.policy). Custom permissions listed in a specific section, such as `\<runner\>`, apply only to the associated security policy file.

- HTTP Method: `GET`
- Endpoint: `/async/AtomSecurityPolicies/response/{token}`

**Parameters**

| Name  | Type | Required | Description                                                 |
| :---- | :--- | :------- | :---------------------------------------------------------- |
| token | str  | ✅       | Takes in the token from a previous call to return a result. |

**Return Type**

`AtomSecurityPoliciesAsyncResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.atom_security_policies.async_token_atom_security_policies(token="token")

print(result)
```

