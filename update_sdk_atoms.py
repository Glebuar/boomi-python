import json
import sys
import ast
import re
import astor # Import astor

def parse_signature(signature_str: str):
    """Parses an SDK method signature string."""
    match = re.match(r"(\w+)\(([^)]*)\)\s*->\s*(.+)", signature_str)
    if not match:
        raise ValueError(f"Invalid signature format: {signature_str}")
    
    name, params_str, return_type = match.groups()
    
    params = []
    if params_str:
        for p_match_str in params_str.split(','):
            p_match_str = p_match_str.strip()
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
            # Attempt to parse complex types like List[dict] into AST nodes
            try:
                type_annotation_node = ast.parse(p_info["type"]).body[0].value
            except: # Fallback for simple names or if parsing fails
                type_annotation_node = ast.Name(id=p_info["type"], ctx=ast.Load())
        else:
            type_annotation_node = None
        ast_params_list.append(ast.arg(arg=p_info["name"], annotation=type_annotation_node))

    args_node = ast.arguments(
        posonlyargs=[], 
        args=ast_params_list, 
        vararg=None, 
        kwonlyargs=[], 
        kw_defaults=[], 
        kwarg=None, 
        defaults=[]
    )
    
    api_path = method_plan["api_path"]
    path_params_in_signature = [p for p in sig_info["params"] if p["name"] != "self" and "_val" in p["name"]]
    
    if path_params_in_signature:
        path_placeholders = re.findall(r"{([^}]+)}", api_path)
        f_string_parts = []
        current_pos = 0
        for placeholder in path_placeholders:
            placeholder_start = api_path.find("{" + placeholder + "}", current_pos)
            if placeholder_start > current_pos:
                f_string_parts.append(ast.Constant(value=api_path[current_pos:placeholder_start]))
            
            var_name_in_sig = placeholder[0].lower() + placeholder[1:] + "_val"
            # Ensure this var_name_in_sig is actually in our sig_info["params"]
            matching_param = next((p for p in path_params_in_signature if p["name"] == var_name_in_sig), None)
            if not matching_param and path_params_in_signature: # Fallback
                 var_name_in_sig = path_params_in_signature[0]["name"]
            
            f_string_parts.append(ast.FormattedValue(
                value=ast.Name(id=var_name_in_sig, ctx=ast.Load()),
                conversion=-1,
                format_spec=None
            ))
            current_pos = placeholder_start + len(placeholder) + 2
        
        if current_pos < len(api_path):
            f_string_parts.append(ast.Constant(value=api_path[current_pos:]))
        
        path_expr = ast.JoinedStr(values=f_string_parts) if f_string_parts else ast.Constant(value=api_path)
    else:
        path_expr = ast.Constant(value=api_path)

    http_call = ast.Call(
        func=ast.Attribute(
            value=ast.Attribute(value=ast.Name(id="self", ctx=ast.Load()), attr="_http", ctx=ast.Load()),
            attr=method_plan["http_method"].lower(),
            ctx=ast.Load()
        ),
        args=[path_expr],
        keywords=[]
    )

    body_param = next((p for p in sig_info["params"] if p["name"] in ["payload", "query_payload"]), None)
    if body_param:
        http_call.keywords.append(
            ast.keyword(arg="json", value=ast.Name(id=body_param["name"], ctx=ast.Load()))
        )

    return_handling_desc = method_plan.get("response_handling", "").lower()
    return_type_hint = sig_info["return_type"].lower()
    
    # Determine return expression based on HTTP method and return type hint
    if method_plan["http_method"].upper() == "DELETE" and "bool" in return_type_hint:
        # For DELETE returning bool: call the http method, then return True (assuming _http raises on error)
        # Or, if _http returns a response object, check response.ok
        # Let's assume _http returns a response object and we check .ok
        # Stmt1: response = self._http.delete(...)
        # Stmt2: return response.ok
        # For simplicity as per original attempt, if _http raises, just call and return True.
        # However, explicit .ok is safer if available from _http methods.
        # The plan was "Return True on successful deletion". If _http.delete() doesn't return a response object but None on success:
        # For now, let's assume _http methods (like requests') return a response obj.
        # response_var = ast.Name(id="response", ctx=ast.Store())
        # assign_stmt = ast.Assign(targets=[response_var], value=http_call)
        # return_expression = ast.Attribute(value=ast.Name(id="response", ctx=ast.Load()), attr="ok", ctx=ast.Load())
        # body_stmts = [assign_stmt, ast.Return(value=return_expression)]
        # For now, to match the simpler earlier logic:
        # If the method truly returns bool, and it's a DELETE, often it's about the status code.
        # A common pattern is to return nothing on success (204) or raise an error.
        # If the _http client handles raising errors for non-2xx, then we can simplify.
        # Let's assume the _http call itself will handle non-2xx by raising.
        # Then a successful call means we can return True.
        body_stmts = [ast.Expr(value=http_call), ast.Return(value=ast.Constant(value=True))]
    elif "bool" in return_type_hint: # Other methods returning bool
         return_expression = ast.Call(func=ast.Attribute(value=http_call, attr="json", ctx=ast.Load()), args=[], keywords=[])
         body_stmts = [ast.Return(value=return_expression)]
    else: # Default: call .json()
        return_expression = ast.Call(func=ast.Attribute(value=http_call, attr="json", ctx=ast.Load()), args=[], keywords=[])
        body_stmts = [ast.Return(value=return_expression)]

    try:
        return_type_annotation_node = ast.parse(sig_info["return_type"]).body[0].value
    except: # Fallback for simple names or if parsing fails
        return_type_annotation_node = ast.Name(id=sig_info["return_type"], ctx=ast.Load())

    method_def = ast.FunctionDef(
        name=method_name,
        args=args_node,
        body=body_stmts,
        decorator_list=[],
        returns=return_type_annotation_node
    )
    return method_def


def update_atoms_file_content(current_content: str, atom_plan: list) -> str:
    if not atom_plan:
        return current_content

    tree = ast.parse(current_content)
    
    class_modified = False
    for node in tree.body:
        if isinstance(node, ast.ClassDef) and node.name == "Atoms":
            existing_method_names = {m.name for m in node.body if isinstance(m, ast.FunctionDef)}
            
            for method_to_add_plan in atom_plan:
                new_method_name = parse_signature(method_to_add_plan["sdk_method_signature"])["name"]
                if new_method_name not in existing_method_names:
                    method_ast = generate_method_ast(method_to_add_plan)
                    node.body.append(method_ast)
                    class_modified = True
            break 

    if class_modified:
        return astor.to_source(tree) # Use astor to convert AST back to source

    return current_content

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(json.dumps({"error": "Usage: python update_sdk_atoms.py <implementation_plan_json_string> <current_atoms_py_content_string>"}), file=sys.stderr)
        sys.exit(1)

    plan_json_str = sys.argv[1]
    atoms_py_content_str = sys.argv[2]

    try:
        full_plan = json.loads(plan_json_str)
    except json.JSONDecodeError as e:
        print(json.dumps({"error": f"JSON decoding error for implementation plan: {e}"}), file=sys.stderr)
        sys.exit(1)

    atom_specific_plan = full_plan.get("Atom", [])
    if not atom_specific_plan:
        print(atoms_py_content_str)
        sys.exit(0)
        
    updated_content = update_atoms_file_content(atoms_py_content_str, atom_specific_plan)
    print(updated_content)
