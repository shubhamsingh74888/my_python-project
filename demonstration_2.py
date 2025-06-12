import ast
import re

def is_snake_case(name):
    return re.match(r'^[a-z_][a-z0-9_]*$', name) is not None

def check_docstring(node):
    return ast.get_docstring(node) is not None

def check_inline_comments(lines):
    return any(line.strip().startswith('#') for line in lines)

def check_indentation(code_lines):
    for i, line in enumerate(code_lines):
        if line.strip():  # skip blank lines
            stripped = line.lstrip('\t ')
            indent = len(line) - len(stripped)
            if indent % 4 != 0:
                return False, i + 1
    return True, -1

def software_assurance_checklist(source_code):
    results = {
        "Function Naming Convention": [],
        "Docstring Present": [],
        "Inline Comments": False,
        "Indentation Check": True
    }

    # Parse code to AST
    tree = ast.parse(source_code)
    lines = source_code.splitlines()

    # Check indentation
    indent_ok, bad_line = check_indentation(lines)
    results["Indentation Check"] = indent_ok
    if not indent_ok:
        print(f"[Indentation] Improper indentation at line {bad_line}")

    # Check inline comments
    results["Inline Comments"] = check_inline_comments(lines)

    # Analyze functions
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            results["Function Naming Convention"].append(
                (node.name, is_snake_case(node.name))
            )
            results["Docstring Present"].append(
                (node.name, check_docstring(node))
            )

    return results

# Example Python code to test
test_code = '''
def MyFunction(x, y):
    """This is a sample function"""
    result = x + y  # add the numbers
    return result

def anotherFunction():
  x = 1
  y = 2
  return x + y
'''

# Run the checklist
results = software_assurance_checklist(test_code)

# Display results
print("=== Software Assurance Checklist ===")
for func, ok in results["Function Naming Convention"]:
    print(f"[Naming] Function '{func}': {'OK' if ok else 'Not snake_case'}")

for func, ok in results["Docstring Present"]:
    print(f"[Docstring] Function '{func}': {'Present' if ok else 'Missing'}")

print(f"[Comments] Inline comments: {'Present' if results['Inline Comments'] else 'Missing'}")
print(f"[Indentation] Consistent: {'Yes' if results['Indentation Check'] else 'No'}")
