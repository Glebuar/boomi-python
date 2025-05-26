import ast
import sys
import json
import astor # Ensure astor is available

def update_resources_init_content(current_content: str, class_name: str, module_name: str) -> str:
    tree = ast.parse(current_content)
    
    # 1. Add Import: from .<module_name> import <ClassName>
    new_import = ast.ImportFrom(
        module=module_name,  # The module name like 'accounts'
        names=[ast.alias(name=class_name, asname=None)],
        level=1  # Relative import: from .<module>
    )
    
    # Insert the import statement. Try to place it with other similar imports.
    # A simple strategy: insert after the last existing ImportFrom, or at the beginning.
    last_import_idx = -1
    for i, node in enumerate(tree.body):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            # Check if this specific import already exists
            if isinstance(node, ast.ImportFrom) and node.module == module_name:
                if any(alias.name == class_name for alias in node.names):
                    print(f"Import for {class_name} from .{module_name} already exists. Skipping import addition.", file=sys.stderr)
                    new_import = None # Signal not to add
                    break
            last_import_idx = i
    if new_import is not None: # if not already found
        if last_import_idx != -1:
            tree.body.insert(last_import_idx + 1, new_import)
        else: # No imports yet, insert at the beginning
            tree.body.insert(0, new_import)

    # 2. Add ClassName to __all__
    all_list_node = None
    all_assign_node = None
    
    for i, node in enumerate(tree.body):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "__all__":
                    all_assign_node = node
                    if isinstance(node.value, ast.List):
                        all_list_node = node.value
                    break
            if all_assign_node: break
            
    if all_list_node:
        # __all__ exists and is a list. Add the class name if not already present.
        if not any(isinstance(elt, ast.Constant) and elt.value == class_name for elt in all_list_node.elts):
            all_list_node.elts.append(ast.Constant(value=class_name))
            # Sort the __all__ list alphabetically
            all_list_node.elts.sort(key=lambda x: x.value if isinstance(x, ast.Constant) else "")
    elif all_assign_node: 
        # __all__ is assigned but not a list (e.g. a variable). This is unusual.
        print(f"Warning: __all__ is defined but not as a list. Cannot automatically add {class_name}.", file=sys.stderr)
    else:
        # __all__ does not exist. Create it.
        new_all_assign = ast.Assign(
            targets=[ast.Name(id="__all__", ctx=ast.Store())],
            value=ast.List(elts=[ast.Constant(value=class_name)], ctx=ast.Load())
        )
        # Add it after imports or at the end of the file.
        if last_import_idx != -1:
            tree.body.insert(last_import_idx + 1, new_all_assign) # after last import
        else:
            tree.body.append(new_all_assign) # or at the end

    return astor.to_source(tree)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python update_resources_init.py <current_init_content> <ClassName> <module_name>", file=sys.stderr)
        sys.exit(1)
        
    current_content_arg = sys.argv[1]
    class_name_arg = sys.argv[2]
    module_name_arg = sys.argv[3]
    
    updated_code = update_resources_init_content(current_content_arg, class_name_arg, module_name_arg)
    print(updated_code)
