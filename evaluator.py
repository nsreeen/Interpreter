
def execute_calculation(left, right, op):
    if op == "!ADD":
        return left + right
    elif op == "!SUB":
        return left - right
    elif op == "!MUL":
        return left * right

def calculate_value_of_expression(expression):
    if isinstance(expression.left, int) and isinstance(expression.right, int):
        return execute_calculation(expression.left, expression.right, expression.operator)
    elif expression.left.value and expression.right.value:
        return execute_calculation(expression.left.value, expression.right.value, expression.operator)

def traverse_graph_expressions(program):
    for statement in program.statements:
        if statement.expression: #only expressions have operator
            expression.value = calculate_value_of_expression(statement)

#why is program a nonetype object?!?!?!
