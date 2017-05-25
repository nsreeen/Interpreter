
class Program():
    def __init__(self):
        self.statements = []

class Expression():
    def __init__(self, left=None, right=None, operator=None, value=None):
        self.left = left
        self.right = right
        self.operator = operator
        self.value = value
        self.expression = True

class Assignment():
    def __init__(self, name=None, value=None):
        self.name = name
        self.value = value
        self.expression = False

def print_error(message):
    print("ERROR: ", message)

def parse_program(tokens, dictionary):
    program = Program()
    while tokens:
        statement = parse_statement(tokens, dictionary)
        if statement:
            program.statements.append(statement)
        else:
            return
    return program


def parse_statement(tokens, dictionary):
    if len(tokens) > 2 and tokens[1].type == "VAR" and tokens[2].type == "ASS":
        return parse_assignment(tokens, dictionary)
    return parse_expression(tokens, dictionary)


def parse_expression_side(tokens, dictionary):
    print('\n in parse_expression_side \n')

    if tokens[0].type == "OPE":
        return parse_expression(tokens, dictionary)

    elif tokens[0].type == "NUM":
        first = tokens.pop(0)
        return int(first.value)

    elif tokens[0].type == "VAR" and first.value in dictionary:
        first = tokens.pop(0)
        val = dictionary[first.value]
        return int(val.value)

    elif tokens[0].type == "VAR":
        first = tokens.pop(0)
        return first.value

    else:
        print_error("Expression side could not be parsed")


def parse_expression(tokens, dictionary):
    print('\n in parse expression, first token is: ', tokens[0])
    if tokens[0].type == "OPE":
        tokens.pop(0)
    else:
        print("\n Statement doesn't start with | \n", tokens[0])
        return
    left = parse_expression_side(tokens, dictionary)
    if tokens[0].type == "CLO":
        value = left
        result = Expression(left=value, value=value)
    elif tokens[0].type == "OPP":
        operator = tokens.pop(0).value
        print('\n', operator, tokens[0])
        right = parse_expression_side(tokens, dictionary)
        result = Expression(left=left, right=right, operator=operator)
    else:
        print_error("Expression could not be parsed")
        return
    if tokens[0].type == "CLO":
        tokens.pop(0)
    else:
        print("\n Assignment syntax incorrect \n", tokens[0])
        return
    return result


def parse_assignment(tokens, dictionary):
    if tokens[0].type == "OPE":
        tokens.pop(0)
    else:
        print_error("Statement doesn't start with | ")
        return
    name = tokens.pop(0).value
    tokens.pop(0)
    expression = parse_expression(tokens, dictionary)
    if tokens[0].type == "CLO":
        tokens.pop(0)
    else:
        print_error("Assignment syntax incorrect")
        return
    return Assignment(name, expression)
