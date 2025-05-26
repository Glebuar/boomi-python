import json
import sys

def parse_openapi_data(openapi_content_str):
    try:
        openapi_data = json.loads(openapi_content_str)
    except json.JSONDecodeError as e:
        # Print error as JSON to stdout, as the expected output is JSON
        print(json.dumps({"error": f"Invalid JSON input: {e}"}))
        sys.exit(1)

    unique_tags = set()
    if 'tags' in openapi_data and isinstance(openapi_data['tags'], list):
        for tag_obj in openapi_data['tags']:
            if isinstance(tag_obj, dict) and 'name' in tag_obj:
                unique_tags.add(tag_obj['name'])
    
    tagged_paths = {tag: [] for tag in unique_tags}

    if 'paths' in openapi_data and isinstance(openapi_data['paths'], dict):
        for path, path_item in openapi_data['paths'].items():
            if not isinstance(path_item, dict):
                continue
            for method, operation in path_item.items():
                # Check if the key is a potential HTTP method.
                # OpenAPI methods are typically lowercase.
                # More robustly, one might check against a list of known HTTP methods.
                if method.lower() in ['get', 'post', 'put', 'delete', 'patch', 'options', 'head', 'trace']:
                    if isinstance(operation, dict) and 'tags' in operation and isinstance(operation['tags'], list):
                        for tag_name in operation['tags']:
                            if tag_name in tagged_paths: # Ensure the tag was in the global "tags" list
                                tagged_paths[tag_name].append({
                                    'path': path,
                                    'method': method.upper() # Standardize to uppercase
                                })
    
    # Filter out tags that ended up with no paths (e.g. if a tag in paths wasn't in the global tags list)
    # Or if a globally defined tag is simply not used in any path.
    final_tagged_paths = {tag: paths for tag, paths in tagged_paths.items() if paths}
    
    try:
        # Print the final JSON result to stdout
        print(json.dumps(final_tagged_paths, indent=2))
    except TypeError as e:
        # Print error as JSON to stdout
        print(json.dumps({"error": f"Could not serialize result to JSON: {e}"}))
        sys.exit(1)

if __name__ == '__main__':
    # Read the OpenAPI JSON content from stdin
    openapi_json_content_from_stdin = sys.stdin.read()
    parse_openapi_data(openapi_json_content_from_stdin)
