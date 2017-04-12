import lexical, syntax, evaluator

from pprint import pprint

"""
make test and have ~10 sample strings

"""

#script = "| | 2 !ADD | 3 !ADD 1 > > !SUB | 5 !ADD 7 > >"

#script = "| ?x <- | 5 !ADD 7 > >"

script = "| 2 !ADD | 5 !ADD 7 > >"

tokens = lexical.tokenize(script)

pprint(tokens)

program = syntax.parse_program(tokens)

#for statement in program.statements:
#    print(statement)

#program = evaluator.traverse_graph_expressions(program)

print("STATEMENT", program.statements[0])

evaluator.evaluate_tree(program.statements[0])

print(program.statements[0].value)
