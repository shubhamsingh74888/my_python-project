def sample_function(x, y):
    """A simple sample function to test: returns x divided by y"""
    if y == 0:
        return "Error: Division by zero"
    return x / y

# Define test cases as tuples: (input_args, expected_output)
test_cases = [
    ((10, 2), 5),
    ((5, 0), "Error: Division by zero"),
    ((9, 3), 3),
    ((0, 1), 0),
    ((-10, 2), -5),
]

def run_tests(func, test_cases):
    print("=== Automated Software Testing Report ===")
    passed = 0

    for i, (inputs, expected) in enumerate(test_cases):
        try:
            actual = func(*inputs)
            result = "PASS" if actual == expected else "FAIL"
            if result == "PASS":
                passed += 1
            print(f"Test Case {i + 1}: {inputs}")
            print(f"Expected: {expected}, Actual: {actual} -> {result}\n")
        except Exception as e:
            print(f"Test Case {i + 1}: {inputs}")
            print(f"Exception occurred: {e} -> FAIL\n")

    total = len(test_cases)
    print(f"Summary: {passed}/{total} test cases passed.")

# Run the tests
run_tests(sample_function, test_cases)
