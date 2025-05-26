import json
import sys
import re

def analyze_documentation(doc_files_content_dict: dict, sdk_changes: dict) -> str:
    report = {}

    # --- Define SDK Change Lookups ---
    new_atom_methods = sdk_changes.get("Atom", {}).get("new_methods", [])
    refactored_atom_list = sdk_changes.get("Atom", {}).get("refactored_list", False)
    
    new_account_resource = sdk_changes.get("Account", {}).get("is_new", False)
    new_account_methods = sdk_changes.get("Account", {}).get("methods", [])
    
    updated_component_model_fields = sdk_changes.get("Component_Model", {}).get("added_fields", [])
    refactored_components_get = sdk_changes.get("Component_Resource", {}).get("refactored_get", False)
    
    client_has_new_accounts_attr = sdk_changes.get("Client", {}).get("new_accounts_attr", False)

    # --- Analyze each documentation file ---
    for file_path, content in doc_files_content_dict.items():
        areas_to_update = []

        # --- docs/resources.md ---
        if file_path == "docs/resources.md":
            if "Atom Resource" in content or "## Atom Resource" in content:
                atom_changes = []
                atom_constructs = []
                if refactored_atom_list:
                    atom_changes.append("Update Atoms.list() signature (now takes optional query_payload: Optional[dict] = None) and describe its dual GET/POST behavior (uses POST /Atom/query with payload, else GET /Atom).")
                    atom_constructs.append("Atoms.list")
                if new_atom_methods:
                    atom_changes.append(f"Add documentation for new Atom methods: {', '.join(new_atom_methods)} (e.g., post_atom_disable, post_atom_query).")
                    atom_constructs.extend([f"Atoms.{m}" for m in new_atom_methods])
                
                if atom_changes:
                    areas_to_update.append({
                        "area_description": "Atom Resource Section",
                        "specific_changes_needed": " ".join(atom_changes),
                        "relevant_sdk_constructs": list(set(atom_constructs))
                    })

            if new_account_resource:
                areas_to_update.append({
                    "area_description": "Account Resource Section (New)",
                    "specific_changes_needed": f"Add complete documentation for the new Accounts resource, including its methods: {', '.join(new_account_methods)} (e.g., get_account_details, get_account_list). Detail parameters and return types.",
                    "relevant_sdk_constructs": ["Accounts"] + [f"Accounts.{m}" for m in new_account_methods]
                })
            
            if "Component Resource" in content or "## Component Resource" in content:
                comp_res_changes = []
                comp_res_constructs = []
                if refactored_components_get:
                    comp_res_changes.append("Update Components.get() description to reflect it now expects and processes a JSON response (using model_validate(r.json())) instead of XML.")
                    comp_res_constructs.append("Components.get")
                
                if comp_res_changes:
                    areas_to_update.append({
                        "area_description": "Component Resource Section",
                        "specific_changes_needed": " ".join(comp_res_changes),
                        "relevant_sdk_constructs": list(set(comp_res_constructs))
                    })
        
        elif file_path == "docs/classes.md":
            # Component Model
            if "## Model Classes" in content and "### Component" in content:
                model_changes = []
                model_constructs = []
                if updated_component_model_fields:
                    model_changes.append(f"Update attributes list for the Component model to include: {', '.join(updated_component_model_fields)} (e.g., description: str, version: int).")
                    model_constructs.append("Component") 
                
                if model_changes:
                     areas_to_update.append({
                        "area_description": "Component Model Documentation (under Model Classes)",
                        "specific_changes_needed": " ".join(model_changes),
                        "relevant_sdk_constructs": list(set(model_constructs))
                    })
            
            # Atom Resource Class (for list method update)
            if "### Atoms" in content:
                if refactored_atom_list:
                    areas_to_update.append({
                        "area_description": "Atoms Class Method List",
                        "specific_changes_needed": "Update signature of Atoms.list() to `list(self, query_payload: Optional[dict] = None)`. Add new methods if listed here: " + (", ".join(new_atom_methods) if new_atom_methods else "none") + ".",
                        "relevant_sdk_constructs": ["Atoms.list"] + ([f"Atoms.{m}" for m in new_atom_methods] if new_atom_methods else [])
                    })
            
            # Accounts Resource Class (New)
            if new_account_resource:
                 areas_to_update.append({
                        "area_description": "Accounts Class (New Resource)",
                        "specific_changes_needed": f"Add new section for Accounts class with its methods: {', '.join(new_account_methods)}.",
                        "relevant_sdk_constructs": ["Accounts"] + [f"Accounts.{m}" for m in new_account_methods]
                    })


        elif file_path == "docs/client.md":
            if client_has_new_accounts_attr and "Available Resources" in content:
                areas_to_update.append({
                    "area_description": "Client Available Resources Section",
                    "specific_changes_needed": "Add 'accounts: Accounts' to the list of available resources on the Boomi client instance.",
                    "relevant_sdk_constructs": ["Boomi.accounts"]
                })

        elif file_path in ["docs/examples.md", "docs/quickstart.md"]:
            review_points = []
            constructs_for_review = []
            if refactored_atom_list:
                review_points.append("Update examples using Atoms.list() to show new signature and dual behavior.")
                constructs_for_review.append("Atoms.list")
            if new_atom_methods:
                review_points.append(f"Consider adding examples for new Atom methods: {', '.join(new_atom_methods)}.")
                constructs_for_review.extend([f"Atoms.{m}" for m in new_atom_methods])
            if new_account_resource:
                review_points.append(f"Add examples for the new Accounts resource and its methods: {', '.join(new_account_methods)}.")
                constructs_for_review.append("Accounts")
            if refactored_components_get:
                review_points.append("Update examples using Components.get() to ensure they align with JSON response handling and updated Component model.")
                constructs_for_review.append("Components.get")
            
            if review_points:
                areas_to_update.append({
                    "area_description": "Code Examples and Quick Start Usage",
                    "specific_changes_needed": " ".join(review_points),
                    "relevant_sdk_constructs": list(set(constructs_for_review))
                })
        
        elif file_path in ["docs/index.md", "docs/installation.md", "docs/errors.md"]:
            if new_account_resource: # A new resource is a notable feature
                 areas_to_update.append({
                    "area_description": "General Site Content (e.g., Feature List, Overview)",
                    "specific_changes_needed": "Review for any indirect impacts from new 'Accounts' resource (e.g., update feature lists, table of contents if resources are listed).",
                    "relevant_sdk_constructs": ["Accounts"]
                })

        if areas_to_update:
            report[file_path] = areas_to_update
            
    return json.dumps(report, indent=2)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(json.dumps({"error": "Usage: python identify_doc_updates.py <doc_files_content_json_string>"}), file=sys.stderr)
        sys.exit(1)

    doc_files_content_json_arg = sys.argv[1] # This is now the JSON string itself
    
    try:
        doc_files_content_dict_arg = json.loads(doc_files_content_json_arg)
    except json.JSONDecodeError as e:
        print(json.dumps({"error": f"JSON decoding error for doc_files_content_json_string: {e}"}), file=sys.stderr)
        sys.exit(1)

    sdk_changes_summary_data = {
        "Atom": {
            "new_methods": ["post_atom_disable", "post_atom_query"],
            "refactored_list": True
        },
        "Account": {
            "is_new": True,
            "methods": ["get_account_details", "get_account_list"]
        },
        "Component_Model": {
            "added_fields": ["description", "version"]
        },
        "Component_Resource": {
            "refactored_get": True
        },
        "Client": {
            "new_accounts_attr": True
        }
    }
    
    report_json = analyze_documentation(doc_files_content_dict_arg, sdk_changes_summary_data)
    print(report_json)
