import syntax


def execute_calculation(left, right, op):
    if op == "!ADD":
        return left + right
    elif op == "!SUB":
        return left - right
    elif op == "!MUL":
        return left * right


def one_side_expression(statement, statement_side, side, dictionary):
    if isinstance(statement_side, syntax.Expression) and statement_side.value != None:
        side = statement_side.value
    elif isinstance(statement_side, syntax.Expression) and statement_side.value == None:
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
    #print("ev exp gets val from ex calc : ", statement.value)
    return statement, dictionary


def evaluate_assignment(statement, dictionary): #, variables):
    name = statement.name
    if statement.value.value != None:
        #print("statement.value.value is ", statement.value.value)
        value = statement.value
    else:
        statement.value, dictionary = evaluate_expression(statement.value, dictionary)
        value = statement.value
    dictionary[name] = value
    return statement, dictionary


def evaluate_statement(statement, dictionary):
    if isinstance(statement, syntax.Expression):
        return evaluate_expression(statement, dictionary)
    elif isinstance(statement, syntax.Assignment):
        return evaluate_assignment(statement, dictionary)


def evaluate_program(program, dictionary):
    #variables = {}
    for statement in program.statements:
        statement, dictionary = evaluate_statement(statement, dictionary)
    #print(program.__dict__)
    return program, dictionary
