import lexer, parser, evaluator

def interpret(script, dictionary):
    print(script)
    tokens = lexer.tokenize(script)

    tokens = list(tokens)

    program = parser.parse_program(tokens, dictionary)

    program, dictionary = evaluator.evaluate_program(program, dictionary)

    return program, dictionary

"""
#For debugging:
def print_object(obj, space=0):
    buf = space * 5 * '  '
    if isinstance(obj, parser.Expression):
        print('\n', buf, 'Expression object')
        for each in (obj.left, obj.right, obj.operator, obj.value):
            print(buf, each)
            if isinstance(each, parser.Expression):
                print('the expressions attribute is an expression,  ')
                print_object(each, space+1)
        print('\n')

    elif isinstance(obj, parser.Assignment):
        print('\n Assignment object')
        print(obj.name, obj.value)
        if isinstance(obj.value, parser.Expression):
            print('the assignments value is an expression, ')
            print_object(obj.value, space+1)
        print('\n')
"""
