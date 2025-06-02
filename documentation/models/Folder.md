# Folder

**Properties**

| Name            | Type           | Required | Description                                                                                                                                  |
| :-------------- | :------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------- |
| permitted_roles | PermittedRoles | ❌       | Optional. The defined role assigned to the available folder object.                                                                          |
| deleted         | bool           | ❌       | Read only. Indicates if the component is deleted. A true value indicates a deleted status, whereas a false value indicates an active status. |
| full_path       | str            | ❌       | Read only. The full path of the folder location in which the component most currently resides within the Component Explorer hierarchy.       |
| id\_            | str            | ❌       | Required. Read only. The -generated, unique identifier of the folder.                                                                        |
| name            | str            | ❌       | Required. The user-defined name given to the folder.                                                                                         |
| parent_id       | str            | ❌       | Required. The -generated, unique identifier of the parent folder.                                                                            |
| parent_name     | str            | ❌       |                                                                                                                                              |

