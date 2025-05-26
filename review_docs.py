import json
import sys
import re

def check_markdown_syntax(content: str) -> list:
    issues = []
    # Unmatched brackets/parentheses (simple non-nested check)
    if content.count('[') != content.count(']'):
        issues.append("Potential unmatched square brackets.")
    if content.count('(') != content.count(')'):
        # This is too broad, as () are used in method signatures in text.
        # A more specific check for markdown links:
        for match in re.finditer(r"\[([^]]+)\]\(([^)]+)\s+\)", content): # Space before closing parenthesis in link
            issues.append(f"Malformed link with trailing space: '{match.group(0)}'")
    
    # Unmatched backticks (check for odd numbers of single and triple backticks)
    if (len(re.findall(r"```", content))) % 2 != 0:
        issues.append("Potential unmatched triple backticks (```).")
    
    # Check for odd number of single backticks, but be careful of code blocks
    # This is tricky because single backticks can be valid within triple backtick code blocks.
    # A simple line-by-line check for non-code-block lines:
    lines = content.split('\\n')
    in_code_block = False
    for i, line in enumerate(lines):
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            continue
        if not in_code_block:
            if (line.count('`') % 2) != 0:
                issues.append(f"Potential unmatched single backtick on line {i+1}: '{line[:50]}...'")
                break # Report first occurrence per file to avoid flood

    return issues

def check_placeholders(content: str) -> list:
    issues = []
    placeholders = ["TODO", "NEEDS UPDATE", "XXX", "placeholder"] # Case-insensitive search
    for p in placeholders:
        if re.search(p, content, re.IGNORECASE):
            issues.append(f"Found potential placeholder text: '{p}'.")
    return issues

def check_consistency(file_path: str, content: str, sdk_changes: dict) -> list:
    inconsistencies = []
    # SDK Change Lookups (from the hardcoded summary in main script)
    new_atom_methods_names = [m['name'] for m in sdk_changes.get("Atom", {}).get("new_methods", [])]
    atom_list_refactored = sdk_changes.get("Atom", {}).get("refactored_list", False)
    account_is_new = sdk_changes.get("Account", {}).get("is_new", False)
    account_method_names = [m['name'] for m in sdk_changes.get("Account", {}).get("methods", [])]
    component_model_fields = sdk_changes.get("Component_Model", {}).get("added_fields", []) # ["description: str", "version: int"]
    component_get_refactored = sdk_changes.get("Component_Resource", {}).get("refactored_get", False)
    client_has_accounts = sdk_changes.get("Client", {}).get("new_accounts_attr", False)

    if file_path == "docs/resources.md":
        if atom_list_refactored and not ("query_payload" in content and "/Atom/query" in content and "## Atom Resource" in content and "### List Atoms" in content):
            inconsistencies.append("Atoms.list() refactor (dual GET/POST) may not be fully documented in Atom Resource section.")
        for method_name in new_atom_methods_names:
            if not (f"### {method_name.replace('_', ' ').title()}" in content and method_name in content and "## Atom Resource" in content):
                inconsistencies.append(f"New Atom method '{method_name}' may be missing from Atom Resource section.")
        if account_is_new and not ("## Account Resource" in content and all(m_name in content for m_name in account_method_names)):
            inconsistencies.append("New Account resource or its methods may be missing/incomplete.")
        if component_get_refactored and not ("Component Resource" in content and "Get Component" in content and ( "JSON" in content or ".json()" in content)):
            inconsistencies.append("Components.get() refactor (JSON response) may not be documented in Component Resource section.")

    elif file_path == "docs/classes.md":
        if atom_list_refactored and not ("class Atoms:" in content and "query_payload: Optional[dict]" in content):
            inconsistencies.append("Atoms.list() signature update (Optional[dict]) may be missing in Atoms class definition.")
        for method_name in new_atom_methods_names:
            if not (f"class Atoms:" in content and method_name in content):
                 inconsistencies.append(f"New Atom method '{method_name}' signature may be missing from Atoms class definition.")
        if account_is_new and not ("class Accounts:" in content and all(m_name in content for m_name in account_method_names)):
            inconsistencies.append("New Accounts class or its method signatures may be missing.")
        if component_model_fields:
            for field_def_str in component_model_fields: # e.g. "description: str"
                field_name = field_def_str.split(':')[0].strip()
                if not ("class Component(BaseModel):" in content and field_name in content):
                    inconsistencies.append(f"Component model update (field '{field_name}') may be missing from class definition.")
    
    elif file_path == "docs/client.md":
        if client_has_accounts and not ("accounts: Manage Boomi accounts" in content or "client.accounts" in content):
            inconsistencies.append("New 'accounts' client attribute may be missing from 'Available Resources' list.")

    elif file_path in ["docs/examples.md", "docs/quickstart.md"]:
        if atom_list_refactored and not ("client.atoms.list(query_payload=" in content):
            inconsistencies.append(f"Example for Atoms.list() with query_payload may be missing in {file_path}.")
        if component_get_refactored and not ("component_details.description" in content or "component_details.version" in content or "JSON response" in content and "client.components.get" in content):
             inconsistencies.append(f"Example for Components.get() reflecting JSON and new model fields may be outdated/missing in {file_path}.")
        if account_is_new and not ("client.accounts.get" in content): # Basic check for any account example
            inconsistencies.append(f"Examples for the new Accounts resource may be missing in {file_path}.")

    elif file_path == "docs/index.md":
        if account_is_new and not ("Account Management" in content or "Accounts" in content): # Check if "Accounts" or related feature mentioned
            inconsistencies.append("Mention of new Account Management features might be missing from index.md.")
            
    return inconsistencies

