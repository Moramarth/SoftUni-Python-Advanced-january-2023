algebraic_expression = input()

index_stack = list()

for index in range(len(algebraic_expression)):
    if algebraic_expression[index] == "(":
        index_stack.append(index)
    elif algebraic_expression[index] == ")":
        opening_parentheses = index_stack.pop()
        print(algebraic_expression[opening_parentheses:index + 1])
