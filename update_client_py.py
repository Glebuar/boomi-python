import ast
import sys
import json
import astor # Ensure astor is available

def update_client_content(current_content: str, class_name: str, module_name: str) -> str: # Added module_name
    tree = ast.parse(current_content)
    
    # 1. Add Import: from .resources.<module_name> import <ClassName>
    new_import = ast.ImportFrom(
        module=f"resources.{module_name}",  # e.g. resources.accounts
        names=[ast.alias(name=class_name, asname=None)],
        level=1 # from .resources.accounts
    )
    
    import_exists = False
    last_import_from_resources_idx = -1
    
    # Find existing imports from .resources to place the new import nearby
    # And check if the exact import already exists
    for i, node in enumerate(tree.body):
        if isinstance(node, ast.ImportFrom) and node.level == 1: # Relative import
            if node.module and node.module.startswith("resources."):
                last_import_from_resources_idx = i
                if node.module == f"resources.{module_name}":
                    if any(alias.name == class_name for alias in node.names):
                        print(f"Import for {class_name} from .{node.module} already exists. Skipping import addition.", file=sys.stderr)
                        import_exists = True
                        break
    
    if not import_exists:
        if last_import_from_resources_idx != -1:
            # Insert after the last 'from .resources.xxx import Yyy'
            tree.body.insert(last_import_from_resources_idx + 1, new_import)
        else:
            # Fallback: if no '.resources.xxx' imports, find any import and insert after it
            # Or insert at the beginning after __future__ imports
            last_import_idx = -1
            for i, node in enumerate(tree.body):
                if isinstance(node, (ast.Import, ast.ImportFrom)):
                    last_import_idx = i
            if last_import_idx != -1:
                 tree.body.insert(last_import_idx + 1, new_import)
            else: # No imports at all, very unlikely for this file. Add at top.
                 tree.body.insert(0, new_import)


    # 2. Add attribute to Boomi.__init__
    class_def_found = False
    for node in tree.body:
        if isinstance(node, ast.ClassDef) and node.name == "Boomi":
            class_def_found = True
            init_method_found = False
            for class_member in node.body:
                if isinstance(class_member, ast.FunctionDef) and class_member.name == "__init__":
                    init_method_found = True
                    attr_name = class_name.lower() # e.g. accounts
                    
                    if any(isinstance(stmt, ast.Assign) and \
                           isinstance(stmt.targets[0], ast.Attribute) and \
                           stmt.targets[0].attr == attr_name \
                           for stmt in class_member.body):
                        print(f"Attribute self.{attr_name} already exists in Boomi.__init__. Skipping.", file=sys.stderr)
                        break 

                    new_assign = ast.Assign(
                        targets=[ast.Attribute(
                            value=ast.Name(id="self", ctx=ast.Load()),
                            attr=attr_name, 
                            ctx=ast.Store()
                        )],
                        value=ast.Call(
                            func=ast.Name(id=class_name, ctx=ast.Load()), 
                            args=[ast.Name(id="http", ctx=ast.Load())], 
                            keywords=[]
                        )
                    )
                    
                    insert_idx = len(class_member.body)
                    # Try to insert before a `classmethod` or after the last `self.xxx =`
                    last_self_assign_idx = -1
                    for i, stmt in enumerate(class_member.body):
                        if isinstance(stmt, ast.Assign) and isinstance(stmt.targets[0], ast.Attribute) and \
                           isinstance(stmt.targets[0].value, ast.Name) and stmt.targets[0].value.id == 'self':
                            last_self_assign_idx = i
                        if isinstance(stmt, ast.Return): # Should not be a return here, but good to check
                            insert_idx = i
                            break
                    
                    if last_self_assign_idx != -1 :
                        insert_idx = last_self_assign_idx + 1
                    else: # No self.xxx assignments found, insert after http = _HTTP(...)
                        for i, stmt in enumerate(class_member.body):
                            if isinstance(stmt, ast.Assign) and stmt.targets[0].id == 'http':
                                insert_idx = i + 1
                                break
                    
                    class_member.body.insert(insert_idx, new_assign)
                    break 
            
            if not init_method_found:
                 print("Warning: Boomi.__init__ method not found. Cannot add attribute.", file=sys.stderr)
            break 

    if not class_def_found:
        print("Warning: Boomi class definition not found. Cannot add attribute.", file=sys.stderr)
        
    return astor.to_source(tree)

if __name__ == '__main__':
    if len(sys.argv) != 4: # Expect current_client_content, ClassName, module_name
        print("Usage: python update_client_py.py <current_client_content> <ClassName> <module_name>", file=sys.stderr)
        sys.exit(1)
        
    current_content_arg = sys.argv[1]
    class_name_arg = sys.argv[2]
    module_name_arg = sys.argv[3] # Added module_name
    
    updated_code = update_client_content(current_content_arg, class_name_arg, module_name_arg)
    print(updated_code)
