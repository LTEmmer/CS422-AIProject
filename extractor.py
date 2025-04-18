import ast
from typing import List, Dict


def extract_definitions(file_path: str) -> List[Dict]:
    """Extract class and function definitions from a Python file using AST."""
    with open(file_path, "r", encoding="utf-8") as f:
        source = f.read()

    try:
        tree = ast.parse(source)
    except SyntaxError as e:
        print(f"Syntax error in {file_path}: {e}")
        return []

    definitions = []
    lines = source.splitlines()

    class Extractor(ast.NodeVisitor):
        def visit_FunctionDef(self, node):
            # Skip functions that are inside classes (we'll handle them in visit_ClassDef)
            if not any(isinstance(parent, ast.ClassDef) for parent in ast.walk(node)):
                if hasattr(node, "lineno") and hasattr(node, "end_lineno"):
                    code = "\n".join(lines[node.lineno - 1: node.end_lineno])
                    definitions.append({
                        "type": "function",
                        "name": node.name,
                        "code": code
                    })
            self.generic_visit(node)

        def visit_ClassDef(self, node):
            class_code = "\n".join(lines[node.lineno - 1: node.end_lineno])
            definitions.append({
                "type": "class",
                "name": node.name,
                "code": class_code
            })

            # Collect methods
            methods = []
            for child in node.body:
                if isinstance(child, ast.FunctionDef):
                    method_code = "\n".join(lines[child.lineno - 1: child.end_lineno])
                    methods.append({
                        "type": "method",
                        "name": child.name,
                        "code": method_code
                    })

            # Only add methods if they're not shadowing standalone functions
            standalone_funcs = {d['name'] for d in definitions if d['type'] == 'function'}
            for method in methods:
                if method['name'] not in standalone_funcs:
                    definitions.append({
                        "type": "method",
                        "name": f"{node.name}.{method['name']}",
                        "code": method['code']
                    })
            self.generic_visit(node)

    Extractor().visit(tree)
    return definitions
