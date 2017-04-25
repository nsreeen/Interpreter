import lexer, parser, evaluator

#script = "| ?x <- | 5 !ADD 7 > > | 20 !ADD 10 > | ?x !ADD 1 >"

def interpret(script, dictionary):

    #print("compile running")

    tokens = lexer.tokenize(script)

    tokens = list(tokens)

    program = parser.parse_program(tokens, dictionary)

    program, dictionary = evaluator.evaluate_program(program, dictionary)

    """output = []

    for statement in program.statements:
        #print("statement")
        if isinstance(statement, syntax.Assignment):
            #output.append((statement.name + " = " + str(variables[statement.name])))
            pass
        elif isinstance(statement, syntax.Expression):
            #print("expression")
            output.append(statement.value)


    for line in output:
        print(line)"""

    return program, dictionary

if __name__ == "__main__":
    interpret(script)
