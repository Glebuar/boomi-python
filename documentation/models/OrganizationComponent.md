# OrganizationComponent

**Properties**

| Name                      | Type                    | Required | Description                                                                                                                                                                                                            |
| :------------------------ | :---------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| organization_contact_info | OrganizationContactInfo | ✅       |                                                                                                                                                                                                                        |
| component_id              | str                     | ❌       | A unique ID assigned by the system to the component.                                                                                                                                                                   |
| component_name            | str                     | ❌       | A user-defined name for the component.                                                                                                                                                                                 |
| deleted                   | bool                    | ❌       | Indicates if the component is deleted. A value of `true` indicates a deleted status, whereas `false` indicates an active status.                                                                                       |
| description               | str                     | ❌       | Description of the component. \>**Note:** Although this field is in the object, operations do not support the field. For example, the system ignores the field if it is present in a QUERY, CREATE, or UPDATE request. |
| folder_id                 | int                     | ❌       | The ID of the folder in which the component currently resides.                                                                                                                                                         |
| folder_name               | str                     | ❌       | The folder location of the component within Component Explorer.                                                                                                                                                        |

