import json
import sys
import ast
import re
import astor # Ensure astor is available

def parse_signature(signature_str: str):
    """Parses an SDK method signature string."""
    match = re.match(r"(\w+)\(([^)]*)\)\s*->\s*(.+)", signature_str)
    if not match:
        # Try to handle cases where return type might be missing in the plan (though unlikely for this task)
        match_no_return = re.match(r"(\w+)\(([^)]*)\)", signature_str)
        if not match_no_return:
            raise ValueError(f"Invalid signature format: {signature_str}")
        name, params_str = match_no_return.groups()
        return_type = "Any" # Default if not specified
    else:
        name, params_str, return_type = match.groups()
    
    params = []
    if params_str:
        for p_match_str in params_str.split(','):
            p_match_str = p_match_str.strip()
            if not p_match_str: continue # Skip if empty string from splitting "()"
            param_name_type = p_match_str.split(':')
            param_name = param_name_type[0].strip()
            param_type = param_name_type[1].strip() if len(param_name_type) > 1 else "Any"
            params.append({"name": param_name, "type": param_type})
            
    return {"name": name, "params": params, "return_type": return_type}


def generate_method_ast(method_plan: dict) -> ast.FunctionDef:
    """Generates an AST FunctionDef node for a given SDK method plan."""
    sig_info = parse_signature(method_plan["sdk_method_signature"])
    method_name = sig_info["name"]
    
    ast_params_list = []
    for p_info in sig_info["params"]:
        if p_info["type"] != "Any":
            try:
                type_annotation_node = ast.parse(p_info["type"]).body[0].value
            except: 
                type_annotation_node = ast.Name(id=p_info["type"], ctx=ast.Load())
        else:
            type_annotation_node = None
        ast_params_list.append(ast.arg(arg=p_info["name"], annotation=type_annotation_node))

    args_node = ast.arguments(
        posonlyargs=[], args=ast_params_list, vararg=None, 
        kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]
    )
    
    api_path = method_plan["api_path"]
    path_params_in_signature = [p for p in sig_info["params"] if p["name"] != "self" and "_val" in p["name"].lower()] # e.g. accountid_val
    
    if path_params_in_signature:
        path_placeholders = re.findall(r"{([^}]+)}", api_path)
        f_string_parts = []
        current_pos = 0
        for placeholder in path_placeholders:
            placeholder_start = api_path.find("{" + placeholder + "}", current_pos)
            if placeholder_start > current_pos:
                f_string_parts.append(ast.Constant(value=api_path[current_pos:placeholder_start]))
            
            # Try to match placeholder (e.g. accountId) to param name (e.g. accountid_val)
            var_name_in_sig = placeholder[0].lower() + placeholder[1:] + "_val" # common pattern
            matching_param = next((p for p in path_params_in_signature if p["name"].lower() == var_name_in_sig.lower()), None)
            
            if not matching_param and path_params_in_signature: # Fallback if naming convention isn't perfect
                 var_name_in_sig_to_use = path_params_in_signature[0]["name"]
            elif matching_param:
                 var_name_in_sig_to_use = matching_param["name"]
            else: # Should not happen if path_placeholders is non-empty & path_params_in_signature
                 var_name_in_sig_to_use = placeholder + "_val" # Best guess

            f_string_parts.append(ast.FormattedValue(
                value=ast.Name(id=var_name_in_sig_to_use, ctx=ast.Load()),
                conversion=-1, format_spec=None ))
            current_pos = placeholder_start + len(placeholder) + 2
        
        if current_pos < len(api_path):
            f_string_parts.append(ast.Constant(value=api_path[current_pos:]))
        
        path_expr = ast.JoinedStr(values=f_string_parts) if f_string_parts else ast.Constant(value=api_path)
    else:
        path_expr = ast.Constant(value=api_path)

    http_call = ast.Call(
        func=ast.Attribute(
            value=ast.Attribute(value=ast.Name(id="self", ctx=ast.Load()), attr="_http", ctx=ast.Load()),
            attr=method_plan["http_method"].lower(), ctx=ast.Load() ),
        args=[path_expr], keywords=[] )

    body_param = next((p for p in sig_info["params"] if p["name"] in ["payload", "query_payload", "data"]), None)
    if body_param:
        http_call.keywords.append(
            ast.keyword(arg="json", value=ast.Name(id=body_param["name"], ctx=ast.Load())) )

    return_type_hint = sig_info["return_type"].lower()
    
    body_stmts = []
    if method_plan["http_method"].upper() == "DELETE" and "bool" in return_type_hint:
        # Assumes _http client raises on non-2xx, so if call succeeds, it's True
        body_stmts = [ast.Expr(value=http_call), ast.Return(value=ast.Constant(value=True))]
    elif "bool" in return_type_hint: # Other methods returning bool (e.g. a check operation)
         # This case might need specific handling based on API. Default to .json() if not DELETE.
         return_expression = ast.Call(func=ast.Attribute(value=http_call, attr="json", ctx=ast.Load()), args=[], keywords=[])
         body_stmts = [ast.Return(value=return_expression)]
    else: # Default: call .json()
        return_expression = ast.Call(func=ast.Attribute(value=http_call, attr="json", ctx=ast.Load()), args=[], keywords=[])
        body_stmts = [ast.Return(value=return_expression)]

    try:
        return_type_annotation_node = ast.parse(sig_info["return_type"]).body[0].value
    except: 
        return_type_annotation_node = ast.Name(id=sig_info["return_type"], ctx=ast.Load())

    method_def = ast.FunctionDef(
        name=method_name, args=args_node, body=body_stmts,
        decorator_list=[], returns=return_type_annotation_node )
    return method_def

