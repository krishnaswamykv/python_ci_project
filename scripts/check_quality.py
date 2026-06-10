import ast
import os
import sys

for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".py"):

            path = os.path.join(root, file)

            if ".venv" in path or "venv" in path:
                continue

            # Check file length
            lines = sum(1 for _ in open(path))

            if lines > 100:
                print(f"ERROR: {path} has {lines} lines (>100)")
                sys.exit(1)

            # Check docstrings
            with open(path, "r") as f:
                tree = ast.parse(f.read())

            for node in ast.walk(tree):
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    if ast.get_docstring(node) is None:
                        print(
                            f"ERROR: Function '{node.name}' in {path} has no docstring"
                        )
                        sys.exit(1)

print("All quality checks passed.")
