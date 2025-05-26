import json
import sys

def update_or_add_conceptual_tests(original_tests_json_str: str) -> str:
    try:
        tests_plan = json.loads(original_tests_json_str)
    except json.JSONDecodeError as e:
        print(f"Error decoding original_tests_json: {e}", file=sys.stderr)
        # If input is crucial and parsing fails, might be better to return original or error out.
        # For now, let's assume it might be an empty structure if it's the first time.
        tests_plan = {}


    # --- Update/Add Test for Atoms.list() ---
    atom_tests = tests_plan.get("Atom", [])
    
    # Remove any pre-existing (unlikely for 'list' from step 8) test for Atoms.list to avoid duplicates
    # This assumes test_method_name would be 'test_list_success' or similar.
    # A more robust check would be on sdk_method_under_test == "list".
    atom_tests = [t for t in atom_tests if t.get("sdk_method_under_test") != "list"]

    list_description = (
        "Verifies the refactored `list` method's dual behavior: "
        "1. (No payload): Calls `self._http.get` with API path '/Atom'. "
        "2. (With payload): Calls `self._http.post` with API path '/Atom/query' and passes the `query_payload` as JSON. "
        "Ensures the method returns the mocked JSON response, which should be a list of Atom-like dictionaries."
    )
    atoms_list_test = {
        "test_method_name": "test_atoms_list_refactored_success",
        "sdk_class_name": "Atoms",
        "sdk_method_under_test": "list",
        "description": list_description
    }
    atom_tests.append(atoms_list_test)
    tests_plan["Atom"] = atom_tests

    # --- Update/Add Test for Components.get() ---
    component_tests = tests_plan.get("Component", []) # Changed from "Components" to "Component" to match typical resource key
    
    # Remove any pre-existing test for Components.get()
    component_tests = [t for t in component_tests if t.get("sdk_method_under_test") != "get"]

    get_description = (
        "Verifies the refactored `get` method: "
        "Calls `self._http.get` with the API path '/Component/{componentId}' (with `componentId` substituted). "
        "Ensures the call is made without XML-specific headers. "
        "Verifies that the method processes the JSON response using `Component.model_validate(response.json())`. "
        "The mocked response should be a dictionary aligning with the updated `Component` model (which includes `description` and `version`)."
    )
    components_get_test = {
        "test_method_name": "test_components_get_refactored_success",
        "sdk_class_name": "Components",
        "sdk_method_under_test": "get",
        "description": get_description
    }
    component_tests.append(components_get_test)
    tests_plan["Component"] = component_tests # Changed from "Components" to "Component"

    return json.dumps(tests_plan, indent=2)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(json.dumps({"error": "Usage: python update_conceptual_tests.py <original_conceptual_tests_json_string>"}), file=sys.stderr)
        sys.exit(1)

    original_tests_json_arg = sys.argv[1]
    
    updated_tests_json = update_or_add_conceptual_tests(original_tests_json_arg)
    print(updated_tests_json)
