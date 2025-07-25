# ComponentDiffResponseCreate

**Properties**

| Name                    | Type                  | Required | Description |
| :---------------------- | :-------------------- | :------- | :---------- |
| component_diff_response | ComponentDiffResponse | ❌       |             |

# ComponentDiffResponse

**Properties**

| Name         | Type        | Required | Description                                           |
| :----------- | :---------- | :------- | :---------------------------------------------------- |
| message      | str         | ❌       | Message providing details about the diffed components |
| generic_diff | GenericDiff | ❌       |                                                       |

# GenericDiff

**Properties**

| Name         | Type         | Required | Description |
| :----------- | :----------- | :------- | :---------- |
| addition     | Addition     | ❌       |             |
| modification | Modification | ❌       |             |

# Addition

**Properties**

| Name   | Type           | Required | Description               |
| :----- | :------------- | :------- | :------------------------ |
| total  | int            | ❌       | Total number of additions |
| change | AdditionChange | ❌       |                           |

# AdditionChange

**Properties**

| Name                  | Type              | Required | Description                          |
| :-------------------- | :---------------- | :------- | :----------------------------------- |
| type\_                | str               | ❌       | Type of change (e.g., element)       |
| changed_particle_name | str               | ❌       | Name of the particle that changed    |
| element_key           | ChangeElementKey1 | ❌       |                                      |
| new_value             | str               | ❌       | New value of the element in the diff |

# ChangeElementKey_1

**Properties**

| Name         | Type    | Required | Description         |
| :----------- | :------ | :------- | :------------------ |
| element_name | str     | ❌       | Name of the element |
| key_part     | KeyPart | ❌       |                     |

# KeyPart

**Properties**

| Name      | Type | Required | Description     |
| :-------- | :--- | :------- | :-------------- |
| attribute | str  | ❌       | Attribute name  |
| value     | str  | ❌       | Attribute value |

# Modification

**Properties**

| Name   | Type               | Required | Description                   |
| :----- | :----------------- | :------- | :---------------------------- |
| total  | int                | ❌       | Total number of modifications |
| change | ModificationChange | ❌       |                               |

# ModificationChange

**Properties**

| Name                  | Type              | Required | Description                            |
| :-------------------- | :---------------- | :------- | :------------------------------------- |
| type\_                | str               | ❌       | Type of modification (e.g., attribute) |
| changed_particle_name | str               | ❌       | Name of the particle that was modified |
| element_key           | ChangeElementKey2 | ❌       |                                        |
| new_value             | str               | ❌       | New value of the attribute             |
| old_value             | str               | ❌       | Old value of the attribute             |

# ChangeElementKey_2

**Properties**

| Name         | Type | Required | Description         |
| :----------- | :--- | :------- | :------------------ |
| element_name | str  | ❌       | Name of the element |

