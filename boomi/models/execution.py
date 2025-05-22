from typing import List, Optional, Dict
from pydantic import BaseModel, Field

class CancelExecutionRequest(BaseModel):
    """
    Model for a cancel execution request.
    Corresponds to the conceptual CancelExecution operation, though not explicitly in openapi.json schemas.
    """
    executionId: str
    notes: Optional[str] = None

class ProcessProperty(BaseModel):
    """
    A key-value pair for a process property.
    """
    Name: str
    Value: str

class ProcessProperties(BaseModel):
    """
    A collection of process properties.
    Corresponds to ProcessProperties within ExecutionRequest in openapi.json.
    """
    Property: List[ProcessProperty] = Field(alias="ProcessProperty")

class DynamicProcessProperty(BaseModel):
    """
    A key-value pair for a dynamic process property.
    Corresponds to DynamicProcessProperty within ExecutionRequest in openapi.json.
    """
    Name: str
    Value: str

class ExecutionRequestModel(BaseModel):
    """
    Model for an execution request.
    Corresponds to ExecutionRequest in openapi.json.
    """
    atomId: str
    processId: str
    ProcessProperties: Optional[ProcessProperties] = None
    dynamicProcessProperties: Optional[List[DynamicProcessProperty]] = Field(default=None, alias="DynamicProcessProperties")
    # Alias for dynamicProcessProperties based on common XML/JSON array naming in Boomi

    class Config:
        allow_population_by_field_name = True # Allows using either alias or field name

class ExecutionResponse(BaseModel):
    """
    Model for an execution response.
    Based on typical asynchronous execution responses providing an ID to track the request.
    The `openapi.json` defines `ExecutionRequest` returning `requestId` and `recordUrl`.
    """
    executionId: Optional[str] = None # This might be part of a subsequent query using requestId
    requestId: Optional[str] = None
    recordUrl: Optional[str] = None # As seen in the ExecutionRequest response example
    message: Optional[str] = None # General message field for responses

    # If the actual execution result is needed, a more complex model based on ExecutionRecord would be used.
    # For now, this covers the immediate response from an execution submission.

# Example from openapi.json for ExecuteProcess operation (which is similar to ExecutionRequest)
# The response for ExecuteProcess is not explicitly detailed but typically returns a way to track it.
# The ExecutionRequest object's response example shows:
# {
#   "@type" : "ExecutionRequest",
#   "processId" : "789abcde-f012-3456-789a-bcdef0123456",
#   "atomId" : "3456789a-bcde-f0123-4567-89abcdef012",
#   "requestId" : "executionrecord-110b23f4-567a-8d90-1234-56789e0b123d",
#   "recordUrl" : "http://localhost:8081/api/rest/v1/account1234/ExecutionRecord/async/executionrecord-110b23f4-567a-8d90-1234-56789e0b123d"
# }
# So, ExecutionResponse should reflect this.
# The `executionId` for the actual process run is often part of the ExecutionRecord, not the immediate submission response.
# Let's adjust ExecutionResponse to better match the ExecutionRequest's POST response.

class ExecutionSubmissionResponse(BaseModel):
    """
    Response from submitting an execution request.
    Corresponds to the immediate response from POST /ExecutionRequest in openapi.json
    """
    requestId: str
    recordUrl: str # URL to query the ExecutionRecord
    # Other fields like processId, atomId from the request are also echoed back but not essential for the response model itself.
    # Adding message for any informational text from the API.
    message: Optional[str] = None


# ExecutionRecord itself is a very complex object, if we need to model that, it would be separate.
# For now, the task asks for ExecutionResponse, which I interpret as the response to an execution *request*.
# The openapi.json snippet for POST /ExecutionRequest shows a response containing requestId and recordUrl.
# Let's keep ExecutionResponse simple as initially requested, but acknowledge the richer ExecutionSubmissionResponse.
# For the purpose of this task, ExecutionResponse will be a simplified version.

class SimplifiedExecutionResponse(BaseModel):
    """
    Simplified model for an execution response, focusing on IDs.
    """
    executionId: Optional[str] = None # This might be the ID of the actual execution if returned directly
    requestId: Optional[str] = None # ID to track an asynchronous execution request

    class Config:
        allow_population_by_field_name = True
        
