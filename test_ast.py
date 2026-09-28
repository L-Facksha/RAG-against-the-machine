import ast

source = """
x = 10

def hello(name):
    return "Hello " + name
"""

tree = ast.parse(source)

for node in ast.walk(tree):
    if isinstance(node, ast.FunctionDef):
        print(node.name)

        for statement in node.body:
            print(type(statement).__name__)