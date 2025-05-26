import json
import sys
import re

def parse_signature_simple(signature_str: str):
    """Parses a simple method signature string to get name, params list, and return type."""
    match = re.match(r"(\w+)\(([^)]*)\)\s*(?:->\s*(.+))?", signature_str)
    if not match:
        return {"name": signature_str, "params_str": "", "return_type": "Unknown"} # Fallback
    name, params_str, return_type = match.groups()
    return {"name": name, "params_str": params_str, "return_type": return_type if return_type else "Unknown"}

def generate_param_description(param_name_type: str) -> str:
    name, p_type = param_name_type.split(':')
    name = name.strip()
    p_type = p_type.strip()
    # Basic descriptions, can be enhanced
    if "id" in name.lower():
        return f"- `{name}` ({p_type}): The ID of the resource."
    if "payload" in name.lower():
        return f"- `{name}` ({p_type}): The data payload for the request."
    return f"- `{name}` ({p_type}): (No description available)"


def update_account_documentation(
    current_doc_contents: dict, 
    account_sdk_summary_str: str
) -> dict:
    try:
        account_summary = json.loads(account_sdk_summary_str)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON input for account_sdk_summary: {e}", file=sys.stderr)
        return current_doc_contents # Return original if input is broken

    new_contents = current_doc_contents.copy()
    
    class_name = account_summary.get("class_name", "Accounts")
    client_attr = account_summary.get("client_attribute", "accounts")
    methods = account_summary.get("methods", [])

    # --- 1. Update docs/resources.md ---
    if "docs/resources.md" in new_contents:
        content = new_contents["docs/resources.md"]
        account_section_title = f"\n\n## {class_name.replace('s','')} Resource\n" # e.g. ## Account Resource
        
        account_docs = account_section_title
        for method_info in methods:
            sig_details = parse_signature_simple(method_info["signature"])
            method_name_display = sig_details["name"].replace('_', ' ').title()
            
            account_docs += f"\n### {method_name_display}\n\n"
            account_docs += f"{method_info.get('description', 'Description placeholder.')}\n\n"
            account_docs += f"**Signature:**\n```python\n{method_info['signature']}\n```\n\n"
            
            if sig_details["params_str"] and sig_details["params_str"] != "self":
                account_docs += f"**Parameters:**\n"
                params = [p.strip() for p in sig_details["params_str"].split(',') if p.strip() != "self"]
                for p_def in params:
                    account_docs += f"{generate_param_description(p_def)}\n"
                account_docs += "\n"

            account_docs += f"**Returns:**\n- {sig_details['return_type']}\n"

        # Try to insert before "Next Steps" or append
        next_steps_pattern = re.compile(r"\n## Next Steps", re.MULTILINE)
        match = next_steps_pattern.search(content)
        if match:
            content = content[:match.start()] + account_docs + content[match.start():]
        else:
            content += account_docs # Append if "Next Steps" not found
        new_contents["docs/resources.md"] = content

    # --- 2. Update docs/classes.md ---
    if "docs/classes.md" in new_contents:
        content = new_contents["docs/classes.md"]
        accounts_class_doc = f"\n### {class_name}\nManages {class_name.lower()}.\n\n```python\nclass {class_name}:\n"
        for method_info in methods:
            accounts_class_doc += f"    {method_info['signature']}\n"
        accounts_class_doc += "```\n"
        
        resource_classes_pattern = re.compile(r"(## Resource Classes\s*\n)", re.MULTILINE)
        match = resource_classes_pattern.search(content)
        if match:
            # Insert after "## Resource Classes" and before the next class, or just after the header
            # Find where the list of classes starts and append there
            insertion_point = match.end()
            # A simple way is to append it right after the "## Resource Classes" header,
            # or find the last "### ClassName" and append after its code block.
            # For simplicity, appending after the header.
            content = content[:insertion_point] + accounts_class_doc + content[insertion_point:]
        else:
            content += "\n## Resource Classes\n" + accounts_class_doc # Append if section not found
        new_contents["docs/classes.md"] = content

    # --- 3. Update docs/client.md ---
    if "docs/client.md" in new_contents:
        content = new_contents["docs/client.md"]
        available_resources_pattern = re.compile(r"(## Available Resources\s*\n(?:- `\w+`: .*\n)*)", re.MULTILINE)
        new_resource_line = f"- `{client_attr}`: Manage Boomi accounts.\n"
        
        match = available_resources_pattern.search(content)
        if match:
            content = match.group(1) + new_resource_line + content[match.end():]
        else: # Fallback if pattern fails
            content += "\n## Available Resources\n" + new_resource_line
        new_contents["docs/client.md"] = content
        
    # --- 4. Update docs/examples.md & docs/quickstart.md ---
    for doc_path in ["docs/examples.md", "docs/quickstart.md"]:
        if doc_path in new_contents:
            content = new_contents[doc_path]
            accounts_examples_section = f"\n### Working with {class_name}\n\n```python\n"
            accounts_examples_section += f"# Assuming 'client' is an initialized Boomi client instance\n\n"
            for method_info in methods:
                method_name = parse_signature_simple(method_info["signature"])["name"]
                example_call = f"client.{client_attr}.{method_name}("
                if "account_id" in method_info["signature"]: # Specific for get_account_details
                    example_call += 'account_id="your-account-id-example"'
                elif "payload" in method_info["signature"]: # Specific for get_account_list with payload
                    example_call += 'query_payload={"filter": "example_filter"}' # Example payload
                example_call += ")"
                accounts_examples_section += f"# Example for {method_name}\n"
                accounts_examples_section += f"try:\n"
                accounts_examples_section += f"    result = {example_call}\n"
                accounts_examples_section += f"    print(result)\n"
                accounts_examples_section += f"except Exception as e:\n"
                accounts_examples_section += f"    print(f'Error calling {method_name}: {{e}}')\n\n" # Escaped {e}
            accounts_examples_section += "```\n"

            # Try to insert after "Common Operations" or "Advanced Examples" or append
            common_ops_pattern = re.compile(r"(## Common Operations\s*\n|## Advanced Examples\s*\n)", re.MULTILINE)
            match = common_ops_pattern.search(content)
            if match:
                # Find end of that section to append new examples logically
                next_section_start = re.search(r"\n## |\n### |\Z", content[match.end():])
                if next_section_start:
                    insertion_point = match.end() + next_section_start.start()
                    content = content[:insertion_point] + accounts_examples_section + content[insertion_point:]
                else:
                    content += accounts_examples_section
            else:
                content += "\n## Account Examples\n" + accounts_examples_section
            new_contents[doc_path] = content

    # --- 5. Update docs/index.md ---
    if "docs/index.md" in new_contents:
        content = new_contents["docs/index.md"]
        features_pattern = re.compile(r"(## Features\s*\n(?:- .*\n)*)", re.MULTILINE)
        new_feature_line = f"- Account Management: Access account details and lists.\n"
        match = features_pattern.search(content)
        if match:
            content = match.group(1) + new_feature_line + content[match.end():]
        else: # Fallback if no features list found
            # Could also try to add to Table of Contents if "Accounts" is a new major resource
            if "Table of Contents" in content: # Add to ToC if possible
                 content = content.replace("- [Resources](resources.md)", "- [Resources](resources.md)\n  - Accounts") # very basic
            else: # Append
                 content += "\n## Features\n" + new_feature_line
        new_contents["docs/index.md"] = content
            
    return new_contents

if __name__ == '__main__':
    if len(sys.argv) != 3: # Expects current_doc_contents_json_str and account_sdk_summary_json_str
        print(json.dumps({"error": "Usage: python update_account_docs.py <current_doc_contents_json_str> <account_sdk_summary_json_str>"}), file=sys.stderr)
        sys.exit(1)

    current_doc_contents_arg = sys.argv[1]
    account_sdk_summary_arg = sys.argv[2]
    # doc_update_plan_arg is not used by this script version, focused on specific Account changes

    try:
        current_doc_contents_dict = json.loads(current_doc_contents_arg)
    except json.JSONDecodeError as e:
        print(json.dumps({"error": f"JSON decoding error for current_doc_contents: {e}"}), file=sys.stderr)
        sys.exit(1)
        
    updated_docs_dict = update_account_documentation(current_doc_contents_dict, account_sdk_summary_arg)
    
    print(json.dumps(updated_docs_dict, indent=2))