# Re-evaluating the ExecutionResponse based on the task:
# "ExecutionResponse":
#   "executionId: str"
#   "requestId: Optional[str] = None (and any other relevant fields from the OpenAPI ExecutionResponse schema)."
# The openapi.json does not have a direct "ExecutionResponse" schema.
# The closest is the response from POST /ExecutionRequest which is:
# {
#   "@type" : "ExecutionRequest",
#   ... (echoes of request params)
#   "requestId" : "executionrecord-110b23f4-567a-8d90-1234-56789e0b123d",
#   "recordUrl" : "http://localhost:8081/api/rest/v1/account1234/ExecutionRecord/async/executionrecord-110b23f4-567a-8d90-1234-56789e0b123d"
# }
# This response does NOT contain `executionId` directly. `executionId` is part of the `ExecutionRecord` which is fetched using the `requestId`.
# For the purpose of this task, I will create `ExecutionResponse` as specified, assuming `executionId` might be populated from a subsequent call
# or a different context not immediately clear from the provided openapi.json snippet for ExecutionRequest's response.

class ExecutionResponse(BaseModel): # Final decision based on task spec
    """
    Model for an execution response.
    Fields are based on the subtask description.
    `executionId` would typically be retrieved by a subsequent query using `requestId`.
    """
    executionId: str # As per task, though typically not in immediate submission response
    requestId: Optional[str] = None
    recordUrl: Optional[str] = None # Adding this as it's a relevant field from similar responses
    message: Optional[str] = None # General message

    class Config:
        allow_population_by_field_name = True

# Ensuring DynamicProcessProperties is correctly aliased if needed for ExecutionRequestModel
# The openapi.json example for ExecutionRequest shows:
# "DynamicProcessProperties": { "DynamicProcessProperty": [ { "name": "property1", "value": "value1" } ] }
# This implies that dynamicProcessProperties in the Pydantic model should indeed be a list of DynamicProcessProperty objects
# and the field itself in the JSON payload is "DynamicProcessProperties".
# The `Field(alias="DynamicProcessProperties")` in `ExecutionRequestModel` handles this.
# Similarly for `ProcessProperties`.
# The openapi.json example for ExecutionRequest shows:
# "ProcessProperties": { "ProcessProperty": [ { "componentId": "456789a-bcde-f0123-4567-89abcdef012", "ProcessPropertyValue": [ ... ] } ] }
# My `ProcessProperties` model has `Property: List[ProcessProperty] = Field(alias="ProcessProperty")`.
# This seems to align with the structure where `ProcessProperties` is an object containing a list named `ProcessProperty`.
# Let's verify the `ProcessProperty` in openapi.json for `ExecutionRequest`.
# The example for `ExecutionRequest` in `openapi.json` shows:
# "ProcessProperties": {
#   "ProcessProperty": [
#     {
#       "componentId": "456789a-bcde-f0123-4567-89abcdef012",  <-- This is not Name/Value
#       "ProcessPropertyValue": [ { "key": "key1", "value": "value1" } ]
#     }
#   ]
# }
# This structure for ProcessProperty is different from the simple Name/Value I initially assumed.
# It seems `ProcessProperty` itself is more complex, containing `componentId` and a list of `ProcessPropertyValue`.

# Correcting ProcessProperty and ProcessProperties based on openapi.json example for ExecutionRequest:

class ProcessPropertyValue(BaseModel):
    """
    A key-value pair for a specific property within a ProcessProperty component.
    """
    key: str
    value: str
    # encrypted: Optional[bool] = None # Depending on if this detail is needed/available

class ProcessProperty(BaseModel): # This is actually a "ProcessPropertyComponent"
    """
    Represents a Process Property Component to be overridden in an execution request.
    Corresponds to an item in the ProcessProperty list within ExecutionRequest in openapi.json.
    """
    componentId: str
    ProcessPropertyValue: List[ProcessPropertyValue] # List of actual key-value property overrides

class ProcessProperties(BaseModel):
    """
    A collection of Process Property Components to be overridden.
    Corresponds to ProcessProperties within ExecutionRequest in openapi.json.
    """
    ProcessProperty: List[ProcessProperty] # This list holds ProcessPropertyComponent-like objects

# Re-defining DynamicProcessProperty based on its structure in openapi.json for ExecutionRequest:
# "DynamicProcessProperties": {
#   "DynamicProcessProperty": [ { "name": "property1", "value": "value1" } ]
# }
# This means DynamicProcessProperty is a simple Name/Value, and it's nested under a list called "DynamicProcessProperty"
# which itself is under "DynamicProcessProperties".

class DynamicProcessProperty(BaseModel): # This is correct as Name/Value
    """
    A key-value pair for a dynamic process property.
    """
    Name: str # Matches the 'name' in the example
    Value: str # Matches the 'value' in the example

