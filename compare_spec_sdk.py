import json
import sys
import re

def generate_suspected_sdk_name(path, http_method, resource_name_openapi):
    action = ""
    path_parts_cleaned = [part for part in path.split('/') if part and not part.startswith('{')]
    id_param_match = re.search(r"{([^}]+)}", path)
    id_param_exists = bool(id_param_match)
    id_param_name = id_param_match.group(1).lower() if id_param_match else "id"

    # Normalize resource_name_openapi for use in method names
    sdk_resource_name_part = resource_name_openapi.lower()

    if http_method == 'GET':
        if id_param_exists:
            # GET /Resource/{id} -> get_resource_by_id
            action = f"get_{sdk_resource_name_part}_by_{id_param_name}"
        elif path_parts_cleaned and path_parts_cleaned[-1].lower() != sdk_resource_name_part and path_parts_cleaned[-1].lower() != sdk_resource_name_part + 's':
            # GET /Resource/subpath -> get_resource_subpath
            action = f"get_{sdk_resource_name_part}_{'_'.join(path_parts_cleaned[1:])}" # Assuming first part is resource
        else:
            # GET /Resource -> list_resources
            action = f"list_{sdk_resource_name_part}s" # or list_resource
            if sdk_resource_name_part.endswith('s'): # Avoid list_atoms_s
                 action = f"list_{sdk_resource_name_part}"


    elif http_method == 'POST':
        if not path_parts_cleaned or path_parts_cleaned[-1].lower() == sdk_resource_name_part or path_parts_cleaned[-1].lower() == sdk_resource_name_part + 's':
             # POST /Resource -> create_resource
            action = f"create_{sdk_resource_name_part}"
        else:
            # POST /Resource/action -> action_resource or resource_action
            action_name = '_'.join(p for p in path_parts_cleaned if p.lower() != sdk_resource_name_part and p.lower() != sdk_resource_name_part+'s')
            if id_param_exists:
                action = f"{action_name}_{sdk_resource_name_part}_by_{id_param_name}"
            else:
                action = f"{action_name}_{sdk_resource_name_part}"
            if not action_name: # e.g. POST /Resource/{id} (uncommon for create, maybe update-like)
                action = f"update_{sdk_resource_name_part}_by_{id_param_name}"


    elif http_method == 'PUT':
        # PUT /Resource/{id} -> update_resource_by_id
        if id_param_exists:
            action = f"update_{sdk_resource_name_part}_by_{id_param_name}"
        else: # PUT /Resource (bulk update?)
            action = f"update_{sdk_resource_name_part}s"


    elif http_method == 'DELETE':
        # DELETE /Resource/{id} -> delete_resource_by_id
        if id_param_exists:
            action = f"delete_{sdk_resource_name_part}_by_{id_param_name}"
        else: # DELETE /Resource (bulk delete?)
             action = f"delete_{sdk_resource_name_part}s"

    elif http_method == 'PATCH':
        if id_param_exists:
            action = f"patch_{sdk_resource_name_part}_by_{id_param_name}"
        else:
            action = f"patch_{sdk_resource_name_part}s"
    else:
        action = f"{http_method.lower()}_{sdk_resource_name_part}_{'_'.join(path_parts_cleaned[1:]) if len(path_parts_cleaned) > 1 else ''}".strip('_')

    return action.replace("__", "_") # Clean up double underscores

