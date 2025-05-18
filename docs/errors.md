# Error Handling

This guide covers how to handle errors and exceptions in the Boomi Python SDK.

## Exception Hierarchy

The SDK provides a hierarchy of exceptions for different error scenarios:

```python
from boomi.exceptions import (
    BoomiError,           # Base exception class
    AuthenticationError,  # Authentication errors
    RateLimitError,       # Rate limiting errors
    ApiError             # Any other non-retryable API error
)
```

## Common Error Scenarios

### Authentication Errors

```python
from boomi.exceptions import AuthenticationError

try:
    client = Boomi(
        account_id="invalid-id",
        user="invalid-user",
        secret="invalid-secret"
    )
    client.components.list()
except AuthenticationError as e:
    print(f"Authentication failed: {e}")
```

### API Errors

```python
from boomi.exceptions import ApiError

try:
    component = client.components.get(cid="non-existent")
except ApiError as e:
    print(f"API error occurred: {e}")
```

### Rate Limiting

The SDK automatically handles rate limits with exponential backoff. If you need custom handling:

```python
from boomi.exceptions import RateLimitError
import time

def make_request_with_retry():
    try:
        return client.components.list()
    except RateLimitError as e:
        time.sleep(2)  # SDK already handles retries, this is just an example
        return make_request_with_retry()
```

## Best Practices

1. **Always Use Try-Except**

```python
try:
    result = client.components.get(cid="123")
except BoomiError as e:
    # Handle all Boomi-related errors
    logger.error(f"Boomi error: {e}")
except Exception as e:
    # Handle unexpected errors
    logger.error(f"Unexpected error: {e}")
```

2. **Log Errors Appropriately**

```python
import logging

logger = logging.getLogger(__name__)

try:
    component = client.components.get(cid="123")
except BoomiError as e:
    logger.error(f"Error accessing component: {e}", exc_info=True)
    # Handle error appropriately
```

## Next Steps

- Review the [Client Configuration](client.md) for timeout and retry settings
- Check out the [Examples](examples.md) for error handling patterns
- See [Resources](resources.md) for API-specific error details 