class DynamicProcessProperties(BaseModel):
    """
    Container for a list of DynamicProcessProperty objects.
    """
    DynamicProcessProperty: List[DynamicProcessProperty]


class ExecutionRequestModel(BaseModel):
    """
    Model for an execution request.
    Corresponds to ExecutionRequest in openapi.json.
    """
    atomId: str
    processId: str
    ProcessProperties: Optional[ProcessProperties] = None # This model structure is now corrected
    # The field in JSON is "DynamicProcessProperties", which contains a list also named "DynamicProcessProperty"
    # So, the type should be a model that has a "DynamicProcessProperty" list attribute.
    DynamicProcessProperties: Optional[DynamicProcessProperties] = None # Corrected

    class Config:
        allow_population_by_field_name = True
        
# Final check on ExecutionResponse:
# The task is specific: `executionId: str`, `requestId: Optional[str] = None`.
# The POST /ExecutionRequest in openapi.json returns `requestId` and `recordUrl`. It does *not* return `executionId`.
# `executionId` is part of the `ExecutionRecord` schema, which is what you'd query later using the `requestId`.
# I will stick to the task's explicit definition for `ExecutionResponse`, but note this discrepancy.

class ExecutionResponse(BaseModel):
    """
    Model for an execution response.
    Fields are based on the subtask description.
    `executionId` would typically be retrieved by a subsequent query using `requestId`.
    """
    executionId: str # As per task spec
    requestId: Optional[str] = None
    # Adding other relevant fields based on typical async submission responses or potential future needs
    recordUrl: Optional[str] = None 
    message: Optional[str] = None

    class Config:
        allow_population_by_field_name = True

# Let's ensure all classes are defined before use.
# The order should be:
# 1. CancelExecutionRequest
# 2. ProcessPropertyValue
# 3. ProcessProperty (which uses ProcessPropertyValue)
# 4. ProcessProperties (which uses ProcessProperty)
# 5. DynamicProcessProperty
# 6. DynamicProcessProperties (which uses DynamicProcessProperty)
# 7. ExecutionRequestModel (uses ProcessProperties, DynamicProcessProperties)
# 8. ExecutionResponse

# Final structure for execution.py:
# ```python
from typing import List, Optional, Dict
from pydantic import BaseModel, Field

class CancelExecutionRequest(BaseModel):
    executionId: str
    notes: Optional[str] = None

class ProcessPropertyValue(BaseModel):
    key: str
    value: str

class ProcessProperty(BaseModel): # Represents a Process Property Component definition for overrides
    componentId: str
    ProcessPropertyValue: List[ProcessPropertyValue]

class ProcessProperties(BaseModel): # Container for multiple Process Property Component overrides
    ProcessProperty: List[ProcessProperty]

class DynamicProcessProperty(BaseModel): # Actual key-value for a dynamic property
    Name: str
    Value: str

class DynamicProcessProperties(BaseModel): # Container for DynamicProcessProperty list
    DynamicProcessProperty: List[DynamicProcessProperty]

class ExecutionRequestModel(BaseModel):
    atomId: str
    processId: str
    ProcessProperties: Optional[ProcessProperties] = None
    DynamicProcessProperties: Optional[DynamicProcessProperties] = None # Corrected type

    class Config:
        allow_population_by_field_name = True
        # If the JSON field is "DynamicProcessProperties" and it's an object containing a list
        # then the alias is not needed here if the Pydantic field name matches the JSON key.
        # The openapi.json shows:
        # "DynamicProcessProperties": { "DynamicProcessProperty": [ ... ] }
        # This means `DynamicProcessProperties` is a key in the JSON that holds an object,
        # and that object has a key `DynamicProcessProperty` which is a list.
        # So, `DynamicProcessProperties: Optional[DynamicProcessPropertiesContainer]` where
        # `DynamicProcessPropertiesContainer` has `DynamicProcessProperty: List[DynamicProcessPropertyActual]`
        # This matches my current structure with `DynamicProcessProperties` model containing the list.

class ExecutionResponse(BaseModel):
    executionId: str # As per task spec, even if not in immediate POST response
    requestId: Optional[str] = None
    recordUrl: Optional[str] = None
    message: Optional[str] = None

    class Config:
        allow_population_by_field_name = True

# ```
# This refined structure looks correct based on openapi.json examples for ExecutionRequest.
# The `ExecutionResponse` is per task spec, acknowledging it differs from typical immediate API responses for async tasks.

# Now, update `boomi/models/__init__.py`.
# I need to read it first to see its current content.
read_files(["boomi/models/__init__.py"])