def generate_or_update_accounts_content(current_content_str: str, account_plan: list, is_new_file: bool) -> str:
    if not account_plan: # No methods to add
        if is_new_file:
            # Create basic new file structure
            tree = ast.parse("from .._http import _HTTP\n\nclass Accounts:\n    def __init__(self, http: _HTTP):\n        self._http = http\n")
            return astor.to_source(tree)
        return current_content_str

    if is_new_file:
        # Start with a base structure for a new file
        tree = ast.parse("from .._http import _HTTP\n\nclass Accounts:\n    def __init__(self, http: _HTTP):\n        self._http = http\n")
        class_node = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == "Accounts")
        # Add pass to __init__ if it's empty, astor might need it.
        # init_method = next(n for n in class_node.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        # if not init_method.body: init_method.body.append(ast.Pass())
    else:
        tree = ast.parse(current_content_str)
        class_node = next((n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == "Accounts"), None)
        if not class_node:
            # This case should ideally not happen if file exists and is supposed to contain Accounts class
            # For robustness, could create the class here, or raise error.
            # For now, let's assume if file exists, class Accounts exists.
            # If it truly doesn't, astor.to_source(tree) will just return the original content if no changes.
            # Or, more safely:
            print("Error: 'Accounts' class not found in existing file. Cannot add methods.", file=sys.stderr)
            return current_content_str 


    existing_method_names = {m.name for m in class_node.body if isinstance(m, ast.FunctionDef)}
    
    for method_to_add_plan in account_plan:
        new_method_name = parse_signature(method_to_add_plan["sdk_method_signature"])["name"]
        if new_method_name not in existing_method_names:
            method_ast = generate_method_ast(method_to_add_plan)
            class_node.body.append(method_ast)
        else:
            # Optionally, could update existing methods if plan indicates changes
            # For now, only adding new ones.
            print(f"Method '{new_method_name}' already exists. Skipping.", file=sys.stderr)
            
    return astor.to_source(tree)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print(json.dumps({"error": "Usage: python manage_sdk_accounts.py <implementation_plan_json_string> <current_accounts_py_content_string_or_empty> <is_new_file_bool>"}), file=sys.stderr)
        sys.exit(1)

    plan_json_str = sys.argv[1]
    accounts_py_content_str = sys.argv[2]
    is_new_file = sys.argv[3].lower() == 'true'

    try:
        full_plan = json.loads(plan_json_str)
    except json.JSONDecodeError as e:
        print(json.dumps({"error": f"JSON decoding error for implementation plan: {e}"}), file=sys.stderr)
        sys.exit(1)

    account_specific_plan = full_plan.get("Account", [])
    
    # If the plan for "Account" is empty and it's a new file, 
    # we still want the basic class structure.
    # The generate_or_update_accounts_content handles this.
        
    updated_content = generate_or_update_accounts_content(accounts_py_content_str, account_specific_plan, is_new_file)
    print(updated_content)
