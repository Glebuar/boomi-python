# ListenerStatusAsyncResponse

**Properties**

| Name                 | Type                 | Required | Description                                                                                                                                                                                           |
| :------------------- | :------------------- | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| response_status_code | ResponseStatusCode   | ✅       | The status code returned from a request, as follows: - 202 — Initialized the Listener status request and is in progress (QUERY response). - 200 — Listener status request is complete (GET response). |
| number_of_results    | int                  | ❌       |                                                                                                                                                                                                       |
| result               | List[ListenerStatus] | ❌       |                                                                                                                                                                                                       |

# ResponseStatusCode

The status code returned from a request, as follows: - 202 — Initialized the Listener status request and is in progress (QUERY response). - 200 — Listener status request is complete (GET response).

**Properties**

| Name  | Type | Required | Description |
| :---- | :--- | :------- | :---------- |
| \_200 | int  | ✅       | 200         |
| \_202 | int  | ✅       | 202         |

