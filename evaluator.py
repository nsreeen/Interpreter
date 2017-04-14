import syntax


def execute_calculation(left, right, op):
    if op == "!ADD":
        return left + right
    elif op == "!SUB":
        return left - right
    elif op == "!MUL":
        return left * right


def one_side_expression(statement, statement_side, side):
    if isinstance(statement_side, syntax.Expression) and statement_side.value != None:
         side = statement_side.value
    elif isinstance(statement_side, syntax.Expression) and statement_side.value == None:
         side = evaluate_expression(statement_side)
    else:
         side = statement_side
    return side


def evaluate_expression(statement):
    left, right = None, None
    left = one_side_expression(statement, statement.left, left)
    right = one_side_expression(statement, statement.right, right)
    statement.value = execute_calculation(left, right, statement.operator)
    return statement.value


def evaluate_assignment(assignment, variables):
    name = assignment.name
    value = evaluate_expression(assignment.value)
    variables[name] = value
    return variables


def evaluate_statement(statement, variables):
    if isinstance(statement, syntax.Expression):
        return evaluate_expression(statement)
    elif isinstance(statement, syntax.Assignment):
        return evaluate_assignment(statement, variables)


def evaluate_program(program):
    variables = {}
    for statement in program.statements:
        evaluate_statement(statement, variables)
    return program, variables
