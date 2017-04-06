"""
This part sends a token at a time to the next stage
(for now it just splits into a string)
"""
def tokenize(script):
    tokens = script.split(" ")
    return tokens
