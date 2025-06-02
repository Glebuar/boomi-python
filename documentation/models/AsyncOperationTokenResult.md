# AsyncOperationTokenResult

**Properties**

| Name                 | Type       | Required | Description                                                                                                                                                                                           |
| :------------------- | :--------- | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| async_token          | AsyncToken | ✅       |                                                                                                                                                                                                       |
| response_status_code | int        | ✅       | The status code returned from a request, as follows: - 202 — Initialized the Listener status request and is in progress (QUERY response). - 200 — Listener status request is complete (GET response). |

