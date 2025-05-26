import json
import sys
import re

def get_params_from_signature(signature_str: str) -> list:
    """Extracts parameter names from a signature string, excluding 'self'."""
    match = re.match(r"\w+\(([^)]*)\)", signature_str)
    if not match:
        return []
    params_part = match.group(1)
    if not params_part:
        return []
    
    param_names = []
    for p_decl in params_part.split(','):
        p_decl = p_decl.strip()
        param_name = p_decl.split(':')[0].strip()
        if param_name != "self":
            param_names.append(param_name)
    return param_names

def generate_conceptual_test_cases(plan_json_str: str) -> str:
    try:
        plan = json.loads(plan_json_str)
    except json.JSONDecodeError as e:
        print(f"Error decoding plan JSON: {e}", file=sys.stderr)
        return "{}"

    output_test_cases = {}
    target_resources = {"Atom": "Atoms", "Account": "Accounts"} # Map resource key in plan to SDK Class Name

    for resource_key_in_plan, sdk_class_name_val in target_resources.items():
        if resource_key_in_plan not in plan:
            continue

        output_test_cases[resource_key_in_plan] = []
        
        for method_details in plan[resource_key_in_plan]:
            sdk_method_name = method_details["sdk_method_name"]
            test_method_name = f"test_{sdk_method_name}_success"
            
            api_path = method_details["api_path"]
            http_method_verb = method_details["http_method"].lower() # e.g., "post", "get"
            
            description_parts = [
                f"Verifies that `{sdk_method_name}` calls `self._http.{http_method_verb}` with the API path '{api_path}'."
            ]

            # Path parameters
            path_params = re.findall(r"{([^}]+)}", api_path)
            if path_params:
                param_mentions = []
                # Get parameter names from SDK method signature to ensure consistency
                sdk_method_params = get_params_from_signature(method_details["sdk_method_signature"])
                
                # Heuristic: match path placeholders to SDK params.
                # Assumes SDK params for path are often like placeholder_val or just placeholder.
                for pp in path_params:
                    # Try to find corresponding SDK param name (e.g., {atomId} might be atomid_val or atom_id)
                    # This is a simple heuristic. A more robust way would be to have this mapping clearly in the plan.
                    # For now, we'll just state that they are substituted.
                    param_mentions.append(f"'{pp}'")

                if param_mentions:
                     description_parts.append(f"Path parameter(s) ({', '.join(param_mentions)}) are correctly substituted based on method arguments.")
            
            # Payload / JSON body
            # Infer payload from signature (e.g., params named 'payload', 'data', 'query_payload')
            # This relies on the signature provided in the plan.
            method_signature_params = get_params_from_signature(method_details["sdk_method_signature"])
            payload_param_name = None
            for p_name in method_signature_params:
                if p_name in ["payload", "query_payload", "data"]:
                    payload_param_name = p_name
                    break
            
            if payload_param_name and http_method_verb in ["post", "put", "patch"]:
                description_parts.append(f"The '{payload_param_name}' argument is correctly passed as the `json` argument to the `_http.{http_method_verb}` call.")

            # Return value
            return_desc = "the mocked JSON response" # Default
            if http_method_verb == "delete": # Based on common patterns
                # The plan's response_handling or signature's return type could refine this.
                # Assuming delete methods (if returning bool from signature) return True on success.
                if "bool" in method_details["sdk_method_signature"].lower():
                    return_desc = "True upon successful deletion"
            
            description_parts.append(f"Ensures the method returns {return_desc}.")
            
            final_description = " ".join(description_parts)
            
            output_test_cases[resource_key_in_plan].append({
                "test_method_name": test_method_name,
                "sdk_class_name": sdk_class_name_val,
                "sdk_method_under_test": sdk_method_name,
                "description": final_description
            })
            
    return json.dumps(output_test_cases, indent=2)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(json.dumps({"error": "Usage: python generate_test_cases.py <implementation_plan_json_string>"}), file=sys.stderr)
        sys.exit(1)

    plan_json_str_arg = sys.argv[1]
    
    conceptual_tests_json = generate_conceptual_test_cases(plan_json_str_arg)
    print(conceptual_tests_json)
