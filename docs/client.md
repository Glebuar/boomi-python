# Client Configuration

This guide covers the configuration options available for the Boomi client.

## Basic Configuration

The `Boomi` client can be configured with various options during initialization:

```python
from boomi import Boomi

client = Boomi(
    account_id="your-account-id",
    user="your-username",
    secret="your-secret",
    retries=3,  # Optional
    timeout=30  # Optional
)
```

## Configuration Options

### Required Parameters

- `account_id` (str): Your Boomi account ID
- `user` (str): Your Boomi username
- `secret` (str): Your Boomi secret

### Optional Parameters

- `retries` (int): Maximum number of retry attempts for failed requests. Defaults to 3
- `timeout` (int): Request timeout in seconds. Defaults to 30

## Environment Variables

The client can be configured using environment variables:

```bash
export BOOMI_ACCOUNT="your-account-id"
export BOOMI_USER="your-username"
export BOOMI_SECRET="your-secret"
```

Then initialize using:

```python
client = Boomi.from_env()  

## Available Resources

The client provides access to the following resources:

- `components`: Manage Boomi components (create, get, update, delete)
- `folders`: Manage folders (create, get, delete)
- `packages`: Create component packages
- `deployments`: Deploy packages to environments
- `atoms`: List Boomi atoms
- `environments`: List environments
- `runs`: Manage process runs and logs
- `schedules`: Manage process schedules
- `extensions`: Manage environment extensions
- `runtime`: Manage runtime releases
- `execute`: Execute and cancel processes

## Best Practices

1. **Security**
   - Never hardcode credentials in your code
   - Use environment variables or secure credential storage
   - Rotate secrets regularly

2. **Performance**
   - Reuse the client instance when possible
   - Set appropriate timeout values
   - Configure retry settings based on your needs

3. **Error Handling**
   - Always implement proper error handling
   - Use the built-in exception classes:
     - `AuthenticationError`: Invalid or expired credentials
     - `RateLimitError`: Too many requests (HTTP 429)
     - `ApiError`: Other API errors (HTTP >= 400)
   - Log errors appropriately

## Next Steps

- Review the [Resources](resources.md) documentation for available API endpoints
- Check out the [Examples](examples.md) for implementation patterns
- See [Error Handling](errors.md) for detailed error management 