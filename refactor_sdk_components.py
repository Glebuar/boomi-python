import json
import sys
import ast
import re
import astor # Ensure astor is available

# --- AST Helper Functions (Minimal for this task, more could be added) ---
def find_class_node(tree, class_name):
    for node in tree.body:
        if isinstance(node, ast.ClassDef) and node.name == class_name:
            return node
    return None

def find_method_node(class_node, method_name):
    if not class_node:
        return None
    for node in class_node.body:
        if isinstance(node, ast.FunctionDef) and node.name == method_name:
            return node
    return None

def get_pydantic_field_names(class_node):
    """Extracts field names from a Pydantic-like model (annotated class attributes)."""
    fields = set()
    if not class_node:
        return fields
    for node in class_node.body:
        if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            fields.add(node.target.id)
        # Could also look for `ClassVar` or other Pydantic specifics if needed
    return fields

# --- Main Analysis and Refactoring Logic ---
def analyze_and_refactor_components(
    discrepancy_report_json_str: str,
    openapi_spec_json_str: str,
    current_components_py_content: str,
    current_component_model_py_content: str,
    component_schema_json_str: str,
    component_metadata_schema_json_str: str
):
    model_summary_log = ["Model Review for boomi/models/component.py:"]
    resource_summary_log = ["Resource Method Review for boomi/resources/components.py:"]
    model_changes_made = False
    resource_changes_made = False

    try:
        # discrepancy_report = json.loads(discrepancy_report_json_str) # Not heavily used in this script yet
        openapi_spec = json.loads(openapi_spec_json_str)
        component_schema = json.loads(component_schema_json_str)
        component_metadata_schema = json.loads(component_metadata_schema_json_str)
    except json.JSONDecodeError as e:
        error_msg = f"Error decoding JSON input: {e}"
        return (current_component_model_py_content, [error_msg],
                current_components_py_content, [error_msg])

    # --- 1. Model Review (boomi/models/component.py) ---
    model_tree = ast.parse(current_component_model_py_content)
    
    # Review Component model
    component_class_node = find_class_node(model_tree, "Component")
    if component_class_node:
        model_fields = get_pydantic_field_names(component_class_node)
        schema_fields = set(component_schema.get("properties", {}).keys())
        
        missing_in_model = schema_fields - model_fields
        extra_in_model = model_fields - schema_fields

        if missing_in_model:
            model_changes_made = True
            model_summary_log.append(f"- Component model: Missing fields found: {missing_in_model}. Adding them.")
            for field_name in sorted(list(missing_in_model)):
                # Get type from schema, default to 'Any' or 'str'
                field_type_from_schema = component_schema["properties"][field_name].get("type", "string")
                python_type = "str" # Default
                if field_type_from_schema == "integer": python_type = "int"
                elif field_type_from_schema == "boolean": python_type = "bool"
                elif field_type_from_schema == "array": python_type = "list" # Needs List[Something]
                elif field_type_from_schema == "object": python_type = "dict" # Needs Dict[str, Something]
                
                # Create AnnAssign node: field_name: python_type
                # This assumes Pydantic style. If it's plain class, __init__ would be modified.
                # The current model looks Pydantic-like.
                new_field_ann = ast.AnnAssign(
                    target=ast.Name(id=field_name, ctx=ast.Store()),
                    annotation=ast.Name(id=python_type, ctx=ast.Load()), # Simplified type hint
                    simple=1 # Indicates no value assignment here
                )
                # Insert into class body (e.g., after last AnnAssign or at top)
                # A simple append is fine for now.
                component_class_node.body.append(new_field_ann)
            model_summary_log.append(f"  - Added: {', '.join(sorted(list(missing_in_model)))}")


        if extra_in_model:
            # Decide whether to remove or just note. For now, just note.
            model_summary_log.append(f"- Component model: Extra fields found: {extra_in_model}. These were not removed automatically.")
        
        if not missing_in_model and not extra_in_model:
            model_summary_log.append("- Component model: Fields align with Component.json schema.")

    else:
        model_summary_log.append("- Component class not found in boomi/models/component.py.")

    # Review ComponentMetadata model (similar logic)
    metadata_class_node = find_class_node(model_tree, "ComponentMetadata")
    if metadata_class_node:
        model_fields = get_pydantic_field_names(metadata_class_node)
        schema_fields = set(component_metadata_schema.get("properties", {}).keys())
        
        missing_in_model = schema_fields - model_fields
        extra_in_model = model_fields - schema_fields

        if missing_in_model:
            model_changes_made = True
            model_summary_log.append(f"- ComponentMetadata model: Missing fields found: {missing_in_model}. Adding them.")
            for field_name in sorted(list(missing_in_model)):
                field_type_from_schema = component_metadata_schema["properties"][field_name].get("type", "string")
                python_type = "str" # Default
                if field_type_from_schema == "integer": python_type = "int"
                elif field_type_from_schema == "boolean": python_type = "bool"
                
                new_field_ann = ast.AnnAssign(
                    target=ast.Name(id=field_name, ctx=ast.Store()),
                    annotation=ast.Name(id=python_type, ctx=ast.Load()),
                    simple=1
                )
                metadata_class_node.body.append(new_field_ann)
            model_summary_log.append(f"  - Added: {', '.join(sorted(list(missing_in_model)))}")


        if extra_in_model:
            model_summary_log.append(f"- ComponentMetadata model: Extra fields found: {extra_in_model}. Not removed.")
        
        if not missing_in_model and not extra_in_model:
            model_summary_log.append("- ComponentMetadata model: Fields align with ComponentMetadata.json schema.")
    else:
        model_summary_log.append("- ComponentMetadata class not found in boomi/models/component.py.")

    if not model_changes_made:
        model_summary_log.append("No changes made to boomi/models/component.py based on schema field comparison.")

    # --- 2. Resource Method Review (boomi/resources/components.py) ---
    # This part is highly dependent on specific discrepancies identified.
    # The problem description is generic: "If misalignments are found..."
    # For this script, I'll focus on one potential misalignment:
    # If OpenAPI specifies JSON for component operations, but SDK uses XML.
    # This requires checking the `openapi_spec` for paths like `/Component` and `/Component/{id}`.
    
    resource_tree = ast.parse(current_components_py_content)
    components_class_node = find_class_node(resource_tree, "Components")
    
    if components_class_node:
        # Example: Check the 'get' method.
        # SDK's get method: `get(self, cid: str) -> Component`, uses `_HDR_XML`, `_attrs(r.content)`
        # Let's check if OpenAPI for `GET /Component/{componentId}` specifies JSON response.
        
        get_component_path_spec = openapi_spec.get("paths", {}).get("/Component/{componentId}", {}).get("get", {})
        produces_json = False
        if "responses" in get_component_path_spec:
            for status_code, response_spec in get_component_path_spec["responses"].items():
                if str(status_code).startswith("2"): # Success responses
                    if "content" in response_spec and "application/json" in response_spec["content"]:
                        produces_json = True
                        break
        
        if produces_json:
            resource_summary_log.append("- GET /Component/{componentId} in OpenAPI produces JSON.")
            
            get_method_node = find_method_node(components_class_node, "get")
            if get_method_node:
                # Check if current 'get' method implies XML handling
                # Current: r = self._http.get(f"/Component/{cid}", headers=_HDR_XML)
                #          return Component.model_validate(self._attrs(r.content))
                # This clearly indicates XML. If OpenAPI says JSON, this is a misalignment.
                
                # Find `headers=_HDR_XML` in the http call
                xml_header_used = False
                returns_attrs_content = False

                for stmt in get_method_node.body:
                    if isinstance(stmt, ast.Assign) and isinstance(stmt.value, ast.Call): # r = self._http.get(...)
                        if isinstance(stmt.value.func, ast.Attribute) and stmt.value.func.attr == "get":
                            for kw in stmt.value.keywords:
                                if kw.arg == "headers" and isinstance(kw.value, ast.Name) and kw.value.id == "_HDR_XML":
                                    xml_header_used = True
                                    stmt.value.keywords = [k for k in stmt.value.keywords if not (k.arg == "headers" and isinstance(k.value, ast.Name) and k.value.id == "_HDR_XML")]
                                    xml_header_used = True
                                    resource_changes_made = True

                    if isinstance(stmt, ast.Return) and isinstance(stmt.value, ast.Call): # return Component.model_validate(...)
                        # Check if it's Component.model_validate(self._attrs(r.content))
                        if isinstance(stmt.value.func, ast.Attribute) and stmt.value.func.attr == "model_validate":
                             call_arg = stmt.value.args[0]
                             if isinstance(call_arg, ast.Call) and \
                                isinstance(call_arg.func, ast.Attribute) and call_arg.func.attr == "_attrs":
                                returns_attrs_content = True
                                # Change to: return Component.model_validate(r.json())
                                stmt.value.args[0] = ast.Call(
                                    func=ast.Attribute(
                                        value=ast.Name(id="r", ctx=ast.Load()), # Assuming response variable is 'r'
                                        attr="json", ctx=ast.Load()),
                                    args=[], keywords=[]
                                )
                                resource_changes_made = True
                
                if xml_header_used or returns_attrs_content:
                    resource_summary_log.append(f"- SDK method 'get' for Components seems to use XML. Refactoring for JSON response as per OpenAPI.")
                else:
                    resource_summary_log.append(f"- SDK method 'get' for Components already seems to handle JSON or its XML usage couldn't be confirmed for refactoring by this script.")

            else:
                resource_summary_log.append("- SDK method 'get' for Components not found for review.")
        else:
            resource_summary_log.append("- GET /Component/{componentId} in OpenAPI does not clearly specify JSON response or path not found. No changes to 'get' method based on this check.")
            
        # Similar checks could be done for create, update, delete if they use XML and OpenAPI implies JSON.
        # This is a simplified example focusing on 'get'.

    else:
        resource_summary_log.append("- Components class not found in boomi/resources/components.py.")

    if not resource_changes_made:
        resource_summary_log.append("No specific misalignments addressed by this script in boomi/resources/components.py.")

    # --- Return Results ---
    final_model_code = astor.to_source(model_tree) if model_changes_made else current_component_model_py_content
    final_resource_code = astor.to_source(resource_tree) if resource_changes_made else current_components_py_content
    
    return final_model_code, model_summary_log, final_resource_code, resource_summary_log

