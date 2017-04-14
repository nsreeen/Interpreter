"""non terminals (should have own func in parser and most have own class):
GRAMMAR:

PROGRAM := STMT +

STMT := EXPR
        ASSIGNMENT

EXPR := | EXPR operator EXPR >
        INTEGER
        NAME

ASSIGNMENT :=
        NAME <- EXPR"""

from pprint import pprint

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


def parse_program(tokens):
    program = Program()
    while tokens:
        statement = parse_statement(tokens)
        if statement:
            program.statements.append(statement)
        else:
            print_error(("no statement, tokens: ", tokens))
            return
    return program


def parse_statement(tokens):
    if tokens[0].type == "OPE":
        tokens.pop(0)
    else:
        print_error("(at parse_statement) statement doesnt start with | ")
        #pprint(tokens)
        return
    if len(tokens) > 2 and tokens[0].type == "VAR" and tokens[1].type == "ASS":
        return parse_assignment(tokens)
    return parse_expression(tokens)


def parse_expression_side(tokens):
    first = tokens.pop(0)
    if first.type == "OPE":
        return parse_expression(tokens)

    elif first.type == "NUM":
        return int(first.value)

    elif first.type == "VAR":
        return first.value

    else:
        print_error("at parse_expression_side")


def parse_expression(tokens):
    left = parse_expression_side(tokens)
    next_token = tokens.pop(0)
    if next_token.type == "CLO":
        value = left
        result = Expression(value=value)
    elif next_token.type == "OPP":
        operator = next_token.value
        right = parse_expression_side(tokens)
        result = Expression(left=left, right=right, operator=operator)
    else:
        print_error("at parse-expression")
    tokens.pop(0)
    return result


def parse_assignment(tokens):
    name = tokens.pop(0).value
    tokens.pop(0)
    expression = parse_statement(tokens)
    if tokens[0].type == "CLO":
        tokens.pop(0)
    else:
        print_error("incorrect assignment")
        return
    return Assignment(name, expression)
    
