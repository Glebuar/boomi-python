import json
import sys
import ast
import re
import astor # Ensure astor is available

def parse_method_signature(signature_str: str):
    """Parses a simple method signature string to get name and params."""
    match = re.match(r"(\w+)\(([^)]*)\)", signature_str)
    if not match:
        return {"name": "unknown", "params": []}
    name, params_str = match.groups()
    params = [p.split(':')[0].strip() for p in params_str.split(',') if p.strip()]
    return {"name": name, "params": params}

def analyze_and_refactor_atoms(
    discrepancy_report_json_str: str,
    openapi_spec_json_str: str,
    current_atoms_py_content: str,
    atom_schema_json_str: str # For context, not direct code modification
):
    summary_log = []
    changes_made = False

    try:
        discrepancy_report = json.loads(discrepancy_report_json_str)
        openapi_spec = json.loads(openapi_spec_json_str)
        # atom_schema = json.loads(atom_schema_json_str) # Parsed if needed for deep inspection
    except json.JSONDecodeError as e:
        summary_log.append(f"Error decoding JSON input: {e}")
        return current_atoms_py_content, "\n".join(summary_log)

    # --- Model Review ---
    summary_log.append("Model Review for Atom:")
    summary_log.append(f"- OpenAPI schema for Atom is defined in 'openapi/components/schemas/Atom.json'.")
    # Check for boomi/models/atom.py would be `ls()` call by agent, not here.
    # Based on problem description, it doesn't exist.
    summary_log.append("- No dedicated SDK model file 'boomi/models/atom.py' is assumed to exist.")
    summary_log.append("- Pre-existing methods in atoms.py are assumed to return raw dicts from API responses.")
    summary_log.append("- Conclusion: No model code changes required for Atom in this step.")

    # --- Method Refactoring (Focus on 'list') ---
    # Identify if 'POST /Atom/query' is a preferred way to list/query Atoms from OpenAPI spec
    openapi_atom_paths = openapi_spec.get("paths", {})
    supports_post_query = "/Atom/query" in openapi_atom_paths and "post" in openapi_atom_paths["/Atom/query"]
    
    summary_log.append("\nMethod Refactoring for atoms.py:")

    # Parse current atoms.py content
    tree = ast.parse(current_atoms_py_content)
    original_method_found = False

    for class_node in tree.body:
        if not (isinstance(class_node, ast.ClassDef) and class_node.name == "Atoms"):
            continue

        for i, method_node in enumerate(class_node.body):
            if not (isinstance(method_node, ast.FunctionDef) and method_node.name == "list"):
                continue
            
            original_method_found = True
            summary_log.append(f"- Found pre-existing method: list()")

            # Check its current implementation (very basic check based on common initial form)
            # A more robust check would involve inspecting method_node.body AST.
            # For this task, we'll assume if supports_post_query is true, 'list' needs refactoring.
            
            current_list_is_simple_get = True # Assume initially
            if len(method_node.args.args) > 1: # Has more than 'self'
                current_list_is_simple_get = False
            # Could also check body: `self._http.get("/Atom")` vs `self._http.post("/Atom/query")`
            
            if supports_post_query:
                summary_log.append(f"- OpenAPI spec supports POST /Atom/query for enhanced listing.")
                if not current_list_is_simple_get and any(arg.arg == "query_payload" for arg in method_node.args.args):
                     summary_log.append(f"- Method 'list' already seems to support querying. No changes made to its structure based on this check.")
                     continue # Already supports query_payload

                summary_log.append(f"- Refactoring 'list' method to support optional query_payload via POST /Atom/query.")
                changes_made = True

                # New signature: list(self, query_payload: Optional[dict] = None) -> List[dict]
                # AST for query_payload: Optional[dict] = None
                query_payload_arg = ast.arg(
                    arg='query_payload',
                    annotation=ast.Subscript(
                        value=ast.Name(id='Optional', ctx=ast.Load()),
                        slice=ast.Name(id='dict', ctx=ast.Load()),
                        ctx=ast.Load()
                    )
                )
                # Default value for query_payload (None)
                method_node.args.defaults = [ast.Constant(value=None)]
                # Update args: keep 'self', add 'query_payload'
                # Ensure 'self' is first if it exists, or handle if not (though it should for a method)
                if method_node.args.args and method_node.args.args[0].arg == 'self':
                    method_node.args.args = [method_node.args.args[0], query_payload_arg]
                else: # Should not happen for typical class methods
                    method_node.args.args = [query_payload_arg]


                # New return type: List[dict]
                method_node.returns = ast.Subscript(
                    value=ast.Name(id='List', ctx=ast.Load()),
                    slice=ast.Name(id='dict', ctx=ast.Load()),
                    ctx=ast.Load()
                )

                # New body for list method:
                # if query_payload:
                #   return self._http.post("/Atom/query", json=query_payload).json()
                # else:
                #   return self._http.get("/Atom").json()
                new_body = [
                    ast.If(
                        test=ast.Name(id='query_payload', ctx=ast.Load()),
                        body=[
                            ast.Return(value=ast.Call(
                                func=ast.Attribute(
                                    value=ast.Call(
                                        func=ast.Attribute(
                                            value=ast.Attribute(value=ast.Name(id='self', ctx=ast.Load()), attr='_http', ctx=ast.Load()),
                                            attr='post', ctx=ast.Load()),
                                        args=[ast.Constant(value='/Atom/query')],
                                        keywords=[ast.keyword(arg='json', value=ast.Name(id='query_payload', ctx=ast.Load()))]),
                                    attr='json', ctx=ast.Load()),
                                args=[], keywords=[]
                            ))
                        ],
                        orelse=[
                            ast.Return(value=ast.Call(
                                func=ast.Attribute(
                                    value=ast.Call(
                                        func=ast.Attribute(
                                            value=ast.Attribute(value=ast.Name(id='self', ctx=ast.Load()), attr='_http', ctx=ast.Load()),
                                            attr='get', ctx=ast.Load()),
                                        args=[ast.Constant(value='/Atom')], keywords=[]),
                                    attr='json', ctx=ast.Load()),
                                args=[], keywords=[]
                            ))
                        ]
                    )
                ]
                method_node.body = new_body
                
                # Ensure typing.Optional and typing.List are imported if not already
                # This part is tricky with AST alone; usually handled by linters/organizers.
                # For this script, we'll assume they are imported or will be added manually if needed.
                # A more advanced script would check and add these imports to tree.body.
                # For now, we'll add a note about it.
                summary_log.append("- Note: Ensure 'Optional' and 'List' from 'typing' are imported in atoms.py.")

            else: # OpenAPI does not support POST /Atom/query
                summary_log.append(f"- Method 'list' uses GET /Atom. OpenAPI spec does not indicate POST /Atom/query. No changes made to 'list'.")
            
            break # Processed 'list', move out of methods loop for this class

    if not original_method_found:
        summary_log.append("- No pre-existing 'list' method found in Atoms class. No refactoring applied.")

    if changes_made:
        # Add imports for Optional and List if not present
        # This is a simplified check and addition
        needed_typing_imports = {"Optional", "List"}
        typing_import_node = None
        for node in tree.body:
            if isinstance(node, ast.ImportFrom) and node.module == "typing":
                typing_import_node = node
                for alias in node.names:
                    if alias.name in needed_typing_imports:
                        needed_typing_imports.remove(alias.name)
                break
        
        if typing_import_node and needed_typing_imports: # Import from typing exists, add missing names
             for name_to_add in needed_typing_imports:
                 typing_import_node.names.append(ast.alias(name=name_to_add, asname=None))
             typing_import_node.names.sort(key=lambda x: x.name) # Keep it sorted
        elif not typing_import_node and needed_typing_imports: # No import from typing yet
            new_typing_import = ast.ImportFrom(
                module="typing",
                names=[ast.alias(name=n, asname=None) for n in sorted(list(needed_typing_imports))],
                level=0 # Absolute import
            )
            # Insert after other imports or at the beginning
            insert_idx = 0
            for i, node in enumerate(tree.body):
                if isinstance(node, (ast.Import, ast.ImportFrom)):
                    insert_idx = i + 1
                elif isinstance(node, ast.ClassDef): # Stop before class defs
                    break
            tree.body.insert(insert_idx, new_typing_import)


        return astor.to_source(tree), "\n".join(summary_log)
    else:
        summary_log.append("\nNo code changes were necessary for boomi/resources/atoms.py.")
        return current_atoms_py_content, "\n".join(summary_log)


if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Usage: python refactor_sdk_atoms.py <discrepancy_report_json> <openapi_spec_json> <atoms_py_content> <atom_schema_json>", file=sys.stderr)
        sys.exit(1)
        
    discrepancy_report_json_arg = sys.argv[1]
    openapi_spec_json_arg = sys.argv[2]
    atoms_py_content_arg = sys.argv[3]
    atom_schema_json_arg = sys.argv[4]
    
    updated_code, summary = analyze_and_refactor_atoms(
        discrepancy_report_json_arg,
        openapi_spec_json_arg,
        atoms_py_content_arg,
        atom_schema_json_arg
    )
    
    print(updated_code)
    print("--- séparation ---", file=sys.stderr) # Separator for agent to distinguish code from summary
    print(summary, file=sys.stderr)
