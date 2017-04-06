import lexical, syntax, tree_stuff


"""
make test and have ~10 sample strings

"""

script = "| | 2 !ADD | 3 !ADD 1 > > !SUB | 5 !ADD 7 > >"

tokens = lexical.tokenize(script)

print(tokens)

tree = tree_stuff.Tree()

for token in tokens:
    #print('token: ', token)
    token_type = syntax.process_token(token)
    tree = syntax.add_to_tree(tree, token_type, token)

tree_stuff.traverse_tree(tree.start)
