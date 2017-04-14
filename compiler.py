import lexical, syntax, evaluator

def compile(script):

    tokens = lexical.tokenize(script)

    tokens = list(tokens)

    program = syntax.parse_program(tokens)

    program, variables = evaluator.evaluate_program(program)

    output = []

    for statement in program.statements:
        if isinstance(statement, syntax.Assignment):
            output.append(variables[statement.name])
        elif isinstance(statement, syntax.Expression):
            output.append(statement.value)

    return output

if __name__ == "__main__":
    print(compile(script))
