import json
import sys
import re

def update_component_documentation(
    current_doc_contents: dict, 
    component_sdk_changes_str: str
    # doc_update_plan_str is not explicitly used here as changes are specific
) -> dict:
    try:
        component_changes = json.loads(component_sdk_changes_str)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON input for component_sdk_changes: {e}", file=sys.stderr)
        return current_doc_contents

    new_contents = current_doc_contents.copy()

    # Extract Component specific changes
    # Component model: Added description: str, version: int.
    # Components.get() method: Refactored for JSON response, uses Component.model_validate(r.json()).
    
    model_added_fields = component_changes.get("model_added_fields", []) # e.g., ["description: str", "version: int"]
    get_method_refactored_for_json = component_changes.get("get_method_json_response", False)

    # --- 1. Update docs/resources.md ---
    if "docs/resources.md" in new_contents and get_method_refactored_for_json:
        content = new_contents["docs/resources.md"]
        
        # Update Components.get() description
        # Look for "### Get Component"
        get_component_pattern = re.compile(
            r"(### Get Component\s*\n\n)(.*?)(?=\n###|\n##|\Z)", 
            re.MULTILINE | re.DOTALL
        )
        
        def replace_get_component_desc(match):
            original_header = match.group(1)
            # original_desc_block = match.group(2) # Old description
            
            new_desc = (
                f"{original_header}"
                f"Retrieves component details by its ID. The API is expected to return JSON, which is then validated into a `Component` model instance.\n\n"
                f"**Signature:**\n```python\nget(self, cid: str) -> Component\n```\n\n"
                f"**Parameters:**\n- `cid` (str): The ID of the component to retrieve.\n\n"
                f"**Returns:**\n- A `Component` object populated with the component's details (including new fields like `description` and `version`).\n\n"
                f"**Example:**\n```python\ncomponent_details = client.components.get(cid=\"comp-123\")\n"
                f"print(component_details.name)\n"
                f"# Access new fields if available\n"
                f"# print(component_details.version)\n"
                f"# print(component_details.description)\n```\n"
            )
            return new_desc

        content, num_replacements = get_component_pattern.subn(replace_get_component_desc, content, count=1)
        if num_replacements == 0:
            print("Warning (docs/resources.md): Could not find '### Get Component' section to update.", file=sys.stderr)
        
        new_contents["docs/resources.md"] = content

    # --- 2. Update docs/classes.md ---
    if "docs/classes.md" in new_contents:
        content = new_contents["docs/classes.md"]
        
        # Update Component model attributes
        if model_added_fields:
            # Look for "### Component" under "## Model Classes"
            component_model_pattern = re.compile(
                r"(### Component\s*\nRepresents a Boomi component\.\s*\n\n```python\nclass Component\(BaseModel\):\n)",
                re.MULTILINE
            )
            match = component_model_pattern.search(content)
            if match:
                insertion_point = match.end()
                # Find the end of this class definition block (before ```)
                end_block_match = re.search(r"(\n```)", content[insertion_point:])
                if end_block_match:
                    actual_insertion_point = insertion_point + end_block_match.start()
                    
                    fields_to_add_str = ""
                    for field_def_str in model_added_fields: # e.g., "description: str"
                        field_name, field_type = field_def_str.split(':')
                        field_name = field_name.strip()
                        field_type = field_type.strip()
                        # Check if field already exists (simple check, might need refinement)
                        if f"    {field_name}:" not in content[insertion_point:actual_insertion_point]:
                             fields_to_add_str += f"    {field_name}: {field_type}\n"
                    
                    if fields_to_add_str:
                        content = content[:actual_insertion_point] + fields_to_add_str + content[actual_insertion_point:]
                        
                        # Also update textual description of new fields if a pattern exists
                        # For now, focusing on the code block.
                        print(f"Info (docs/classes.md): Added fields {model_added_fields} to Component model code block.", file=sys.stderr)
                else:
                    print("Warning (docs/classes.md): Could not find end of Component model code block.", file=sys.stderr)
            else:
                print("Warning (docs/classes.md): Could not find '### Component' model section.", file=sys.stderr)

        # Update Components.get() signature/description (if needed, resources.md is primary for full desc)
        if get_method_refactored_for_json:
            # The signature `get(self, cid: str) -> Component` is likely already there.
            # The main change is behavior, primarily documented in resources.md.
            # Here, we just ensure the signature is present.
            # A more advanced script could update a short description if one exists here.
            # For now, this part is mostly a confirmation that the signature in classes.md is okay.
            # No specific textual changes to Components.get() in classes.md by this script version.
            pass # Covered by resources.md for detailed description.
            
        new_contents["docs/classes.md"] = content
        
    # --- 3. Update docs/examples.md & docs/quickstart.md ---
    for doc_path in ["docs/examples.md", "docs/quickstart.md"]:
        if doc_path in new_contents and get_method_refactored_for_json:
            content = new_contents[doc_path]
            
            # Look for examples of client.components.get()
            # Example pattern: component_details = client.components.get(...)
            # This pattern is simple; more complex regex might be needed for varied examples.
            get_example_pattern = re.compile(r"(component_details = client\.components\.get\(cid=.*\)\n)")
            
            match = get_example_pattern.search(content)
            if match:
                updated_example_snippet = (
                    match.group(1) + 
                    "# The component_details object is an instance of the Component model.\n"
                    "# It now includes 'description' and 'version' fields (if provided by the API).\n"
                    "# Example: print(component_details.description)\n"
                    "# Example: print(component_details.version)\n"
                )
                content = get_example_pattern.sub(updated_example_snippet, content, count=1)
                print(f"Info ({doc_path}): Updated example for client.components.get().", file=sys.stderr)
            else:
                print(f"Warning ({doc_path}): Could not find typical 'client.components.get()' example to update.", file=sys.stderr)
            
            new_contents[doc_path] = content
            
    return new_contents

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(json.dumps({"error": "Usage: python update_component_docs.py <current_doc_contents_json_str> <component_sdk_changes_json_str>"}), file=sys.stderr)
        sys.exit(1)

    current_doc_contents_arg = sys.argv[1]
    component_sdk_changes_arg = sys.argv[2]
    # doc_update_plan_arg is not used

    try:
        current_doc_contents_dict = json.loads(current_doc_contents_arg)
    except json.JSONDecodeError as e:
        print(json.dumps({"error": f"JSON decoding error for current_doc_contents: {e}"}), file=sys.stderr)
        sys.exit(1)
        
    updated_docs_dict = update_component_documentation(current_doc_contents_dict, component_sdk_changes_arg)
    
    print(json.dumps(updated_docs_dict, indent=2))
