import ast

class CyclomaticComplexityVisitor(ast.NodeVisitor):
    def __init__(self):
        self.decision_points = 0

    def visit_If(self, node):
        self.decision_points += 1
        self.generic_visit(node)

    def visit_For(self, node):
        self.decision_points += 1
        self.generic_visit(node)

    def visit_While(self, node):
        self.decision_points += 1
        self.generic_visit(node)

    def visit_Try(self, node):
        self.decision_points += len(node.handlers)  # each except block is a decision
        self.generic_visit(node)

    def visit_BoolOp(self, node):
        # e.g., if a and b or c
        self.decision_points += len(node.values) - 1
        self.generic_visit(node)

    def visit_With(self, node):
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        self.generic_visit(node)

def calculate_cyclomatic_complexity(code):
    tree = ast.parse(code)
    visitor = CyclomaticComplexityVisitor()
    visitor.visit(tree)
    complexity = 1 + visitor.decision_points
    return complexity

# Example function to analyze
example_code = """
def example_function(x):
    if x > 0:
        print("Positive")
    elif x == 0:
        print("Zero")
    else:
        print("Negative")

    for i in range(5):
        if i % 2 == 0:
            print(i)

    while x < 10:
        x += 1
"""

# Run the analysis
complexity = calculate_cyclomatic_complexity(example_code)
print("Cyclomatic Complexity:", complexity)
