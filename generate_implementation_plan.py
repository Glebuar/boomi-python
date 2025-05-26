import json
import sys
import re

def clean_sdk_method_name(suspected_name, resource_name):
    # Simple cleaning: ensure snake_case, remove redundant resource name if present
    # Example: get_pet_findByStatus -> find_pet_by_status or get_pet_status
    # Example: delete_pet_by_petid -> delete_pet_by_id
    name = suspected_name.lower()
    resource_name_lower = resource_name.lower()

    # Remove "get_resource_resource" type duplications
    name = name.replace(f"get_{resource_name_lower}_{resource_name_lower}", f"get_{resource_name_lower}")
    name = name.replace(f"delete_{resource_name_lower}_{resource_name_lower}", f"delete_{resource_name_lower}")
    name = name.replace(f"update_{resource_name_lower}_{resource_name_lower}", f"update_{resource_name_lower}")

    # Standardize "by_id" if param is clearly an id
    name = re.sub(r'_by_[a-zA-Z0-9]+id$', '_by_id', name)
    
    # If suspected name starts with http method like "get_resource_action"
    # and action seems to be part of SDK method conventions (e.g. find_by_status)
    # we might prefer a shorter name if the SDK already has conventions for it.
    # This is complex and depends on SDK's style. For now, keep it simple.
    # If the suspected name is like "get_pet_findbystatus", prefer "find_pet_by_status"
    # This logic is tricky without knowing the SDK's specific naming patterns well.
    
    # A common pattern is action_resource_modifier, e.g. find_pet_by_status
    # The suspected names are often httpmethod_resource_action
    # Let's try to make it more like SDK style if possible.
    
    parts = name.split('_')
    if len(parts) > 2 and parts[0] in ['get', 'create', 'update', 'delete', 'post', 'put']: # http method prefix
        # if parts[1] == resource_name_lower: # e.g. get_pet_action -> action_pet
        #    action_parts = parts[2:]
        #    name = "_".join(action_parts) + "_" + resource_name_lower
        # else: # e.g. get_something_else -> no change from this rule
        pass


    # Ensure it's valid Python identifier (very basic check)
    name = re.sub(r'[^a-zA-Z0-9_]', '', name)
    if not name[0].isalpha() and name[0] != '_':
        name = "_" + name # Ensure starts with letter or underscore

    return name.strip('_')

def generate_method_signature(method_name, path, http_method):
    params = ["self"]
    path_params = re.findall(r"{([^}]+)}", path)
    for p_param in path_params:
        params.append(f"{p_param.lower()}_val: str") # Assuming path params are strings

    # Default return type
    return_type = "dict" 

    if http_method in ["POST", "PUT", "PATCH"]:
        # Check if it looks like a query method (often POST for complex queries)
        if "query" in method_name.lower() or "search" in method_name.lower():
            params.append("query_payload: dict")
            return_type = "List[dict]" # Queries often return lists
        else:
            params.append("payload: dict")
    elif http_method == "GET":
        # If it's a list-like operation (no path params, or name suggests list)
        if not path_params and ("list" in method_name or "query" in method_name):
             return_type = "List[dict]"
        # If it has path params, it's likely getting a single item
        elif path_params:
            return_type = "dict"
        # Could also have query params for GET list/query, not explicitly modeled here yet
        # For example, if path is /Resource and method_name is list_..._by_status
        # We might infer a status: str query parameter.
        # For now, keeping it simpler.

    elif http_method == "DELETE":
        return_type = "bool" # Common for delete to return success/fail

    return f"{method_name}({', '.join(params)}) -> {return_type}"

def describe_parameter_handling(path, http_method):
    notes = []
    path_params = re.findall(r"{([^}]+)}", path)
    for p_param in path_params:
        notes.append(f"Path parameter '{p_param}' (passed as {p_param.lower()}_val) replaces {{{p_param}}} in the API path.")

    if http_method in ["POST", "PUT", "PATCH"]:
        if "query" in path.lower() or "query" in http_method.lower(): # crude check for query
             notes.append("`query_payload` is sent as the JSON request body.")
        else:
            notes.append("`payload` is sent as the JSON request body.")
    
    # Placeholder for query parameter handling if we add that inference
    # Example: if a GET list method has "by_status" in its name, we could suggest a "status" query param
    # if "by_status" in method_name and http_method == "GET":
    # notes.append("Query parameter 'status' (passed as status) should be added to the request URL.")

    if not notes:
        return "No explicit path or body parameters. Review API docs for potential query parameters."
    return " ".join(notes)

