
import re
from collections import namedtuple

Token = namedtuple('Token', 'value type')

def tokenize(script):
    tokens = script.split(" ")
    for token in tokens:
        token_type = process_token(token)
        yield Token(token, token_type)

def process_token(token):
    token_types = { #regex patterns for different token types
    r'\?.+?': "VAR",
    r'\|': "OPE",
    r'\>': "CLO",
    r'\!...': "OPP",
    r'[0-9]+?': "NUM",
    r'<-': "ASS"
    }
    #iterate through dict keys comparing pattern to current token
    for key in token_types.keys():
        if re.search(key, token):
            #return the type
            return token_types[key]