def attempt_autofix(content: str) -> (str, list):
    fixes_applied = []
    original_content = content
    
    # Fix malformed links like [text](url ) -> [text](url)
    # Using a loop to replace all occurrences, as sub might only do one without global flag or careful regex
    new_content = content
    while True:
        corrected = re.sub(r"(\[[^]]+\]\([^)]+)\s+\)", r"\1)", new_content)
        if corrected == new_content: # No more changes
            break
        new_content = corrected
        fixes_applied.append("Corrected malformed link with trailing space.")
        
    # Simple unmatched backtick: if a line has one backtick, assume it's a typo and remove.
    # This is very heuristic and could be wrong. A better autofix might try to pair it.
    # For now, this is too risky to implement broadly.
    # Example (risky):
    # lines = new_content.split('\\n')
    # for i, line in enumerate(lines):
    #     if line.count('`') == 1 and "```" not in line:
    #         lines[i] = line.replace('`', '')
    #         fixes_applied.append(f"Removed a lone backtick on line {i+1} (heuristic).")
    # new_content = '\\n'.join(lines)

    if not fixes_applied:
        return original_content, [] # Return original if no changes
    return new_content, list(set(fixes_applied)) # Return unique list of fix descriptions


def review_documentation_files(doc_files_content_dict: dict, sdk_changes_summary_data: dict) -> str:
    report = {
        "files_reviewed": [],
        "overall_summary": "",
        "temp_file_cleanup_assumption": "Cleanup of temporary files by previous worker agents is assumed complete based on their reports."
    }

    all_issues_found = False
    all_autofixes_applied = []

    for file_path, original_content in doc_files_content_dict.items():
        file_report = {
            "file_path": file_path,
            "syntax_issues": [],
            "placeholder_issues": [],
            "consistency_issues": [],
            "autofixes_applied": [],
            "status": "No major issues found.",
            "updated_content": None # Will hold content if autofixed
        }

        syntax_issues = check_markdown_syntax(original_content)
        if syntax_issues:
            file_report["syntax_issues"] = syntax_issues
            all_issues_found = True
        
        placeholder_issues = check_placeholders(original_content)
        if placeholder_issues:
            file_report["placeholder_issues"] = placeholder_issues
            all_issues_found = True

        consistency_issues = check_consistency(file_path, original_content, sdk_changes_summary_data)
        if consistency_issues:
            file_report["consistency_issues"] = consistency_issues
            all_issues_found = True
        
        # Attempt autofixes
        content_after_fixes, fixes_applied_desc = attempt_autofix(original_content)
        if fixes_applied_desc:
            file_report["autofixes_applied"] = fixes_applied_desc
            file_report["updated_content"] = content_after_fixes 
            all_autofixes_applied.extend(fixes_applied_desc)
            all_issues_found = True # If we autofixed, it implies an issue was found

        if syntax_issues or placeholder_issues or consistency_issues or fixes_applied_desc:
            file_report["status"] = "Issues found."
            if fixes_applied_desc and not (syntax_issues or placeholder_issues or consistency_issues):
                 # If only autofixes were applied for very minor things the other checks didn't catch as "issues"
                 file_report["status"] = "Minor issues autofixed."


        report["files_reviewed"].append(file_report)

    if not all_issues_found and not all_autofixes_applied:
        report["overall_summary"] = "All reviewed documentation files appear consistent with recent SDK changes and have no major syntax/placeholder issues."
    elif all_autofixes_applied and not all_issues_found: # Only autofixes, no other outstanding issues
        report["overall_summary"] = "Minor issues were autofixed in some files. Files appear consistent with recent SDK changes."
    else:
        report["overall_summary"] = "Issues found or inconsistencies noted in some documentation files. Review details per file. Some minor issues may have been autofixed."
            
    return json.dumps(report, indent=2)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(json.dumps({"error": "Usage: python review_docs.py <doc_files_content_json_string>"}), file=sys.stderr)
        sys.exit(1)

    doc_files_content_json_arg = sys.argv[1]
    
    try:
        doc_files_content_dict_arg = json.loads(doc_files_content_json_arg)
    except json.JSONDecodeError as e:
        print(json.dumps({"error": f"JSON decoding error for doc_files_content_json_string: {e}"}), file=sys.stderr)
        sys.exit(1)

    # SDK Changes Summary (hardcoded based on problem description for this script's context)
    sdk_changes_summary = {
        "Atom": {
            "new_methods": [ # List of method_info dicts as used in update_atom_docs.py
                {"name": "post_atom_disable", "signature": "post_atom_disable(self, atomid_val: str, payload: dict) -> dict"},
                {"name": "post_atom_query", "signature": "post_atom_query(self, query_payload: dict) -> List[dict]"}
            ],
            "refactored_list": True
        },
        "Account": {
            "is_new": True,
            "methods": [ # List of method_info dicts
                 {"name": "get_account_details", "signature": "get_account_details(self, account_id: str) -> dict"},
                 {"name": "get_account_list", "signature": "get_account_list(self, query_payload: dict = None) -> dict"}
            ]
        },
        "Component_Model": {
            "added_fields": ["description: str", "version: int"] # Format: "name: type"
        },
        "Component_Resource": {
            "refactored_get": True
        },
        "Client": {
            "new_accounts_attr": True
        }
    }
    
    report_json = review_documentation_files(doc_files_content_dict_arg, sdk_changes_summary)
    print(report_json)
