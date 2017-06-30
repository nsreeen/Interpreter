import parser

def execute_calculation(left, right, op):
    if op == "!ADD":
        return left + right
    elif op == "!SUB":
        return left - right
    elif op == "!MUL":
        return left * right


def evaluate_expression(program, current, dictionary):

    # If current already has a value, return
    if current.value:
        return program, current.value, dictionary

    # If current only has a left attribute which is an int, that is the value, so return
    elif current.left and isinstance(current.left, int) and current.right == None:
        current.value = current.left
        return program, current.value, dictionary

    # Extra steps needed to find the value
    else:
        left, right = None, None

        # Add missing values (from dictionary, or nested Expression objects)
        if current.left in dictionary:
            current.left = dictionary[current.left]
            left = current.left
        if current.right in dictionary:
            current.right = dictionary[current.right]
            right = current.right
        if isinstance(current.left, parser.Expression):
            program, current.left.value, dictionary  = evaluate_expression(program, current.left, dictionary)
            left = current.left.value
        if isinstance(current.right, parser.Expression):
            program, current.right.value, dictionary = evaluate_expression(program, current.right, dictionary)
            right = current.right.value
        if isinstance(current.left, int):
            left = current.left
        if isinstance(current.right, int):
            right = current.right

        # Find value
        if current.left and current.right and current.value == None:
            current.value = execute_calculation(left, right, current.operator)
        elif isinstance(current.left, int):
            current.value = current.left
        else:
            current.value = current.left.value

        return program, current.value, dictionary

def evaluate_assignment(program, statement, dictionary):
    # Assignment object has name and value attributes (value will be an Expression object)
    name = statement.name
    if statement.value.value != None:
        # value attribute is an Expression object that already has a value
        # replace the Assignment objects value (Expression object) with this value (int)
        value = statement.value.value
    else:
        # value attribute is an Expression object does not have a value
        program, value, dictionary = evaluate_expression(program, statement.value, dictionary)
    # add variable to the dictionary
    dictionary[name] = value
    return statement, dictionary

def evaluate_statement(program, statement, dictionary):
    if isinstance(statement, parser.Expression):
        program, statement.value, dictionary = evaluate_expression(program, statement, dictionary)
        return statement, dictionary
    elif isinstance(statement, parser.Assignment):
        return evaluate_assignment(program, statement, dictionary)

def evaluate_program(program, dictionary):
    for statement in program.statements:
        statement, dictionary = evaluate_statement(program, statement, dictionary)

    return program, dictionary
