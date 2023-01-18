def balance_checker(stack, symbol):
    balanced = False
    if symbol == ")" and stack.pop() == "(":
        balanced = True
    elif symbol == "]" and stack.pop() == "[":
        balanced = True
    elif symbol == "}" and stack.pop() == "{":
        balanced = True

    return stack, balanced


parenthesis_sequence = input()

opening_parenthesis = ["{", "(", "["]
if parenthesis_sequence[0] not in opening_parenthesis:
    print("NO")
    exit()

opening_stack = list()
balanced_parenthesis = False


for character in parenthesis_sequence:
    if character in opening_parenthesis:
        opening_stack.append(character)
        continue
    if not opening_stack:
        balanced_parenthesis = False
        break
    else:
        opening_stack, balanced_parenthesis = balance_checker(opening_stack, character)
    if not balanced_parenthesis:
        break


if balanced_parenthesis:
    print("YES")
else:
    print("NO")
