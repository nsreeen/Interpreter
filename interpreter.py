import lexer, parser, evaluator

def interpret(script, dictionary):
    print(script)
    tokens = lexer.tokenize(script)

    tokens = list(tokens)

    program = parser.parse_program(tokens, dictionary)

    program, dictionary = evaluator.evaluate_program(program, dictionary)

    return program, dictionary
