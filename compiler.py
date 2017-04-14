import lexical, syntax, evaluator

#script = "| | 2 !ADD | 3 !ADD 1 > > !SUB | 5 !ADD 7 > >"

script = "| ?x <- | 5 !ADD 7 > > | 20 !ADD 10 >"

#script = "| 2 !MUL | 5 !ADD 7 > >"


def compile(script):

    tokens = lexical.tokenize(script)

    program = syntax.parse_program(tokens)

    program, variables = evaluator.evaluate_program(program)

    output = []

    for statement in program.statements:
        if isinstance(statement, syntax.Assignment):
            output.append(variables[statement.name])
        elif isinstance(statement, syntax.Expression):
            output.append(statement.value)

    return output

print(compile(script))
