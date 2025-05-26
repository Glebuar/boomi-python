import json
import sys
import re

def parse_signature(signature_str: str):
    """Parses an SDK method signature string to get name, params, and return type."""
    match = re.match(r"(\w+)\(([^)]*)\)\s*(?:->\s*(.+))?", signature_str)
    if not match:
        # Try to handle cases where return type might be missing
        match_no_return = re.match(r"(\w+)\(([^)]*)\)", signature_str)
        if not match_no_return:
            raise ValueError(f"Invalid signature format: {signature_str}")
        name, params_str = match_no_return.groups()
        return_type_str = "Any" # Default if not specified
    else:
        name, params_str, return_type_str = match.groups()
        if return_type_str is None: 
            return_type_str = "Any"

    params = []
    if params_str:
        raw_params = params_str.split(',')
        for p_match_str in raw_params:
            p_match_str = p_match_str.strip()
            if not p_match_str: continue

            param_name_type = p_match_str.split(':', 1) # Split only on the first colon
            param_name = param_name_type[0].strip()
            
            param_type_full = "Any" # Default if no type annotation
            if len(param_name_type) > 1:
                param_type_full = param_name_type[1].strip()
            
            param_type = param_type_full.split('=')[0].strip() # Remove default value part
            
            params.append({"name": param_name, "type": param_type})
            
    return {"name": name, "params": params, "return_type": return_type_str}


