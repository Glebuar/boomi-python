# PublisherPackagedComponent

**Properties**

| Name            | Type | Required | Description                                                                                                     |
| :-------------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------- |
| component_id    | str  | ❌       | ID of the primary component in the packaged component.                                                          |
| component_name  | str  | ❌       | Name of the primary component in the packaged component.                                                        |
| component_type  | str  | ❌       | Component type of the primary component in the packaged component.                                              |
| current_version | str  | ❌       | Packaged component version of the component that is currently released in this integration pack.                |
| deleted         | bool | ❌       | If true, the packaged component will be removed from the integration pack in the next release.                  |
| latest_version  | str  | ❌       | Latest packaged component version of the component that is available to be added to this integration pack.      |
| pending_version | str  | ❌       | Packaged component version of the component that will be included in the next release of this integration pack. |

