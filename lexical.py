"""
This part sends a token at a time to the next stage
(for now it just splits into a string)
"""
import re
from collections import namedtuple


Token = namedtuple('Token', 'value type')


def tokenize(script):
    tokens = script.split(" ")
    tokenlist = []
    for token in tokens:
        token_type = process_token(token)
        #yield Token(token, token_type)
        tokenobject = Token(token, token_type)
        tokenlist.append(tokenobject)
    return tokenlist


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