if __name__ == '__main__':
    if len(sys.argv) != 7:
        print("Usage: python refactor_sdk_components.py <discrepancy_json> <openapi_json> <components_py_content> <component_model_py_content> <component_schema_json> <component_metadata_schema_json>", file=sys.stderr)
        sys.exit(1)
        
    discrepancy_json_arg = sys.argv[1]
    openapi_json_arg = sys.argv[2]
    components_py_content_arg = sys.argv[3]
    component_model_py_content_arg = sys.argv[4]
    component_schema_json_arg = sys.argv[5]
    component_metadata_schema_json_arg = sys.argv[6]
    
    model_code, model_sum, res_code, res_sum = analyze_and_refactor_components(
        discrepancy_json_arg, openapi_json_arg, components_py_content_arg,
        component_model_py_content_arg, component_schema_json_arg,
        component_metadata_schema_json_arg
    )
    
    # Print structure for agent to parse
    print(model_code)
    print("--- model_summary_separator ---", file=sys.stderr)
    print("\n".join(model_sum), file=sys.stderr)
    print("--- code_separator ---", file=sys.stderr) # Separates model code from resource code in output stream
    print(res_code)
    print("--- resource_summary_separator ---", file=sys.stderr)
    print("\n".join(res_sum), file=sys.stderr)
