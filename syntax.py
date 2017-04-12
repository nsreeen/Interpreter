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
    def __init__(self, left=None, right=None, operator=None):
        self.left = left
        self.right = right
        self.operator = operator
        self.value = None
        self.expression = True #this must not be necessary


class Assignment():
    def __init__(self, name=None, value=None):
        self.name = name
        self.value = value
        self.expression = False


def print_error(message):
    print(message)


def parse_program(tokens):
    program = Program()
    while tokens:
        #if tokens[0].type == "OPE":
        statement = parse_statement(tokens)
        if statement:
            program.statements.append(statement)
            print('added statement: ', program.statements)
        else:
            print_error("no statement")
            return #should this be break???
    return program


def parse_statement(tokens):
    if tokens[0].type == "OPE": ###shouldnt be here incase assign an int
        tokens.pop(0)
    else:
        print_error("wrong syntax, missing | at parse_statement")
        return
    if len(tokens) > 2 and tokens[0].type == "VAR" and tokens[1].type == "ASS":
        return parse_assignment(tokens)
    return parse_expression(tokens)


def parse_expression(tokens): #assume no nested for now
    pprint(tokens)
    first = tokens.pop(0)
    pprint(tokens)
    if first.type == "NUM":
        left = int(first.value)
    elif first.type == "VAR":
        left = first.value
    elif first.type == "OPE":
        left = parse_expression(tokens)
    else:
        print_error(("incorrect expression syntax (first) ", first))
        return

    second = tokens.pop(0)
    if second.type == "OPP":
        operator = second.value
    else:
        print_error(("incorrect expression syntax (second) ", second))
        return

    pprint(tokens)
    third = tokens.pop(0)
    pprint(tokens)
    if third.type == "NUM":
        right = int(third.value)
    elif third.type == "VAR":
        right = third.value
    elif third.type == "OPE":
        right = parse_expression(tokens)
    else:
        print_error(("incorrect expression syntax (third) ", third))
        return

    if tokens[0].type == "CLO":
        tokens.pop(0)
    else:
        print_error(("incorrect end", tokens[0]))
        return

    return Expression(left=left, right=right, operator=operator)

"""| ?x <- | 5 !ADD 7 > >"""

def parse_assignment(tokens):
    print('parsing an assignment')
    name = tokens.pop(0).value
    tokens.pop(0)
    expression = parse_statement(tokens)
    if tokens[0].type == "CLO":
        tokens.pop(0)
    else:
        print_error(("incorrect expression syntax (third) ", third))
        return
    return Assignment(name, expression)
