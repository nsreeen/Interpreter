import lexical, syntax, evaluator

#script = "| | 2 !ADD | 3 !ADD 1 > > !SUB | 5 !ADD 7 > >"

script = "| ?x <- | 5 !ADD 7 > > | 20 !ADD 10 >"

#script = "| 2 !MUL | 5 !ADD 7 > >"

tokens = lexical.tokenize(script)

program = syntax.parse_program(tokens)

#evaluator.evaluate_statement(program.statements[0])

#print(evaluator.evaluate_statement(program.statements[0]))

evaluator.evaluate_program(program)
