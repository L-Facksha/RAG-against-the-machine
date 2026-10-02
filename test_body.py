import ast

source = """
def hello(name):
    x = 10
    print(name)
    if x > 5:
        print("big")
    if x > 5:
        print("big")
    if x > 5:
        if x > 5:
            print("big")
        print("big")
    return x
"""

tree = ast.parse(source)

for node in ast.walk(tree):
    if isinstance(node, ast.FunctionDef):
        print("About func: ", node.end_lineno)
    if isinstance(node, ast.FunctionDef):
        print("FUNCTION:", node.name)
        print("BODY:")

        for statement in node.body:
            # print(statement.lineno)
            # if type(statement).__name__ == "If":
            #     for child in statement.body:
            #         print(
            #             type(child).__name__,
            #             "line:", statement.lineno,
            #             "end line:", statement.end_col_offset
            #         )
            print(
                type(statement).__name__,
                "line:", statement.end_lineno,
                "end line:", statement.end_col_offset
            )
