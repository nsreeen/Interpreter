import lexical, syntax, evaluator


"""
make test and have ~10 sample strings

"""

#script = "| | 2 !ADD | 3 !ADD 1 > > !SUB | 5 !ADD 7 > >"

script = "| ?x <- | 5 !ADD 7 > >"

tokens = lexical.tokenize(script)

print(tokens)

program = syntax.parse_program(tokens)

for statement in program.statements:
    print(statement)

program = evaluator.traverse_graph_expressions(program)
