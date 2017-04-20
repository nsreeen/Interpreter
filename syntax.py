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


def parse_program(tokens, dictionary):
    #print("\n in parse_program, tokens are ", tokens)
    program = Program()
    while tokens:
        statement = parse_statement(tokens, dictionary)
        if statement:
            program.statements.append(statement)
        else:
            print_error(("No statement found.  The next token is: ", tokens[0]))
            return
    return program


def parse_statement(tokens, dictionary):
    #print("\n in parse_statement, tokens are ", tokens)
    """if tokens[0].type == "OPE":
        tokens.pop(0)
    else:
        print_error("Statement doesn't start with | ")
        #pprint(tokens)
        return"""
    if len(tokens) > 2 and tokens[1].type == "VAR" and tokens[2].type == "ASS":
        return parse_assignment(tokens, dictionary)
    return parse_expression(tokens, dictionary)


def parse_expression_side(tokens, dictionary):
    #print("\n in parse_expression_side, tokens are ", tokens)
    first = tokens.pop(0)
    if first.type == "OPE":
        return parse_expression(tokens, dictionary)

    elif first.type == "NUM":
        return int(first.value)

    elif first.type == "VAR" and first.value in dictionary: #unnessesary?
        val = dictionary[first.value]
        return int(val.value)

    elif first.type == "VAR":
        return first.value

    else:
        print_error("Expression side could not be parsed")


def parse_expression(tokens, dictionary):
    #print("\n in parse_expression, tokens are ", tokens)
    if tokens[0].type == "OPE":
        tokens.pop(0)
    else:
        print_error("Statement doesn't start with | ")
        #pprint(tokens)
        return
    left = parse_expression_side(tokens, dictionary)
    #print("\n in parse_expression, left is ", left, "tokens are ", tokens)
    #next_token = tokens.pop(0)
    if tokens[0].type == "CLO": #expression is one thing
        #tokens.pop(0)
        value = left
        result = Expression(left=value, value=value)
    elif tokens[0].type == "OPP": #expression has opperator and left and right sides
        #tokens.pop(0)
        operator = tokens.pop(0).value
        right = parse_expression_side(tokens, dictionary)
        #print("\n in parse_expression, right is ", right, "tokens are ", tokens)
        result = Expression(left=left, right=right, operator=operator)
        """next_token = tokens.pop(0)
        if next_token.type == "CLO":
            print("\n in parse_expression, right is ", right, "tokens are ", tokens)
            result = Expression(left=left, right=right, operator=operator)
        else:
            print_error("Expression could not be parsed")
            return"""
    else:
        print_error("Expression could not be parsed")
        return
    if tokens[0].type == "CLO":
        tokens.pop(0)
        #print("closed expression, tokens: ", tokens)
    else:
        print_error("Assignment syntax incorrect")
        return
    return result


def parse_assignment(tokens, dictionary):
    #print("\n in parse_assignment, tokens are ", tokens)
    if tokens[0].type == "OPE":
        tokens.pop(0)
    else:
        print_error("Statement doesn't start with | ")
        #pprint(tokens)
        return

    name = tokens.pop(0).value
    #print("in parse_assignment, name is ", name, " tokens are ", tokens)
    tokens.pop(0)
    expression = parse_expression(tokens, dictionary) #parse_statement(tokens, dictionary)
    #print("in parse assignment - has taken name <- and expression.  next tokens are ", tokens)
    #print("expression val ", expression.value)
    if tokens[0].type == "CLO":
        tokens.pop(0)
    else:
        print_error("Assignment syntax incorrect")
        return
    return Assignment(name, expression)
