import syntax

def execute_calculation(left, right, op):
    if op == "!ADD":
        return left + right
    elif op == "!SUB":
        return left - right
    elif op == "!MUL":
        return left * right

def evaluate_expression(statement):
    print("evaluating expression")
    #if statement.value != None:
    #    return statement.value

    if isinstance(statement.left, syntax.Expression) and statement.left.value != None:
        print("1 1")
        left = statement.left.value
    elif isinstance(statement.left, syntax.Expression) and statement.left.value == None:
        print("1 2")
        left = evaluate_expression(statement.left)
    else:
        left = statement.left
        print("1 3 ", left, type(left))

    if isinstance(statement.right, syntax.Expression) and statement.right.value != None:
        print("2 1")
        right = statement.right.value
        print(right, type(right))
    elif isinstance(statement.right, syntax.Expression) and statement.right.value == None:
        print("2 2")
        right = evaluate_expression(statement.right)
    else:
        right = statement.right
        print("2 3", right, type(right))

    print("HERE!!!   left: ", left, "right: ", right)
    print(statement.left, statement.operator, statement.right, statement.value)
    statement.value = execute_calculation(left, right, statement.operator)
    print("RESULT ===> ", statement.value)

    return statement.value


def evaluate_assignment(assignment, variables):
    print("evaluating assignment", assignment.name, assignment.value)
    name = assignment.name
    value = evaluate_expression(assignment.value)
    variables[name] = value
    print(variables)
    return variables


def evaluate_statement(statement, variables):
    print("evaluating statement")
    if isinstance(statement, syntax.Expression):
        print("is expression")
        return evaluate_expression(statement)
    elif isinstance(statement, syntax.Assignment):
        print("is assignment")
        #print(statement.name, " : ", evaluate_expression(statement.value))
        return evaluate_assignment(statement, variables)
    else:
        print("problem evaluating statement")


def evaluate_program(program):
    print("evaluating program")
    variables = {}
    for statement in program.statements:
        evaluate_statement(statement, variables)
    print("program variables: ")
    for key in variables:
        print(key, " : ", variables[key])
        
    print("\n output of statements")

    for statement in program.statements:
        if isinstance(statement, syntax.Assignment):
            print(variables[statement.name])
        elif isinstance(statement, syntax.Expression):
            print(statement.value)
