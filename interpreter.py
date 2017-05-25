import lexer, parser, evaluator


def interpret(script, dictionary):

    tokens = lexer.tokenize(script)

    tokens = list(tokens)

    program = parser.parse_program(tokens, dictionary)

    #import pdb; pdb.set_trace()

    program, dictionary = evaluator.evaluate_program(program, dictionary)

    return program, dictionary

stri = "| 3 !MUL | 5 !ADD 7 > > | 20 !ADD 10 >"

program, dicti = interpret(stri, {})
