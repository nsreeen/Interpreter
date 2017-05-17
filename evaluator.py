import parser

def execute_calculation(left, right, op):
    if op == "!ADD":
        return left + right
    elif op == "!SUB":
        return left - right
    elif op == "!MUL":
        return left * right

def one_side_expression(statement, statement_side, side, dictionary):
    if isinstance(statement_side, parser.Expression) and statement_side.value != None:
        side = statement_side.value
    elif isinstance(statement_side, parser.Expression) and statement_side.value == None:
        side = evaluate_expression(statement_side)
    else:
        side = statement_side
    return side

def evaluate_expression(statement, dictionary):
    if statement.value != None and statement.value in dictionary:
            statement.value = dictionary[statement_side].value
    else:
        left, right = None, None
        left = one_side_expression(statement, statement.left, left, dictionary)
        right = one_side_expression(statement, statement.right, right, dictionary)
        statement.value = execute_calculation(left, right, statement.operator)
    return statement, dictionary

def evaluate_assignment(statement, dictionary):
    name = statement.name
    if statement.value.value != None:
        value = statement.value
    else:
        statement.value, dictionary = evaluate_expression(statement.value, dictionary)
        value = statement.value
    dictionary[name] = value
    return statement, dictionary

def evaluate_statement(statement, dictionary):
    if isinstance(statement, parser.Expression):
        return evaluate_expression(statement, dictionary)
    elif isinstance(statement, parser.Assignment):
        return evaluate_assignment(statement, dictionary)

def evaluate_program(program, dictionary):
    for statement in program.statements:
        statement, dictionary = evaluate_statement(statement, dictionary)
    return program, dictionary