def describe_response_handling(http_method):
    if http_method == "DELETE":
        return "Return `True` on successful deletion (e.g., 204 No Content), raise an exception or return `False` on failure."
    if http_method == "GET" and "list" in http_method.lower(): # Simplistic check
        return "Return `response.json().get('result', [])` or similar for list responses, handling pagination if applicable."
    return "Return `response.json()` if the response contains a JSON body. Handle potential errors (e.g., non-2xx status codes)."


def create_implementation_plan(discrepancy_report_str):
    try:
        report = json.loads(discrepancy_report_str)
    except json.JSONDecodeError as e:
        print(f"Error decoding discrepancy report JSON: {e}", file=sys.stderr)
        return "{}" # Return empty JSON object on error

    plan = {}
    
    # 1. Identify target resources
    target_resources = set(["Atom", "Account"]) # Core focus
    
    # Add from missing_resources
    if "missing_resources" in report:
        for res_name in report["missing_resources"]:
            if len(target_resources) < 4: # Limit to 2 additional for now
                target_resources.add(res_name)
            else:
                break
                
    # Add from missing_endpoints (if many are missing for a resource not yet chosen)
    if "missing_endpoints" in report and len(target_resources) < 4:
        # Sort resources by number of missing endpoints
        sorted_missing_ep_resources = sorted(
            report["missing_endpoints"].items(),
            key=lambda item: len(item[1]),
            reverse=True
        )
        for res_name, _ in sorted_missing_ep_resources:
            if res_name not in target_resources:
                target_resources.add(res_name)
                if len(target_resources) >= 4:
                    break
    
    # Generate plan for selected resources
    for resource_name in list(target_resources): # Iterate over a copy as we might remove
        if resource_name not in report.get("missing_endpoints", {}):
            # If the resource was selected (e.g. "Account") but has no missing endpoints in the report
            # or if it was a "missing_resource" entirely (it will be in missing_endpoints due to how prev script works)
            # We should check if it's in missing_resources and plan for its basic CRUD if so.
            if resource_name in report.get("missing_resources", []):
                 # This resource is entirely missing. Plan for basic CRUD.
                 # This part is more complex as we need to invent endpoints.
                 # For now, we'll rely on missing_endpoints which *should* cover missing_resources too.
                 # The previous script (compare_spec_sdk.py) adds all endpoints of a missing resource
                 # to the missing_endpoints section for that resource.
                 pass # Covered by missing_endpoints check below.
            else:
                continue # No missing endpoints for this specifically focused resource.

        plan[resource_name] = []
        
        # Ensure missing_endpoints for this resource exists and is a list
        endpoints_to_plan = report.get("missing_endpoints", {}).get(resource_name, [])
        if not isinstance(endpoints_to_plan, list):
            continue


        for endpoint_info in endpoints_to_plan:
            api_path = endpoint_info["path"]
            http_method = endpoint_info["method"]
            
            # Use suspected_sdk_method_name as a base, then clean it.
            base_name = endpoint_info.get("suspected_sdk_method_name", f"{http_method.lower()}_{resource_name.lower()}_action")
            sdk_method_name = clean_sdk_method_name(base_name, resource_name)
            
            # Refine SDK method name if it's too generic from suspected_sdk_method_name
            # E.g. if suspected is "get_pet_pet_by_id", clean_sdk_method_name might make it "get_pet_by_id"
            # If suspected is "get_pet_findbystatus", clean_sdk_method_name might make it "get_pet_findbystatus"
            # We want "find_pet_by_status" or similar based on SDK conventions.
            # This is where deeper knowledge of SDK conventions would be useful.
            # For now, the generated name from `generate_suspected_sdk_name` in the previous step
            # and `clean_sdk_method_name` here will have to suffice.

            # A special case: if method name from SDK was in unmatched_sdk_methods and seems to fit path/method
            # This is advanced and not implemented here yet. Requires cross-referencing unmatched_sdk_methods.

            sdk_method_signature = generate_method_signature(sdk_method_name, api_path, http_method)
            param_handling = describe_parameter_handling(api_path, http_method) # Pass sdk_method_name if needed for hints
            resp_handling = describe_response_handling(http_method)

            plan[resource_name].append({
                "sdk_method_name": sdk_method_name,
                "sdk_method_signature": sdk_method_signature,
                "api_path": api_path,
                "http_method": http_method,
                "parameter_handling": param_handling,
                "response_handling": resp_handling
            })

    return json.dumps(plan, indent=2)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(json.dumps({"error": "Usage: python generate_implementation_plan.py <discrepancy_report_json_string>"}), file=sys.stderr)
        sys.exit(1)

    discrepancy_json_str = sys.argv[1]
    
    implementation_plan_json = create_implementation_plan(discrepancy_json_str)
    print(implementation_plan_json)
