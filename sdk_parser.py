import ast
import json
import sys # Ensure sys is imported

def derive_resource_name(class_name):
    if class_name == "Execute":
        return "Execute"
    if class_name == "RuntimeRelease":
        return "RuntimeRelease"
    if class_name.endswith('s') and class_name != "Process": # Avoid turning "Process" into "Proces"
        return class_name[:-1]
    return class_name

def get_public_methods(class_node):
    public_methods = []
    for node in class_node.body:
        if isinstance(node, ast.FunctionDef) and not node.name.startswith('_'):
            # Exclude common inherited/boilerplate methods if necessary, e.g. from a base class
            # For now, assuming all non-underscored methods in the class body are relevant operations
            public_methods.append(node.name)
    return sorted(list(set(public_methods)))

def analyze_sdk_files(file_contents_map):
    resource_operations = {}

    for filepath, content in file_contents_map.items():
        try:
            tree = ast.parse(content, filename=filepath) # Add filename for better error messages
            for node in tree.body:
                if isinstance(node, ast.ClassDef):
                    class_name = node.name
                    resource_name = derive_resource_name(class_name)
                    public_methods = get_public_methods(node)
                    
                    if public_methods:
                        if resource_name in resource_operations:
                            existing_methods = set(resource_operations[resource_name])
                            for method in public_methods:
                                existing_methods.add(method)
                            resource_operations[resource_name] = sorted(list(existing_methods))
                        else:
                            resource_operations[resource_name] = public_methods
        except SyntaxError as e:
            print(f"Syntax error in {filepath}: {e}", file=sys.stderr) # Print errors to stderr
            # Decide if errors should be in the JSON output or halt processing
            # For now, just printing to stderr and continuing.
        except Exception as e:
            print(f"Error processing {filepath}: {e}", file=sys.stderr) # Print errors to stderr

    return resource_operations

if __name__ == '__main__':
    # Read the JSON map of {filepath: content} from stdin
    try:
        input_json_str = sys.stdin.read()
        if not input_json_str:
            print("Error: No input received on stdin.", file=sys.stderr)
            sys.exit(1)
        
        file_contents_map = json.loads(input_json_str)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON input: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error reading input: {e}", file=sys.stderr)
        sys.exit(1)

    # Perform analysis
    result = analyze_sdk_files(file_contents_map)
    
    # Print the final JSON result to stdout
    try:
        print(json.dumps(result, indent=2))
    except TypeError as e:
        print(json.dumps({"error": f"Could not serialize result to JSON: {e}"}), file=sys.stderr)
        sys.exit(1)
