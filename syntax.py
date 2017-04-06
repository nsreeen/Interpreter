"""
This part takes token, and decides what type of token it is.
type -> how the tree is built
send back type and contents, and based on type the tree module decides what to do

script = "| ?x <- | 5 ADD 7 > >"
"""


import re
import tree_stuff


def process_token(token): #move to lexer (token should be a dict or tuple with token and type)
    token_types = { #regex meanings
    r'\?.+?': "VAR",
    r'\|': "OPE",
    r'\>': "CLO",
    r'\!...': "OPP",
    r'[0-9]+?': "NUM",
    r'<-': "ASS"
    }
    #iterate through dict keys
    for key in token_types.keys():
        if re.search(key, token):
            #print('val ', token_types[key])
            #return the nodes contents and type
            return token_types[key]

def add_to_tree(tree, token_type, token):
    print('\n')
    if tree.start:
        print('token is ', token, 'tree.current.contents: ', tree.current.contents)
    else:
        print('token is ', token, 'no nodes to see')

    if token_type == "OPE":
        print('if token_type == "OPE"')
        new_node = tree_stuff.Node()
        if tree.start == None: #if this is first node
            tree.start = new_node
            tree.current = new_node
        else: #add new child to current node, and set the child as the current node
            tree.current = tree.current.add_child(new_node)

    elif token_type == "CLO" and tree.current.parent != None:
        print('elif token_type == "CLO" and tree.current.parent != None:')
        tree.current = tree.current.parent
        print('change current to: ', tree.current.parent)

    elif token_type == "VAR" or token_type == "NUM":
        print('elif token_type == "VAR" or token_type == "NUM":')
        new_node = tree_stuff.Node()
        tree.current.add_child_with_contents(token, new_node)

    elif token_type == "ASS" or token_type == "OPP":
        print('elif token_type == "ASS" or token_type == "OPP": ')
        if tree.current.contents == None:
            tree.current.contents = token
        else:
            new_node = tree_stuff.Node()
            tree.current.add_child_with_contents(token, new_node)

    return tree
