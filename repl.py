import compiler, lexical, syntax, evaluator


def help_giver():
    print("print help")


print("!!! Press q to quit, h for help")

running = True

dictionary = {}

while running:

    user_input = input(">> ")

    #print("input got ")

    if user_input.lower() == "q":
        #print("quiting")
        running = False

    elif user_input.lower() == "h":
        print("get help")
        help_giver()

    elif user_input.lower() == "dictionary":
        print("dictionary")
        for k, v in dictionary.items():
            print(k, " : ", v.value) #__dict__)

    elif user_input in dictionary:
        print(dictionary[user_input].value)

    else:

        tree, dictionary = compiler.compile(user_input, dictionary)

        for statement in tree.statements:
            #print("statement")
            if isinstance(statement, syntax.Assignment):
                #output.append((statement.name + " = " + str(variables[statement.name])))
                pass
            elif isinstance(statement, syntax.Expression):
                #print("expression")
                print(statement.value)
