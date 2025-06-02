# ChangeListenerStatusRequest

**Properties**

| Name         | Type   | Required | Description                                                                                                                                                                                                                                 |
| :----------- | :----- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| action       | Action | ❌       | The action to be performed.                                                                                                                                                                                                                 |
| container_id | str    | ❌       | The ID of the Runtime, Runtime cluster, or Runtime cloud to which you deploy the listener or listeners.                                                                                                                                     |
| listener_id  | str    | ❌       | The ID of a single listener process whose status you want to change. To change the status of all listeners, omit this parameter. \>**Note:** You can obtain the ID for a listener process by using a QUERY operation on the Process object. |

# Action

The action to be performed.

**Properties**

| Name       | Type | Required | Description   |
| :--------- | :--- | :------- | :------------ |
| RESTART    | str  | ✅       | "restart"     |
| RESTARTALL | str  | ✅       | "restart_all" |
| PAUSE      | str  | ✅       | "pause"       |
| PAUSEALL   | str  | ✅       | "pause_all"   |
| RESUME     | str  | ✅       | "resume"      |
| RESUMEALL  | str  | ✅       | "resume_all"  |

