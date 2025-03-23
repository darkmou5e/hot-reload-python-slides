import ast

code = """
def greet():
    return "Hello, World!"
"""

tree = ast.parse(code)
for node in ast.walk(tree):
    if isinstance(node, ast.FunctionDef) and node.name == "greet":
        node.body[0].value.s = "Hello, AST!"

modified_code = compile(tree, "<string>", "exec")
exec(modified_code)
print(greet())  # Вывод: "Hello, AST!"
