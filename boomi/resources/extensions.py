from typing import List, Any, Dict # Added Dict for body type hints for now
from .._http import _HTTP
from ..models.extensions import EnvironmentExtensionsData, EnvironmentExtensionsResponse
# If EnvironmentExtensionsQueryResponse is needed, it would be imported here.
# For now, handling the list extraction directly as per task example.

# A placeholder for a more specific QueryConfig model if we were to type query bodies
# For now, using Dict[str, Any] as per task's existing type hint for query bodies
ExtensionsQueryConfig = Dict[str, Any]

class Extensions:
    def __init__(self, http: _HTTP):
        self._http = http

    def get(self, env_id: str) -> EnvironmentExtensionsResponse:
        """
        Retrieves the extension values for the environment having the specified ID.
        """
        resp = self._http.get(f"/EnvironmentExtensions/{env_id}")
        data = resp.json()
        if hasattr(EnvironmentExtensionsResponse, "model_validate"):
            return EnvironmentExtensionsResponse.model_validate(data)
        return EnvironmentExtensionsResponse.parse_obj(data) # For Pydantic v1 compatibility

    def update(self, env_id: str, extensions_payload: EnvironmentExtensionsData) -> EnvironmentExtensionsResponse:
        """
        Updates the extension values for the environment having the specified ID.
        The extensions_payload includes the 'partial' flag and all extension data.
        """
        # Using by_alias=True to ensure field names match JSON keys if aliases are used in models
        # Using exclude_none=True to avoid sending optional fields that are not set
        payload_dict = extensions_payload.model_dump(by_alias=True, exclude_none=True)
        resp = self._http.post(f"/EnvironmentExtensions/{env_id}", json=payload_dict)
        data = resp.json()
        
        if hasattr(EnvironmentExtensionsResponse, "model_validate"):
            return EnvironmentExtensionsResponse.model_validate(data)
        return EnvironmentExtensionsResponse.parse_obj(data) # For Pydantic v1 compatibility

    def query(self, body: ExtensionsQueryConfig) -> List[EnvironmentExtensionsResponse]:
        """
        Queries for EnvironmentExtensions objects.
        The response is typically a list of EnvironmentExtensions objects.
        The 'body' for the query should conform to the QueryConfig structure for EnvironmentExtensions.
        """
        resp = self._http.post("/EnvironmentExtensions/query", json=body)
        data = resp.json()
        
        # Assuming the actual extension data is in a 'result' field in the response JSON
        # This is a common pattern for Boomi API query responses.
        results_data = data.get("result", [])
        
        parsed_results: List[EnvironmentExtensionsResponse] = []
        for item_data in results_data:
            if hasattr(EnvironmentExtensionsResponse, "model_validate"):
                parsed_results.append(EnvironmentExtensionsResponse.model_validate(item_data))
            else:
                parsed_results.append(EnvironmentExtensionsResponse.parse_obj(item_data)) # For Pydantic v1
        return parsed_results

    def query_conn_field_summary(self, body: ExtensionsQueryConfig) -> Any: # Kept as Any for now
        """
        Queries for EnvironmentConnectionFieldExtensionSummary objects.
        The 'body' for the query should conform to the QueryConfig structure for EnvironmentConnectionFieldExtensionSummary.
        Response parsing uses .json() as specific models for its items were not part of the previous subtask.
        """
        # TODO: Implement specific Pydantic models for EnvironmentConnectionFieldExtensionSummaryQueryResponse
        # and EnvironmentConnectionFieldExtensionSummary if needed for stronger typing.
        return self._http.post(
            "/EnvironmentConnectionFieldExtensionSummary/query", json=body
        ).json()
