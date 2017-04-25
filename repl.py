import interpreter, lexer, parser, evaluator


def help_giver():
    print('\n All expressions should be wrapped in open "|" and close ">".')
    print(' All variable names should start with "?". \n To assign use "<-". \n Operators are: \n "!ADD" \n "!SUB" \n "!MUL"\n ')
    print('Examples:\n "| 5 !MUL 7 >" \n "| | 2 !ADD | 3 !ADD 1 > > !SUB | 5 !ADD 7 > >" \n "| ?x <- | 1 > >" \n "| ?x <- | 5 !ADD 7 > > | 20 !ADD 10 >"\n')


print("!!! Press q to quit, h for help")

running = True

dictionary = {}

while running:

    try:
        user_input = input(">> ")

    except EOFError:
        user_input = 'q'

    if user_input.lower() == "q":
        running = False

    elif user_input.lower() == "h":
        help_giver()

    elif user_input.lower() == "dictionary":
        for k, v in dictionary.items():
            print(k, " : ", v.value)

    elif user_input in dictionary:
        print(dictionary[user_input].value)

    else:
        try:
            tree, dictionary = interpreter.interpret(user_input, dictionary)

            for statement in tree.statements:
                if isinstance(statement, parser.Assignment):
                    pass
                elif isinstance(statement, parser.Expression):
                    print(statement.value)
        except:
            print("\n Syntax error.  Type 'h' for help. \n")
