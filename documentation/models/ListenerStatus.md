# ListenerStatus

**Properties**

| Name           | Type | Required | Description                                                                                                                                           |
| :------------- | :--- | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------- |
| listener_id    | str  | ✅       | The Component ID for the listener process.                                                                                                            |
| status         | str  | ✅       | The status of the listener as `listening`, `paused`, or `errored`.                                                                                    |
| connector_type | str  | ❌       | The internal and unique identifier for connector type, which resembles the connector type names presented on the **Build** tab of the user interface. |

