# MapExtensionsFunctionSteps

Defines the individual function steps and the order in which they need to occur within the greater user-defined function. The following attributes are used: 1.`position` - represents the step's number order in the greater function. 2.`cacheType` - indicates the caching behavior of the individual function step. The allowed `cacheType` values are:1.`None` \(default, if omitted in the request\)— It does not use Map function caching. 2. `ByDocument` — Caches the map function’s input and output values for each processed document. 3. `ByMap` — Caches the map function’s input and output values for each processed map. - `id` - represents the function step's ID in the format of "FUNCEXT--xxxxxxxxxx". 4. `type` - represents the type of function \(for example, "MathCeil" or "CustomScripting"\).\<br /\> Within the `Steps` element, you also need to define the following `input` and `output` variables for each function step:\<br /\>1. `default` - Optional. Specifies the input value that the function uses if not provided by the user.\<br /\>2. `name` - the user-defined name of the associated input or output. \>**Note:** The user interface automatically uses the used function type as the step name, but you can use this API object to change function step names. 3. `key` - the number ID assigned to a function step. This key is used to map function steps together in the `Mappings` attribute.

**Properties**

| Name | Type                            | Required | Description |
| :--- | :------------------------------ | :------- | :---------- |
| step | List[MapExtensionsFunctionStep] | ❌       |             |