def match_endpoints(openapi_data, sdk_data):
    report = {
        "missing_resources": [],
        "missing_endpoints": {},
        "implemented_endpoints": {},
        "unmatched_sdk_methods": {}
    }

    openapi_resource_names = set(openapi_data.keys())
    sdk_resource_names = set(sdk_data.keys())

    for resource_name in openapi_resource_names:
        if resource_name not in sdk_resource_names:
            report["missing_resources"].append(resource_name)
        else:
            report["missing_endpoints"].setdefault(resource_name, [])
            report["implemented_endpoints"].setdefault(resource_name, [])
            report["unmatched_sdk_methods"][resource_name] = list(sdk_data[resource_name])

    for openapi_resource_name, openapi_endpoints in openapi_data.items():
        if openapi_resource_name in report["missing_resources"]:
            for endpoint in openapi_endpoints:
                 report["missing_endpoints"].setdefault(openapi_resource_name, []).append({
                    "path": endpoint["path"],
                    "method": endpoint["method"],
                    "suspected_sdk_method_name": generate_suspected_sdk_name(endpoint["path"], endpoint["method"], openapi_resource_name)
                })
            continue

        sdk_methods_for_resource = sdk_data.get(openapi_resource_name, [])
        
        for endpoint in openapi_endpoints:
            path = endpoint["path"]
            http_method = endpoint["method"]
            matched_sdk_method = None
            
            path_lower = path.lower()
            resource_lower = openapi_resource_name.lower()
            
            # Simplified matching logic for demonstration
            # This needs to be much more robust and use the conventions from the task description

            potential_matches = []
            if http_method == 'GET':
                if re.search(f"/{resource_lower}/{{[^}}]+}}$", path_lower) or re.search(f"/{resource_lower}s/{{[^}}]+}}$", path_lower): # GET /Resource/{id}
                    potential_matches = ["get", "get_by_id", f"get_{resource_lower}_by_id", "retrieve"]
                    id_param_name_match = re.search(r"{([^}]+)}", path)
                    if id_param_name_match:
                        id_param_name = id_param_name_match.group(1).lower()
                        potential_matches.extend([f"get_by_{id_param_name}", f"get_{resource_lower}_by_{id_param_name}"])

                elif path_lower.endswith(f"/{resource_lower}") or path_lower.endswith(f"/{resource_lower}s"): # GET /Resource or /Resources
                    potential_matches = ["list", "query", f"list_{resource_lower}s", f"list_{resource_lower}"]
                else: # Other GET, e.g., /Resource/action or /Resource/{id}/sub_action
                    action_part = path_lower.split('/')[-1]
                    if action_part and not action_part.startswith('{'):
                        potential_matches = [action_part, f"get_{action_part}", f"{action_part}_{resource_lower}"]


            elif http_method == 'POST':
                if path_lower.endswith(f"/{resource_lower}") or path_lower.endswith(f"/{resource_lower}s"): # POST /Resource
                    potential_matches = ["create", f"create_{resource_lower}", "add"]
                elif "/query" in path_lower:
                    potential_matches = ["query", f"query_{resource_lower}s"]
                else: # POST /Resource/action or /Resource/{id}/action
                    action_part = path_lower.split('/')[-1]
                    if action_part and not action_part.startswith('{'):
                         potential_matches = [action_part, f"{action_part}_{resource_lower}", f"execute_{action_part}"]


            elif http_method == 'PUT': # PUT /Resource/{id}
                 potential_matches = ["update", f"update_{resource_lower}", "modify"]
                 id_param_name_match = re.search(r"{([^}]+)}", path)
                 if id_param_name_match:
                     id_param_name = id_param_name_match.group(1).lower()
                     potential_matches.extend([f"update_by_{id_param_name}", f"update_{resource_lower}_by_{id_param_name}"])


            elif http_method == 'DELETE': # DELETE /Resource/{id}
                potential_matches = ["delete", f"delete_{resource_lower}", "remove"]
                id_param_name_match = re.search(r"{([^}]+)}", path)
                if id_param_name_match:
                    id_param_name = id_param_name_match.group(1).lower()
                    potential_matches.extend([f"delete_by_{id_param_name}", f"delete_{resource_lower}_by_{id_param_name}"])
            
            elif http_method == 'PATCH': # PATCH /Resource/{id}
                 potential_matches = ["patch", f"patch_{resource_lower}", "update_partial"]
                 id_param_name_match = re.search(r"{([^}]+)}", path)
                 if id_param_name_match:
                     id_param_name = id_param_name_match.group(1).lower()
                     potential_matches.extend([f"patch_by_{id_param_name}", f"patch_{resource_lower}_by_{id_param_name}"])


            # Check potential matches against available SDK methods
            # This is a simple "is in" check. A more advanced system might use fuzzy matching or scoring.
            for p_match in potential_matches:
                # Normalize p_match (e.g. case, underscores) if SDK methods have a very consistent style
                # For now, direct check
                if p_match in sdk_methods_for_resource:
                    matched_sdk_method = p_match
                    break
                # Try converting camelCase or PascalCase from suspected name to snake_case if SDK uses snake_case
                # e.g. findByStatus -> find_by_status
                snake_case_match = re.sub(r'(?<!^)(?=[A-Z])', '_', p_match).lower()
                if snake_case_match in sdk_methods_for_resource:
                    matched_sdk_method = snake_case_match
                    break
            
            # Fallback: check if operationId (if available in openapi_endpoint object) matches
            if not matched_sdk_method and "operationId" in endpoint:
                op_id = endpoint["operationId"]
                # Direct match or snake_case version of operationId
                if op_id in sdk_methods_for_resource:
                    matched_sdk_method = op_id
                else:
                    op_id_snake = re.sub(r'(?<!^)(?=[A-Z])', '_', op_id).lower()
                    if op_id_snake in sdk_methods_for_resource:
                        matched_sdk_method = op_id_snake


            if matched_sdk_method:
                report["implemented_endpoints"][openapi_resource_name].append({
                    "path": path,
                    "method": http_method,
                    "sdk_method_name": matched_sdk_method
                })
                if matched_sdk_method in report["unmatched_sdk_methods"].get(openapi_resource_name, []):
                    report["unmatched_sdk_methods"][openapi_resource_name].remove(matched_sdk_method)
            else:
                report["missing_endpoints"][openapi_resource_name].append({
                    "path": path,
                    "method": http_method,
                    "suspected_sdk_method_name": generate_suspected_sdk_name(path, http_method, openapi_resource_name)
                })
        
        if openapi_resource_name in report["unmatched_sdk_methods"] and not report["unmatched_sdk_methods"][openapi_resource_name]:
            del report["unmatched_sdk_methods"][openapi_resource_name]
        if openapi_resource_name in report["missing_endpoints"] and not report["missing_endpoints"][openapi_resource_name]:
            del report["missing_endpoints"][openapi_resource_name]

    for sdk_resource_name in sdk_resource_names:
        if sdk_resource_name not in openapi_resource_names:
            if sdk_data.get(sdk_resource_name):
                 report["unmatched_sdk_methods"].setdefault(sdk_resource_name, []).extend(sdk_data[sdk_resource_name])
                 report["unmatched_sdk_methods"][sdk_resource_name] = sorted(list(set(report["unmatched_sdk_methods"][sdk_resource_name])))

    if not report.get("missing_resources"): report.pop("missing_resources", None)
    report = {k: v for k, v in report.items() if v}

    return report

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(json.dumps({"error": "Usage: python compare_spec_sdk.py <openapi_spec_json_string> <sdk_implementation_json_string>"}), file=sys.stderr)
        sys.exit(1)

    openapi_json_str = sys.argv[1]
    sdk_json_str = sys.argv[2]

    try:
        openapi_spec = json.loads(openapi_json_str)
        sdk_implementation = json.loads(sdk_json_str)
    except json.JSONDecodeError as e:
        print(json.dumps({"error": f"JSON decoding error: {e}. Input1: '{openapi_json_str[:100]}...', Input2: '{sdk_json_str[:100]}...'"}), file=sys.stderr)
        sys.exit(1)

    comparison_report = match_endpoints(openapi_spec, sdk_implementation)
    print(json.dumps(comparison_report, indent=2))
