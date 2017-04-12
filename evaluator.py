import syntax

def execute_calculation(left, right, op):
    if op == "!ADD":
        return left + right
    elif op == "!SUB":
        return left - right
    elif op == "!MUL":
        return left * right

def evaluate_tree(statement):
    print("evaluating")
    if statement.value != None:
        print("RESULT ===> ", statement.value)
        #return

        if isinstance(statement.left, syntax.Expression) and statement.left.value == None:
            statement.left.value = evaluate_tree(statement.left)

        if isinstance(statement.right, syntax.Expression) and statement.right.value == None:
            statement.right.value = evaluate_tree(statement.right)

    #if type(statement.left) == int:
    #    statement.left.value = left

        statement.value = statement.left + statement.right.value # execute_calculation(statement.left, statement.right.value, statement.operator)
        print("RESULT ===> ", statement.value)
    return