def update_atom_documentation(
    doc_update_plan_str: str, 
    current_doc_contents: dict, 
    atom_sdk_changes_str: str
) -> dict:
    try:
        atom_changes = json.loads(atom_sdk_changes_str)
    except json.JSONDecodeError as e:
        print(f"Error decoding atom_sdk_changes_str: {e}", file=sys.stderr)
        return current_doc_contents

    new_contents = current_doc_contents.copy()

    atom_refactored_list_sig = atom_changes.get("list_signature", "list(self, query_payload: Optional[dict] = None) -> List[dict]")
    atom_list_return_type = "List of Atom details as dictionaries." 
    
    new_atom_methods_details = atom_changes.get("new_methods", [])
    
    # --- 1. Update docs/resources.md ---
    if "docs/resources.md" in new_contents:
        content = new_contents["docs/resources.md"]
        
        list_pattern_str = r"(## Atom Resource\s*\n(?:.*\n)*?### List Atoms\s*\n\n(?:.*?\n)*?)(?:`client\.atoms\.list\(\)`|`atoms = client\.atoms\.list\(\)`|```python\n# List all atoms\natoms = client\.atoms\.list\(\)\n```)"
        list_pattern = re.compile(list_pattern_str, re.MULTILINE)
        
        # Corrected f-string for query example by escaping curly braces for the dict literal
        updated_list_text_resources = (
            f"### List Atoms\n\n"
            f"Lists Atoms. This method can perform a simple GET request to list all atoms or a POST-based query if a `query_payload` is provided to filter results.\n\n"
            f"**Signature:**\n"
            f"```python\n{atom_refactored_list_sig}\n```\n\n"
            f"**Parameters:**\n"
            f"- `query_payload` (Optional[dict]): A dictionary representing the query filter for a POST request to `/Atom/query`. If `None` or omitted, a `GET /Atom` request is made.\n\n"
            f"**Returns:**\n"
            f"- {atom_list_return_type}\n\n"
            f"**Behavior:**\n"
            f"- If `query_payload` is `None`: Makes a `GET /Atom` request.\n"
            f"- If `query_payload` is provided: Makes a `POST /Atom/query` request with the payload.\n\n"
            f"**Example:**\n"
            f"```python\n# Get all atoms\nall_atoms = client.atoms.list()\n\n# Query for specific atoms (example payload structure)\n"
            f"query = {{'QueryFilter': {{'expression': {{'operator': 'and', 'nestedExpression': [\n"  # Escaped {
            f"    {{'argument': ['MyAtomName'], 'operator': 'EQUALS', 'property': 'name'}}\n" # Escaped {
            f"]}}}}}}\n" # Escaped {
            f"filtered_atoms = client.atoms.list(query_payload=query)\n```\n"
        )
        
        content, num_replacements = list_pattern.sub(lambda m: m.group(1) + updated_list_text_resources, content, count=1)

        if num_replacements == 0:
            atom_resource_pattern = re.compile(r"(## Atom Resource\s*\n)", re.MULTILINE)
            # Ensure replacement text is properly formatted if prepending
            replacement_for_atom_section = updated_list_text_resources
            if not updated_list_text_resources.startswith("\n###"): # ensure it starts as a subsection
                 replacement_for_atom_section = "\n" + updated_list_text_resources

            content, num_atom_sec_repl = atom_resource_pattern.subn(r"\1" + replacement_for_atom_section, content, count=1)
            if num_atom_sec_repl == 0:
                 print("Warning (docs/resources.md): Could not find 'List Atoms' or 'Atom Resource' section. Appending Atom.list documentation.", file=sys.stderr)
                 content += "\n## Atom Resource\n" + updated_list_text_resources
        
        new_methods_docs_resources = ""
        for method_info in new_atom_methods_details:
            new_methods_docs_resources += (
                f"\n### {method_info['name'].replace('_', ' ').title()}\n\n"
                f"{method_info.get('description', 'Method description placeholder.')}\n\n"
                f"**Signature:**\n```python\n{method_info['signature']}\n```\n"
            )
        
        if new_atom_methods_details:
            # Try to append new methods after the (potentially refactored) list method or at the end of Atom section
            # This assumes 'list' is the last documented method if no other specific anchor is found
            processed_list_pattern = re.compile(re.escape(updated_list_text_resources), re.MULTILINE)
            match_processed_list = processed_list_pattern.search(content)
            if match_processed_list:
                insert_point = match_processed_list.end()
                content = content[:insert_point] + new_methods_docs_resources + content[insert_point:]
            else: # Fallback: append to end of Atom section or file
                atom_section_end_pattern = re.compile(r"(## Atom Resource\s*\n(?:.*?\n)*?)(?:##|\Z)", re.MULTILINE | re.DOTALL)
                content, num_replacements_append = atom_section_end_pattern.subn(r"\1" + new_methods_docs_resources.strip() + "\n", content, count=1)
                if num_replacements_append == 0:
                    print("Warning (docs/resources.md): Could not find end of 'Atom Resource' section. Appending new Atom methods to end of file.", file=sys.stderr)
                    content += new_methods_docs_resources
        
        new_contents["docs/resources.md"] = content

    # --- 2. Update docs/classes.md ---
    if "docs/classes.md" in new_contents:
        content = new_contents["docs/classes.md"]
        class_atoms_match = re.search(r"(### Atoms\s*\n\n```python\nclass Atoms:\n)", content)
        if class_atoms_match:
            start_class_def_marker = class_atoms_match.group(1)
            start_class_def_offset = content.find(start_class_def_marker) + len(start_class_def_marker)
            
            end_class_def_match = re.search(r"\n```", content[start_class_def_offset:])
            if end_class_def_match:
                class_def_block_end_offset = start_class_def_offset + end_class_def_match.start()
                class_block_content = content[start_class_def_offset:class_def_block_end_offset]
                
                updated_class_block = re.sub(
                    r"def list\(self\)", atom_refactored_list_sig, class_block_content, count=1)
                
                new_method_sigs_text = ""
                existing_methods_in_block = set(re.findall(r"def (\w+)\(", updated_class_block))
                for method_info in new_atom_methods_details:
                    if method_info['name'] not in existing_methods_in_block:
                        new_method_sigs_text += f"    {method_info['signature']}\n"
                
                updated_class_block = updated_class_block.rstrip() + "\n" + new_method_sigs_text.rstrip()
                content = content[:start_class_def_offset] + updated_class_block + "\n" + content[class_def_block_end_offset:] # Added newline before end ```
            else:
                print("Warning (docs/classes.md): Could not find end of Atoms class code block.", file=sys.stderr)
        else:
            print("Warning (docs/classes.md): Could not find '### Atoms' class definition.", file=sys.stderr)
        new_contents["docs/classes.md"] = content
        
    # --- 3. Update docs/examples.md & docs/quickstart.md ---
    for doc_path in ["docs/examples.md", "docs/quickstart.md"]:
        if doc_path in new_contents:
            content = new_contents[doc_path]
            atom_example_pattern = re.compile(r"((?:# List atoms|### Atom Management)\s*\n(?:.*?\n)*?)(atoms = client\.atoms\.list\(\))", re.MULTILINE)
            
            # Corrected f-string for query example
            updated_atom_list_example = (
                r"\1" 
                r"# Get all atoms (uses GET /Atom)\n"
                r"all_atoms = client.atoms.list()\n\n"
                r"# Example: Query for specific atoms (uses POST /Atom/query)\n"
                r"# The exact query_payload structure depends on API capabilities.\n"
                r"query_payload_example = {{'QueryFilter': {{'expression': {{'operator': 'and', 'nestedExpression': [\n" # Escaped {{ and }}
                r"    {{'argument': ['MyAtomName'], 'operator': 'EQUALS', 'property': 'name'}}\n"
                r"]}}}}}}\n"
                r"filtered_atoms = client.atoms.list(query_payload=query_payload_example)\n"
            )
            content, num_repl = atom_example_pattern.subn(updated_atom_list_example, content, count=1)
            if num_repl == 0:
                 print(f"Warning ({doc_path}): Could not find typical 'client.atoms.list()' example to update.", file=sys.stderr)

            new_method_example_placeholder = "\n\n"
            new_method_example_placeholder += "```python\n# Example usage for new Atom methods:\n"
            for method_info in new_atom_methods_details:
                 params_info = parse_signature(method_info['signature'])['params']
                 param_names = [p['name'] for p in params_info if p['name'] != 'self']
                 dummy_args_list = []
                 if "atomid_val" in param_names: dummy_args_list.append('atomid_val="your_atom_id"')
                 if "payload" in param_names: dummy_args_list.append('payload={"key": "value"}') 
                 if "query_payload" in param_names: dummy_args_list.append('query_payload={"filter": {"example_field": "example_value"}}') # Escaped { }
                 
                 new_method_example_placeholder += f"# result = client.atoms.{method_info['name']}({', '.join(dummy_args_list)})\n"
                 new_method_example_placeholder += f"# print(result)\n"
            new_method_example_placeholder += "```\n"

            atom_mgmt_section_pattern_str = r"((?:### Atom Management|## Advanced Examples)\s*\n)" # Look for these headers
            atom_mgmt_section_match = re.search(atom_mgmt_section_pattern_str, content, re.MULTILINE)

            if atom_mgmt_section_match and new_atom_methods_details:
                # Try to insert before the next section or at the end of current examples for Atom
                insert_pos = -1
                # Find where the Atom examples end (e.g., before next ### or ##, or end of file)
                atom_examples_end_match = re.search(r"(?:### Atom Management\s*(?:\n```python(?:.|\n)*?```\s*)*)(?=\n##|\n###|\Z)", content, re.MULTILINE)
                if atom_examples_end_match:
                    insert_pos = atom_examples_end_match.end()
                
                if insert_pos != -1:
                     content = content[:insert_pos].rstrip() + new_method_example_placeholder + content[insert_pos:]
                else: # Fallback if specific Atom examples section not clearly delineated
                    content += "\n### New Atom Method Examples\n" + new_method_example_placeholder
            elif new_atom_methods_details: # If Atom Management section not found, append
                content += "\n### New Atom Method Examples\n" + new_method_example_placeholder
            
            new_contents[doc_path] = content
            
    return new_contents

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print(json.dumps({"error": "Usage: python update_atom_docs.py <doc_update_plan_json_str> <current_doc_contents_json_str> <atom_sdk_changes_json_str>"}), file=sys.stderr)
        sys.exit(1)

    doc_update_plan_arg = sys.argv[1]
    current_doc_contents_arg = sys.argv[2]
    atom_sdk_changes_arg = sys.argv[3]

    try:
        current_doc_contents_dict = json.loads(current_doc_contents_arg)
    except json.JSONDecodeError as e:
        print(json.dumps({"error": f"JSON decoding error for current_doc_contents: {e}"}), file=sys.stderr)
        sys.exit(1)
        
    updated_docs_dict = update_atom_documentation(doc_update_plan_arg, current_doc_contents_dict, atom_sdk_changes_arg)
    
    print(json.dumps(updated_docs_dict, indent=2))
