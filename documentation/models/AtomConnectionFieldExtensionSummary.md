# AtomConnectionFieldExtensionSummary

**Properties**

| Name               | Type         | Required | Description                                                                                                                                                                                                    |
| :----------------- | :----------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| field              | FieldSummary | ✅       |                                                                                                                                                                                                                |
| atom_id            | str          | ❌       | The ID of the Runtime.                                                                                                                                                                                         |
| connection_id      | str          | ❌       | The ID of the connection.                                                                                                                                                                                      |
| extension_group_id | str          | ❌       | If the process is in a multi-install integration pack, this is the ID of the multi-install integration pack, which is the same as the ID of the process.                                                       |
| id\_               | str          | ❌       | The ID of the object. This is a conceptual ID synthesized from the IDs of the\<br /\> - process\<br /\>- connection\<br /\> - multi-install integration pack \(extensionGroupId\), if applicable\<br /\>- Atom |
| process_id         | str          | ❌       | The ID of the process.                                                                                                                                                                                         |

